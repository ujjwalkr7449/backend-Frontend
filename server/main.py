from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="React + FastAPI App")

# Allow requests from the React development server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name: str
  
  
#default api route    
@app.get("/")
def home():
    return {"message": "FastAPI backend is running!"}

@app.get("/api/users")
def get_users():
    return [
        {"id": 1, "name": "Ujjwal"},
        {"id": 2, "name": "Rahul"},
    ]


@app.get("/api/users")
def get_users():
    return [
        {"id": 1, "name": "Ujjwal"},
        {"id": 2, "name": "Rahul"},
    ]