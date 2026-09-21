from app.services.doc_loader import load_documents
from app.services.chunking import chunk_document

documents = load_documents()
chunks =  chunk_document(documents)

print("The documents",chunks.page_content)
# print("The documents are metadata",documents[0].metadata)