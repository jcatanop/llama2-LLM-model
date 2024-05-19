# from langchain import PromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA

import time; 

DB_FAISS_PATH = "vectorstores/db_faiss/"

custom_prompt_template = """
Context : {context}
Question : {question}
"""

def set_custom_prompt():
    """
    Prompt template for QA retrieval for each vector stores.
    """
    prompt = PromptTemplate(template = custom_prompt_template, input_variables=['context','question'] )
    return prompt

def load_llm():
    llm = CTransformers(
        model = "llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type = "llama",
        max_new_tokens = 512,
        temperature = 0.5
    )
    return llm

def retrieval_qa_chain(llm, prompt, db):
    qa_chain = RetrievalQA.from_chain_type(
        llm = llm,
        chain_type = "stuff",
        retriever = db.as_retriever(search_kwargs={'k':2}),
        return_source_documents = True,
        chain_type_kwargs = {'prompt':prompt}
    )
    return qa_chain

def qa_bot():
    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2', model_kwargs = {'device':'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, db)
    return qa

def final_result(query):
    qa_result = qa_bot()
    response = qa_result({'query':query})
    print('\n- - - - - - - - - - - -   A N S W E R   - - - - - - - - - - - - ')
    print(response['result'])
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')

print("\nAsk something :")
query = input()
print("\n")
TimeStamp0 = time.time()
final_result(query)
TimeStamp1 = time.time()

print("Response time: %5.2f sec \n" % (TimeStamp1 -TimeStamp0)) 
