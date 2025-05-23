# api/greet.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# ✅ Allow all origins for testing — later restrict this to your real Wix domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/greet")
async def greet(request: Request):
    data = await request.json()
    name = data.get("name", "World")
    return JSONResponse({"message": f"Hello, {name}!"})