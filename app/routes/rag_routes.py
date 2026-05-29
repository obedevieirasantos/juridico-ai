from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from langchain_community.document_loaders import PyPDFLoader
import os

from app.services.chunk_service import criar_chunks
from app.services.embedding_service import gerar_embeddings
from app.services.chroma_service import salvar_vetores, buscar_documentos
from app.services.llm_service import gerar_resposta

router = APIRouter()

class PerguntaRequest(BaseModel):
    pergunta: str

# ALTERADO: Mudança para POST, pois altera o estado do banco de dados (gravação)
@router.post("/salvar-vetores", status_code=status.HTTP_201_CREATED)
def salvar_embeddings():
    caminho_pdf = "../storage/Contrato.pdf"
    
    # Boa prática: Validar se o arquivo realmente existe antes de processar
    if not os.path.exists(caminho_pdf):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Arquivo não encontrado em: {caminho_pdf}"
        )
    
    try:
        loader = PyPDFLoader(caminho_pdf)
        docs = loader.load()
        
        # DICA: Se o seu criar_chunks aceitar uma lista de Documentos (LangChain), 
        # mude para passar a lista 'docs' direto para preservar metadados das páginas.
        texto = "\n\n".join([doc.page_content for doc in docs])
        
        chunks = criar_chunks(texto)
        
        # Garantir que não vamos processar uma lista vazia
        if not chunks:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Não foi possível extrair texto ou gerar chunks deste PDF."
            )
            
        embeddings = gerar_embeddings(chunks)
        salvar_vetores(chunks, embeddings)
        
        return {
            "mensagem": "Vetores salvos com sucesso no ChromaDB",
            "total_chunks": len(chunks)
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Erro ao processar o PDF: {str(e)}"
        )

@router.post("/buscar")
def buscar_contexto(request: PerguntaRequest):
    try:
        pergunta = request.pergunta
        
        # Gera o embedding da pergunta
        pergunta_embedding = gerar_embeddings([pergunta])
        
        # Busca no ChromaDB usando o primeiro (e único) embedding gerado
        resultados = buscar_documentos(pergunta_embedding[0])
        
        # Tratamento de erro caso o banco retorne vazio
        if not resultados or "documents" not in resultados or not resultados["documents"][0]:
            return {
                "pergunta": pergunta,
                "resposta": "Não encontrei informações relevantes no documento para responder à sua pergunta.",
                "contexto": []
            }
            
        # Junta os documentos retornados para formar o contexto do LLM
        contexto = "\n".join(resultados["documents"][0])
        
        # Passa o contexto e a pergunta para o LLM
        resposta = gerar_resposta(contexto, pergunta)
        
        return {
            "pergunta": pergunta,
            "resposta": resposta,
            "contexto": resultados["documents"][0] # Retorna a lista linear de textos usados
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Erro ao realizar a busca: {str(e)}"
        )