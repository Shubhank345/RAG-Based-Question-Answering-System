from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama
import tempfile

def build_qa_chain(file):
   #Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file.read())
        file_path = tmp.name

    if file.name.endswith('.pdf'):
        loader=PyPDFLoader(file_path)
    else:
        loader=TextLoader(file_path)
    docs=loader.load()
    #TEXT SPLITTING
    splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)
    split_doc=splitter.split_documents(docs)
    #EMBEDDING
    embedding_model=OllamaEmbeddings(model='mistral')
    #VECTOR STORE
    vector_db=FAISS.from_documents(split_doc,embedding_model)
    #Retriever
    retriever=vector_db.as_retriever(search_kwargs={'k':3})
    llm=ChatOllama(model='mistral')
    
    qa= RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa

