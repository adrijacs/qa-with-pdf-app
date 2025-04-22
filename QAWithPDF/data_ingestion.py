from llama_index.core import Document
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from exception import customexception
from logger import logging

def load_data(uploaded_file):
    """
    Load document from the uploaded file.

    Parameters:
    - uploaded_file (file): The uploaded file object.

    Returns:
    - A list of Document objects.
    """
    try:
        logging.info("Data loading started...")
        
        # Read uploaded file
        file_contents = uploaded_file.read()
        file_name = uploaded_file.name
        
        # Check file type (for PDF or TXT)
        if file_name.endswith('.txt'):
            text = file_contents.decode('utf-8')
        elif file_name.endswith('.pdf'):
            import PyPDF2
            reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        else:
            raise ValueError("Unsupported file type. Please upload a PDF or TXT file.")
        
        # Create a Document object manually
        document = Document(text=text)
        
        logging.info("Data loading completed...")
        return [document]
    
    except Exception as e:
        logging.info("Exception in loading data...")
        raise customexception(e,sys)
