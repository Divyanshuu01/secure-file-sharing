# main.py

from fastapi import FastAPI
from routes import admin, client
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import os

app = FastAPI()

# CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(client.router, prefix="/client", tags=["Client"])

# Create the database tables if they don't exist
from models import Base
Base.metadata.create_all(bind=engine)

# Serve uploaded files
@app.get("/uploads/{filename}")
def get_uploaded_file(filename: str):
    file_path = os.path.join("uploads", filename)
    if not os.path.exists(file_path):
        return {"message": "File not found"}
    return {"file_path": file_path}

# Run the server with: uvicorn main:app --reload
