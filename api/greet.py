from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to your wix domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/greet")
async def greet(request: Request):
    data = await request.json()
    name = data.get("name", "World")
    print(f"📩 Received name: {name}")
    return JSONResponse({"message": f"Hello, {name}!"})