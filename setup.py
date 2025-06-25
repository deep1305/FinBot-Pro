from setuptools import setup, find_packages

setup(name = "agentic-trading-system",
      version = "0.0.1",
      author = "deep",
      author_email = "shahdeep1399@gmail.com",
      packages = find_packages(),
      install_requires = ["lancedb", "langchain", "langgraph", "tavily-python", "polygon"]
)