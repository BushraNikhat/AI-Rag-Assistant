from app.services.doc_loader import load_documents
from app.services.chunking import chunk_document
from app.services.embedding import embedd_chunks

def document_ingestion_pipeline():
    # call the document loader service for loading documents
    documents = load_documents()
    
    # call chunking service to chunk the loaded documents
    chunks =  chunk_document(documents)

    # call embedding service to embedd the chunks
    vectors= embedd_chunks(chunks)

    print(vectors)

document_ingestion_pipeline()