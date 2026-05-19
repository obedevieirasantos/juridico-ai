from fastapi import FastAPI

from app.routes.upload_routes import router as upload_router
from app.routes.rag_routes import router as rag_router

app = FastAPI(
    title="IA Jurídica RAG",
    description="API de busca semântica em documentos jurídicos usando RAG, embeddings e ChromaDB",
    version="1.0.0"
)

app.include_router(upload_router)
app.include_router(rag_router)


@app.get("/")
def home():
    return {
        "msg": "API Jurídico AI funcionando"
    }