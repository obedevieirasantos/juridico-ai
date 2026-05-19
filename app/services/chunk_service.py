from langchain_text_splitters import RecursiveCharacterTextSplitter


def criar_chunks(texto):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_text(texto)

    return chunks