from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import time; 

DATA_PATH = "data/"
DB_FAISS_PATH = "vectorstores/db_faiss"

# create vector database
def create_vector_db():
    loader = DirectoryLoader(DATA_PATH, glob = '*.pdf', loader_cls = PyPDFLoader )
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50 )
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2', model_kwargs = {'device':'cpu'})

    db = FAISS.from_documents(texts, embeddings)
    db.save_local(DB_FAISS_PATH)

if __name__ ==  '__main__':
    TimeStamp0 = time.time()
    create_vector_db()
    TimeStamp1 = time.time()
    print("Response time: %5.2f sec \n" % (TimeStamp1 -TimeStamp0)) 
