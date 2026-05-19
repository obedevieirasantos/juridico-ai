from fastapi import APIRouter

from langchain_community.document_loaders import PyPDFLoader

from app.services.chunk_service import criar_chunks
from app.services.embedding_service import gerar_embeddings
from app.services.chroma_service import (
    salvar_vetores,
    buscar_documentos
)

from app.services.llm_service import gerar_resposta


router = APIRouter()


@router.get("/salvar-vetores")
def salvar_embeddings():

    loader = PyPDFLoader("../storage/Contrato.pdf")

    docs = loader.load()

    texto = "\n".join([doc.page_content for doc in docs])

    chunks = criar_chunks(texto)

    embeddings = gerar_embeddings(chunks)

    salvar_vetores(chunks, embeddings)

    return {
        "mensagem": "Vetores salvos no ChromaDB",
        "total_chunks": len(chunks)
    }


@router.get("/buscar")
def buscar_contexto(pergunta: str):

    pergunta_embedding = gerar_embeddings([pergunta])

    resultados = buscar_documentos(pergunta_embedding[0])

    contexto = "\n".join(resultados["documents"][0])

    resposta = gerar_resposta(contexto, pergunta)

    return {
        "pergunta": pergunta,
        "resposta": resposta,
        "contexto": resultados["documents"]
    }