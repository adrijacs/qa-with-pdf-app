import streamlit as st
import sys
import os
import nltk

NLTK_DATA_DIR = '/tmp/nltk_data'
os.makedirs(NLTK_DATA_DIR, exist_ok=True)
nltk.data.path.append(NLTK_DATA_DIR)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', download_dir=NLTK_DATA_DIR)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'QAWithPDF')))
from data_ingestion import load_data
from embedding import download_gemini_embedding
from model_api import load_model


# Set a writable cache dir for tiktoken to avoid permission errors
os.environ["TIKTOKEN_CACHE_DIR"] = "/tmp/tiktoken_cache"


    
def main():
    st.set_page_config("QA with Documents")
    
    doc=st.file_uploader("upload your document")
    if 'query_engine' not in st.session_state:
        st.session_state.query_engine = None
    
    st.header("QA with Documents(Information Retrieval)")
    
    user_question= st.text_input("Ask your question")
    
    if st.button("submit & process"):
        if doc is None:
            st.error("Please upload a document before submitting.")
        else:
            with st.spinner("Processing..."):
                document=load_data(doc)
                model=load_model()
                query_engine=download_gemini_embedding(model,document)
                
                response = query_engine.query(user_question)
                
                st.write(response.response)
                
                
if __name__=="__main__":
    main()          
                
    
    
    
    
    