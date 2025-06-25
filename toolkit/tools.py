import os
from pathlib import Path
from langchain.tools import tool
from langchain_community.tools import TavilySearchResults
from langchain_community.tools.polygon.financials import PolygonFinancials
from langchain_community.utilities.polygon import PolygonAPIWrapper
from langchain_community.tools.bing_search import BingSearchResults 
from data_models.models import RagToolSchema
from langchain_pinecone import PineconeVectorStore
from utils.model_loaders import ModelLoader
from utils.config_loader import load_config
from dotenv import load_dotenv
from pinecone import Pinecone
from prompt_library.prompt import get_prompt
import logging
from utils.tool_analytics import analytics

# Set up logging for tool usage tracking
logging.basicConfig(level=logging.INFO)
tool_logger = logging.getLogger("tool_usage")

load_dotenv()

# Get the Polygon API key from environment
polygon_api_key = os.getenv("POLYGON_API_KEY")
api_wrapper = PolygonAPIWrapper(polygon_api_key=polygon_api_key)
model_loader=ModelLoader()
config = load_config()

@tool(args_schema=RagToolSchema)
def retriever_tool(question):
    """
    Retrieves relevant financial information from the vector database.
    Use this tool to search through uploaded financial documents and trading guides.
    """
    tool_logger.info(f"🔍 RETRIEVER TOOL CALLED - Query: {question[:100]}...")
    print(f"[BACKEND LOG] Retriever tool called for: {question[:50]}...")
    analytics.log_tool_usage("retriever", question)
    
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    pc = Pinecone(api_key=pinecone_api_key)
    vector_store = PineconeVectorStore(index=pc.Index(config["vector_db"]["index_name"]), 
                            embedding= model_loader.load_embeddings())
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": config["retriever"]["top_k"] , "score_threshold": config["retriever"]["score_threshold"]},
    )
    retriever_result=retriever.invoke(question)
    
    return retriever_result

@tool
def polygon_financials_tool(query: str):
    """Get financial data using Polygon API for stocks, market data, and company financials"""
    tool_logger.info(f"📊 POLYGON API CALLED - Query: {query}")
    print(f"[BACKEND LOG] 🚀 Polygon API called for: {query}")
    analytics.log_tool_usage("polygon_api", query)
    
    try:
        financials_tool = PolygonFinancials(api_wrapper=api_wrapper)
        result = financials_tool.run(query)
        tool_logger.info(f"📊 POLYGON API SUCCESS - Got {len(str(result))} characters of data")
        print(f"[BACKEND LOG] ✅ Polygon API returned data successfully")
        return result
    except Exception as e:
        tool_logger.error(f"📊 POLYGON API ERROR: {str(e)}")
        print(f"[BACKEND LOG] ❌ Polygon API error: {str(e)}")
        return f"Error accessing Polygon API: {str(e)}"

tavilytool = TavilySearchResults(
    max_results=config["tools"]["tavily"]["max_results"],
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    )

@tool 
def tavily_search_tool(query: str):
    """Search current financial news and market updates using Tavily"""
    tool_logger.info(f"🌐 TAVILY SEARCH CALLED - Query: {query}")
    print(f"[BACKEND LOG] 🔍 Tavily search called for: {query}")
    analytics.log_tool_usage("tavily_search", query)
    
    try:
        result = tavilytool.invoke(query)
        tool_logger.info(f"🌐 TAVILY SEARCH SUCCESS - Got results")
        print(f"[BACKEND LOG] ✅ Tavily search returned results")
        return result
    except Exception as e:
        tool_logger.error(f"🌐 TAVILY SEARCH ERROR: {str(e)}")
        print(f"[BACKEND LOG] ❌ Tavily search error: {str(e)}")
        return f"Error accessing Tavily search: {str(e)}"

@tool
def bing_search_tool(query: str):
    """Search the web using Bing Search API for additional financial information"""
    tool_logger.info(f"🔍 BING SEARCH CALLED - Query: {query}")
    print(f"[BACKEND LOG] 🌐 Bing search called for: {query}")
    analytics.log_tool_usage("bing_search", query)
    
    try:
        bing_tool = BingSearchResults()
        result = bing_tool.run(query)
        tool_logger.info(f"🔍 BING SEARCH SUCCESS - Got results")
        print(f"[BACKEND LOG] ✅ Bing search returned results")
        return result
    except Exception as e:
        tool_logger.error(f"🔍 BING SEARCH ERROR: {str(e)}")
        print(f"[BACKEND LOG] ❌ Bing search error: {str(e)}")
        return f"Error accessing Bing Search API: {str(e)}"

def get_all_tools():
    """Return all available tools"""
    return [
        retriever_tool,
        polygon_financials_tool,
        tavily_search_tool,
        bing_search_tool
    ]

if __name__ == "__main__":
    tools = get_all_tools()
    print(f"Available tools: {[tool.name for tool in tools]}")
