from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_document(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(docs)
    return chunks