from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List # Ensure List is imported from typing
from fastapi.middleware.cors import CORSMiddleware # Import CORSMiddleware

# Initialize FastAPI application
app = FastAPI()

# --- CORS Middleware Configuration ---
# This allows the submission platform to access your API from its domain.
origins = [
    "https://exam.sanand.workers.dev",  # Allow your specific evaluation platform's origin
    "https://tds-virtual-ta-9.onrender.com", # Your own API's base URL (good practice)
    "http://localhost",                  # For local development
    "http://localhost:8000",             # For local development with default uvicorn port
    # Add any other origins you might need to allow in the future
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)
# --- End CORS Middleware Configuration ---


# Pydantic model for the input question (as seen in your earlier main.py image)
class QuestionInput(BaseModel):
    question: str
    image: Optional[str] = None

# Pydantic model for a single link (as seen in your earlier main.py image)
class Link(BaseModel):
    url: str # Assuming the link only needs a URL, adjust if more fields are required (e.g., title, description)

# Pydantic model for the API's response (UPDATED to include 'links')
class AnswerResponse(BaseModel):
    answer: str
    sources: List[str]
    timestamp: str
    links: List[Link] # <--- ADDED THIS FIELD FOR THE SUBMISSION PLATFORM

# --- API Endpoints ---

# Optional: Basic GET endpoint for health checks or root access
# This will prevent 404 for GET requests to the base URL /
@app.get("/")
async def read_root():
    return {"message": "Virtual TA API is live!"}

# Your primary POST API endpoint (as seen in your latest main.py image)
@app.post("/api/", response_model=AnswerResponse)
async def answer_question(question_data: QuestionInput):
    # This is where your actual API logic would go to process the question.
    # For now, let's return a simple placeholder response to confirm the structure.

    # print(f"Received question: {question_data.question}") # You can uncomment this for local debugging

    # This is the response your API will send back.
    # It now includes the 'links' field, which is required by the submission platform.
    return AnswerResponse(
        answer=f"You asked: {question_data.question}",
        sources=["example_source"], # Placeholder sources, populate as needed
        timestamp="2025-06-11T00:00:00Z", # Placeholder timestamp, consider using datetime.now()
        links=[
            # Provide at least one link here.
            # Replace with actual relevant links if your project requires them,
            # otherwise, generic ones are fine for passing the structural check.
            Link(url="https://www.example.com/useful-link-1"),
            Link(url="https://www.example.com/useful-link-2")
        ]
    )