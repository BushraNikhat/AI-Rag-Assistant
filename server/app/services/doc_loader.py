from langchain_community.document_loaders import DirectoryLoader, TextLoader

def load_documents():
    loader = DirectoryLoader(
        path="documents",
        glob="**/*.txt",
        loader_cls=TextLoader
    )
    docs = loader.load()
    return docs
