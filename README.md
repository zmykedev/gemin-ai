# FastAPI Google Gemini Agent

A modern FastAPI application with Google Gemini integration for AI-powered chat and text analysis capabilities.

## Features

- 🤖 **AI Chat**: Interactive chat with Google Gemini models
- 📊 **Text Analysis**: Sentiment analysis, summarization, and keyword extraction
- 🚀 **FastAPI**: High-performance async web framework
- 🔧 **Google Gemini**: Powerful generative AI capabilities
- 📝 **Auto-generated API docs**: Interactive documentation with Swagger UI

## Quick Start

### Prerequisites

- Python 3.8+
- Google API key (for Gemini API)

### Installation

1. **Clone or create the project**
   ```bash
   # If starting fresh
   mkdir fastapi-gemini-agent
   cd fastapi-gemini-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Create .env file and add your Google API key
   echo "GOOGLE_API_KEY=your_actual_api_key_here" > .env
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

   Or using uvicorn directly:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Access the application**
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

## API Endpoints

### Health Check
```http
GET /health
```

### Chat with AI
```http
POST /chat
Content-Type: application/json

{
  "message": "Hello, how are you?",
  "system_prompt": "You are a helpful AI assistant."
}
```

### Text Analysis
```http
POST /analyze
Content-Type: application/json

{
  "text": "Your text to analyze here",
  "analysis_type": "sentiment"  // "sentiment", "summary", or "keywords"
}
```

## Usage Examples

### Python Client Example

```python
import requests

# Chat with AI
chat_response = requests.post("http://localhost:8000/chat", json={
    "message": "What is the capital of France?",
    "system_prompt": "You are a helpful geography expert."
})
print(chat_response.json())

# Analyze text sentiment
analysis_response = requests.post("http://localhost:8000/analyze", json={
    "text": "I love this product! It's amazing and works perfectly.",
    "analysis_type": "sentiment"
})
print(analysis_response.json())
```

### cURL Examples

```bash
# Health check
curl http://localhost:8000/health

# Chat with AI
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Explain quantum computing in simple terms",
    "system_prompt": "You are a helpful science educator."
  }'

# Analyze text
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "This is a sample text for analysis",
    "analysis_type": "summary"
  }'
```

## Project Structure

```
fastapi-gemini-agent/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── test_client.py       # Test client for API endpoints
├── README.md           # This file
└── .env               # Your environment variables (create this)
```

## Configuration

### Environment Variables

- `GOOGLE_API_KEY`: Your Google API key for Gemini API (required)

### Getting a Google API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key and add it to your `.env` file

### Customization

You can easily customize the application by:

1. **Adding new analysis types** in the `/analyze` endpoint
2. **Modifying prompts** for different use cases
3. **Adding new endpoints** for specific tasks
4. **Integrating additional Google AI services**

## Development

### Running in Development Mode

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Testing

Run the test client to verify everything works:

```bash
python test_client.py
```

### Adding New Features

1. **New Endpoints**: Add new route functions in `main.py`
2. **Custom Prompts**: Create new prompt templates for specific tasks
3. **Error Handling**: Add additional error handling for specific use cases

## Troubleshooting

### Common Issues

1. **Google API Key Error**: Make sure your `.env` file contains a valid API key
2. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
3. **Port Already in Use**: Change the port in the uvicorn command or kill the process using the port
4. **API Rate Limits**: Google Gemini API has rate limits, consider adding retry logic for production use

### Getting Help

- Check the interactive API documentation at http://localhost:8000/docs
- Review the [Google Gemini API documentation](https://ai.google.dev/docs)
- Ensure your Google API key has the necessary permissions

## License

This project is open source and available under the MIT License. 