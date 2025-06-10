from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware # <--- ADD THIS LINE

# FastAPI application instance
app = FastAPI()

# <--- ADD THIS BLOCK FOR CORS MIDDLEWARE
origins = [
    "https://exam.sanand.workers.dev",  # Crucial: Allow the specific origin of your evaluation platform
    "https://tds-virtual-ta-9.onrender.com", # Your own API URL (sometimes needed for subpaths/internal calls)
    "http://localhost", # For local development
    "http://localhost:8000", # For local development
    # Add any other origins you need to allow
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)
# END OF CORS MIDDLEWARE BLOCK --->

# Pydantic model for the input question
class QuestionInput(BaseModel):
    question: str
    image: Optional[str] = None

# Pydantic model for a single link
class Link(BaseModel):
    url: str

# You will also have your API endpoint defined here.
# For example, your POST /api/ endpoint:
# @app.post("/api/")
# async def answer_question(question_data: QuestionInput):
#     # Your API logic goes here
#     # This is where you process the 'question_data.question'
#     # and return a JSON response, e.g.:
#     return {"answer": "This is a sample answer for: " + question_data.question}

# Make sure you have an actual API endpoint defined, like the one above,
# that matches what promptfoo and the submission system expect.
# The curl command implied a POST to /api/ that takes a 'question' and returns an 'answer'.