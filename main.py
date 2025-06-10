from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

# FastAPI application instance
app = FastAPI()

# CORS middleware (as we added before)
origins = [
    "https://exam.sanand.workers.dev",
    "https://tds-virtual-ta-9.onrender.com",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for the input question
class QuestionInput(BaseModel):
    question: str
    image: Optional[str] = None

# Pydantic model for a single link (if used)
class Link(BaseModel):
    url: str

# ********* ADD THIS API ENDPOINT *********

class AnswerResponse(BaseModel):
    answer: str
    sources: list[str]
    timestamp: str

@app.post("/api/", response_model=AnswerResponse) # This decorator defines a POST endpoint at the /api/ path
async def answer_question(question_data: QuestionInput):
    # This is where your actual API logic would go to process the question.
    # For now, let's return a simple placeholder response to confirm it works.
    print(f"Received question: {question_data.question}") # This will appear in Render logs
    return AnswerResponse(
        answer=f"You asked: {question_data.question}",
        sources=["example_source"],
        timestamp="2025-06-11T00:00:00Z"
    )
    # The submission platform might expect a specific response format,
    # so ensure your actual logic returns what's expected.
    # The 'answer' key is important because promptfoo was configured for it.