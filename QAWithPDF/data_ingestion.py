from llama_index.core import SimpleDirectoryReader, Document
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

        # Save the uploaded file temporarily
        temp_dir = "temp_uploaded_files"
        os.makedirs(temp_dir, exist_ok=True)
        temp_file_path = os.path.join(temp_dir, uploaded_file.name)

        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Now read the uploaded file using SimpleDirectoryReader
        loader = SimpleDirectoryReader(temp_dir)
        documents = loader.load_data()

        # Clean up (optional: remove the uploaded file after loading)
        os.remove(temp_file_path)

        logging.info("Data loading completed...")
        return documents
    
    except Exception as e:
        logging.info("Exception in loading data...")
        raise customexception(e,sys)
