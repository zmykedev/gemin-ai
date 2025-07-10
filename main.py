from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

app = FastAPI(
    title="FastAPI Google Gemini Agent",
    description="A FastAPI application with Google Gemini integration for AI-powered chat and text processing",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')  # Updated model name

# Pydantic models for request/response
class ChatRequest(BaseModel):
    message: str
    system_prompt: Optional[str] = "You are a helpful AI assistant docker."

class ChatResponse(BaseModel):
    response: str
    model: str

class TextAnalysisRequest(BaseModel):
    text: str
    analysis_type: str  # "sentiment", "summary", "keywords"

class TextAnalysisResponse(BaseModel):
    analysis: str
    type: str

# Routes
@app.get("/")
async def root():
    return {
        "message": "Welcome to FastAPI Google Gemini Agent",
        "endpoints": {
            "/chat": "POST - Chat with AI",
            "/analyze": "POST - Analyze text",
            "/health": "GET - Health check"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "FastAPI Google Gemini Agent"}

@app.post("/chat", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest):
    try:
        # Combine system prompt and user message
        full_prompt = f"{request.system_prompt}\n\nUser: {request.message}"
        
        # Get response from Google Gemini
        response = model.generate_content(full_prompt)
        
        return ChatResponse(
            response=response.text,
            model="gemini-1.5-flash"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")

@app.post("/analyze", response_model=TextAnalysisResponse)
async def analyze_text(request: TextAnalysisRequest):
    try:
        # Create different prompts based on analysis type
        if request.analysis_type == "sentiment":
            prompt = f"Analyze the sentiment of the following text and provide a brief explanation: {request.text}"
        elif request.analysis_type == "summary":
            prompt = f"Provide a concise summary of the following text: {request.text}"
        elif request.analysis_type == "keywords":
            prompt = f"Extract the key topics and keywords from the following text: {request.text}"
        else:
            raise HTTPException(status_code=400, detail="Invalid analysis type. Use 'sentiment', 'summary', or 'keywords'")
        
        # Get response from Google Gemini
        response = model.generate_content(prompt)
        
        return TextAnalysisResponse(
            analysis=response.text,
            type=request.analysis_type
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing text: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 