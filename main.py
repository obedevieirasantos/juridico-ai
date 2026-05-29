from fastapi import FastAPI

from app.routes.upload_routes import router as upload_router
from app.routes.rag_routes import router as rag_router

app = FastAPI(
    title="Juridico AI RAG",
    description="API de busca semantica em documentos juridicos usando RAG, embeddings e ChromaDB",
    version="1.0.0",
)

app.include_router(upload_router)
app.include_router(rag_router)


@app.get("/")
def home():
    return {
        "msg": "API Juridico AI funcionando",
    }
