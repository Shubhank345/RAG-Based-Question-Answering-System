import streamlit as st
from rag_pipeline import build_qa_chain
st.set_page_config(page_title="LOCAL RAG APP",layout='wide')
st.title('RAG BASED QA')
uploaded_file=st.file_uploader("Upload your pdf or txt",type=['pdf','txt'])
if uploaded_file:
    qa=build_qa_chain(uploaded_file)
    query=st.text_input("Ask your question")
    if query:
        result=qa.invoke({'query':query})
        st.subheader("Answer")
        st.write(result['result'])