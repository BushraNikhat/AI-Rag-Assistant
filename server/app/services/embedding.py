from langchain_ollama import OllamaEmbeddings

def embedd_chunks(chunked_doc):
    text = [chunks.page_content for chunks in chunked_doc]
    embed = OllamaEmbeddings(model="nomic-embed-text")
    vectors = embed.embed_documents(text)
    return vectors