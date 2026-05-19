# ⚖️ Jurídico AI — Intelligent Legal RAG Platform

Plataforma de Inteligência Artificial Jurídica baseada em arquitetura **RAG (Retrieval-Augmented Generation)** para análise contextual de documentos legais utilizando IA Generativa, Embeddings Semânticos e Busca Vetorial.

---

# 🚀 Sobre o Projeto

O Jurídico AI foi desenvolvido para transformar documentos jurídicos em uma base consultável por linguagem natural, permitindo buscas semânticas inteligentes e respostas contextualizadas geradas por modelos de IA.

A solução combina:

* Processamento de documentos jurídicos
* Busca semântica
* Banco vetorial
* Embeddings
* Large Language Models (LLMs)
* APIs modernas
* Arquitetura modular escalável

---

# 🧠 Arquitetura da Solução

```text id="n8q3vr"
PDF → Extração de Texto → Chunking → Embeddings → ChromaDB → Recuperação Contextual → LLM → Resposta Inteligente
```

---

# ⚙️ Principais Funcionalidades

## ✅ Upload de PDFs Jurídicos

Suporte para contratos, pareceres, decisões, políticas e documentos legais.

## ✅ Extração Automática de Texto

Leitura e processamento completo do conteúdo do documento.

## ✅ Chunking Inteligente

Divisão semântica do texto para melhorar a recuperação contextual.

## ✅ Embeddings Vetoriais

Transformação do conteúdo textual em vetores semânticos.

## ✅ Banco Vetorial Persistente

Armazenamento vetorial utilizando ChromaDB.

## ✅ Busca Semântica

Recuperação de contexto baseada no significado da consulta.

## ✅ IA Generativa

Respostas contextualizadas utilizando LLMs de alta performance.

## ✅ API REST

Arquitetura moderna baseada em FastAPI.

---

# 🛠️ Stack Tecnológica

## Backend

* Python
* FastAPI
* Uvicorn

## Inteligência Artificial

* Sentence Transformers
* Embeddings Semânticos
* RAG Architecture
* Groq API

## Banco Vetorial

* ChromaDB

## Processamento de Documentos

* PyMuPDF

---

# 📂 Estrutura do Projeto

```text id="m5x2qw"
backend/
│
├── app/
│   ├── config/
│   │   └── settings.py
│   │
│   ├── routes/
│   │   ├── upload_routes.py
│   │   └── rag_routes.py
│   │
│   └── services/
│       ├── pdf_service.py
│       ├── chunk_service.py
│       ├── embedding_service.py
│       ├── chroma_service.py
│       └── llm_service.py
│
├── db/
├── .env
├── .gitignore
└── main.py
```

---

# 🔐 Segurança

O projeto utiliza:

* Variáveis de ambiente (`.env`)
* Proteção de credenciais
* `.gitignore`
* Separação modular de serviços

---

# ▶️ Execução do Projeto

## Clonar repositório

```bash id="p3n8wd"
git clone https://github.com/seu-usuario/juridico-ai.git
```

---

## Entrar no diretório

```bash id="k9m4xt"
cd juridico-ai/backend
```

---

## Ativar ambiente virtual

### Windows

```bash id="w2q7rv"
..\venv\Scripts\activate
```

---

## Instalar dependências

```bash id="y6r3mn"
pip install -r requirements.txt
```

---

## Configurar variáveis de ambiente

Criar arquivo `.env`

```env id="f8x5pt"
GROQ_API_KEY=sua_chave_api
```

---

## Executar servidor

```bash id="v4m2qa"
uvicorn main:app --reload
```

---

# 📚 Swagger Documentation

Após iniciar a API:

```text id="q7p3dk"
http://127.0.0.1:8000/docs
```

---

# 🔎 Fluxo de Utilização

## 1️⃣ Upload do Documento

```text id="h2w9mz"
/upload
```

---

## 2️⃣ Geração de Embeddings

```text id="u5r8xn"
/salvar-vetores
```

---

## 3️⃣ Consulta Inteligente

```text id="n4x6qp"
/buscar
```

---

# 📈 Evoluções Futuras

* Frontend interativo
* Memória conversacional
* Multi-document retrieval
* Deploy em Cloud
* Docker
* LangChain Integration
* OCR para PDFs escaneados
* Autenticação JWT
* Histórico de consultas
* Painel administrativo

---

# 👨‍💻 Desenvolvedor

**Obede Vieira dos Santos**

Especializado em soluções de Inteligência Artificial aplicada, sistemas RAG, NLP, automação inteligente e arquitetura de APIs para recuperação contextual de informação.
