from langchain_community.document_loaders import PyPDFLoader


def carregar_pdf(caminho_pdf):

    loader = PyPDFLoader(caminho_pdf)

    docs = loader.load()

    texto = "\n".join([doc.page_content for doc in docs])

    return texto