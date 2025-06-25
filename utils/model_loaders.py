import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from utils.config_loader import load_config
from langchain_groq import ChatGroq

class ModelLoader:
    """
    A utility class to load embedding models and LLM models.
    """
    def __init__(self):
        load_dotenv()
        self._validate_env()
        self.config=load_config()

    def _validate_env(self):
        """
        Validate necessary environment variables.
        """
        required_vars = ["OPENAI_API_KEY"]
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            raise EnvironmentError(f"Missing environment variables: {missing_vars}")

    def load_embeddings(self):
        """
        Load and return the embedding model.
        """
        print("Loading Embedding model")
        model_name=self.config["embedding_model"]["model_name"]
        return OpenAIEmbeddings(model=model_name)

    def load_llm(self):
        """
        Load and return the LLM model.
        """
        print("LLM loading...")
        
        model_name = self.config["llm"]["openai"]["model_name"]
        print(f"Using OpenAI model: {model_name}")
        
        openai_api_key = os.getenv("OPENAI_API_KEY")
        openai_model = ChatOpenAI(
            model=model_name, 
            api_key=openai_api_key,
            max_tokens=4000,  
            temperature=0.1   
        )
        
        return openai_model