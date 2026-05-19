import chromadb


client = chromadb.PersistentClient(path="../db")


collection = client.get_or_create_collection(
    name="documentos_juridicos"
)


def limpar_collection():

    ids = collection.get()["ids"]

    if ids:
        collection.delete(ids=ids)


def salvar_vetores(chunks, embeddings):

    limpar_collection()

    for i, chunk in enumerate(chunks):

        collection.add(
            documents=[chunk],
            embeddings=[embeddings[i].tolist()],
            ids=[f"doc_{i}"]
        )


def buscar_documentos(pergunta_embedding):

    resultados = collection.query(
        query_embeddings=[pergunta_embedding.tolist()],
        n_results=3
    )

    return resultados