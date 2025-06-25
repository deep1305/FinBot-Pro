# 📈 Agentic Trading Bot

A sophisticated AI-powered financial trading assistant that provides real-time market analysis, stock insights, and trading guidance using multiple data sources and APIs.

## 🚀 Features

- **Real-time Financial Data**: Integration with Polygon API for live stock prices and market data
- **Intelligent Document Processing**: Upload and query financial documents (PDFs, DOCX)
- **Multi-source Information**: Combines data from vector database, web search, and financial APIs
- **Current Market Awareness**: Always knows the current date and provides up-to-date analysis
- **Professional Financial Analysis**: Technical and fundamental analysis capabilities
- **Web Interface**: User-friendly Streamlit interface for easy interaction
- **RESTful API**: FastAPI backend for programmatic access

## 🛠️ Technologies Used

- **Backend**: FastAPI, LangChain, LangGraph
- **Frontend**: Streamlit
- **AI/ML**: OpenAI GPT-4, LangChain Agents
- **Vector Database**: Pinecone
- **Financial Data**: Polygon API
- **Search**: Tavily Search, Bing Search
- **Document Processing**: PyPDF, docx2txt
- **Environment Management**: Python-dotenv

## 📋 Prerequisites

- Python 3.10+
- API Keys for:
  - OpenAI
  - Polygon.io
  - Pinecone
  - Tavily (optional)
  - Bing Search (optional)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Agentic-Trading-Bot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   # Required API Keys
   OPENAI_API_KEY=your_openai_api_key_here
   POLYGON_API_KEY=your_polygon_api_key_here
   PINECONE_API_KEY=your_pinecone_api_key_here
   
   # Optional API Keys
   TAVILY_API_KEY=your_tavily_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   BING_SEARCH_API_KEY=your_bing_api_key_here
   ```

## 🚀 Usage

### Starting the Backend Server

1. **Run the FastAPI server**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8001 --reload
   ```

2. **Access the API documentation**
   - Swagger UI: http://localhost:8001/docs
   - ReDoc: http://localhost:8001/redoc

### Starting the Frontend Interface

1. **Run Streamlit interface** (in a separate terminal)
   ```bash
   streamlit run streamlit_ui.py
   ```

2. **Access the web interface**
   - Open your browser to: http://localhost:8501

## 📚 API Endpoints

### Upload Documents
```http
POST /upload
Content-Type: multipart/form-data

Upload financial documents (PDF, DOCX) to build knowledge base
```

### Query the Bot
```http
POST /query
Content-Type: application/json

{
  "question": "What's the current price of Apple stock?"
}
```

### Tool Analytics
```http
GET /analytics

Returns tool usage statistics for monitoring
```

## 📁 Project Structure

```
Agentic-Trading-Bot/
├── agent/                  # AI agent and workflow logic
│   ├── agents.py
│   └── workflow.py
├── config/                 # Configuration files
│   └── config.yaml
├── data_ingestion/         # Document processing pipeline
├── data_models/            # Pydantic models
├── exception/              # Custom exceptions
├── fallback_data/          # Offline financial documents
├── logging/                # Logging utilities
├── notebook/               # Jupyter notebooks for experiments
├── prompt_library/         # AI prompts and templates
├── static/                 # CSS and static files
├── templates/              # HTML templates
├── toolkit/                # Tools and API integrations
├── utils/                  # Utility functions
├── main.py                 # FastAPI application
├── streamlit_ui.py         # Streamlit frontend
└── requirements.txt        # Python dependencies
```

## 🔧 Configuration

### Adjusting AI Behavior

Edit `config/config.yaml`:

```yaml
retriever:
  top_k: 2                 # Number of documents to retrieve
  score_threshold: 0.7     # Relevance threshold

embedding_model:
  provider: "openai"
  model_name: "text-embedding-3-large"

llm:
  openai:
    provider: "openai"
    model_name: "gpt-4o"
```

### Available Tools

1. **Retriever Tool**: Searches uploaded documents
2. **Polygon API**: Real-time financial data
3. **Tavily Search**: Current financial news
4. **Bing Search**: Additional web information

## 📊 Monitoring

The application includes built-in analytics to track tool usage:

- **Backend Logs**: See which tools are called in your terminal
- **Analytics Endpoint**: Visit `/analytics` for usage statistics
- **Persistent Tracking**: Tool usage saved to `tool_usage_analytics.json`

## 🛡️ Security Considerations

- Store API keys in `.env` file (never commit to version control)
- Use environment variables for all sensitive configuration
- Implement rate limiting for production deployments
- Validate all user inputs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the AI framework
- [Polygon.io](https://polygon.io/) for financial data
- [Pinecone](https://pinecone.io/) for vector database
- [OpenAI](https://openai.com/) for language models

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page
2. Create a new issue with detailed description
3. Provide logs and error messages

## 🔄 Changelog

### v1.0.0 (2025-06-25)
- Initial release
- Multi-tool AI agent implementation
- Streamlit web interface
- FastAPI backend
- Document upload and processing
- Real-time financial data integration

---

**⚠️ Disclaimer**: This tool is for educational and research purposes only. All financial advice should be verified independently. Users should conduct their own research and consult financial advisors for investment decisions.
