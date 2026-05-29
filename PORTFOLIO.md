# Juridico AI - Material para Portfolio

## Pitch curto

Desenvolvi uma API de IA juridica baseada em RAG para analisar contratos em PDF.
O sistema extrai o texto do documento, cria embeddings, salva os vetores em um
banco vetorial e responde perguntas em linguagem natural usando apenas os
trechos recuperados como contexto.

## Descricao para GitHub ou LinkedIn

Projeto backend em Python com FastAPI que aplica arquitetura RAG
(Retrieval-Augmented Generation) para consulta inteligente de contratos
juridicos. A API processa PDFs, divide o texto em chunks, gera embeddings com
Sentence Transformers, persiste vetores no ChromaDB e integra uma LLM via Groq
para responder perguntas com base no contexto recuperado.

## Bullets para curriculo

- Desenvolvi uma API REST com FastAPI para analise de documentos juridicos com IA generativa.
- Implementei pipeline RAG com extracao de PDF, chunking, embeddings, ChromaDB e LLM.
- Estruturei servicos modulares para processamento de documentos, busca semantica e geracao de respostas.
- Integrei banco vetorial persistente para recuperacao contextual de trechos relevantes.
- Retornei os trechos originais usados pela IA para aumentar rastreabilidade e confianca da resposta.

## Roteiro para video demo

Tempo ideal: 60 a 90 segundos.

1. Apresentar o problema:
   "Contratos longos sao demorados de revisar e muitas vezes e dificil localizar rapidamente riscos ou clausulas especificas."

2. Mostrar o upload:
   "Aqui envio um contrato em PDF para a API."

3. Mostrar a indexacao:
   "O sistema extrai o texto, divide em chunks, gera embeddings e salva os vetores no ChromaDB."

4. Fazer uma pergunta:
   "Agora pergunto: quais clausulas representam risco juridico?"

5. Mostrar a resposta:
   "A IA responde usando apenas os trechos recuperados do contrato."

6. Destacar o diferencial:
   "Alem da resposta, retorno o contexto original consultado, o que ajuda a validar a conclusao da IA."

7. Fechar com stack:
   "Esse projeto usa Python, FastAPI, LangChain, Sentence Transformers, ChromaDB e Groq."

## Melhor frase para abrir entrevista

"Eu quis construir algo alem de um chatbot. O foco foi montar um pipeline RAG completo, com ingestao de documento, busca vetorial e resposta contextualizada, aplicado a um problema real do setor juridico."

## Melhorias que valem ponto em entrevista

- Adicionar identificacao de pagina nos trechos recuperados.
- Classificar riscos por severidade: baixo, medio e alto.
- Permitir multiplos documentos por usuario.
- Adicionar testes automatizados para endpoints e servicos.
- Criar Dockerfile para facilitar execucao.
- Implementar OCR para contratos escaneados.
- Adicionar autenticacao e historico de consultas.
