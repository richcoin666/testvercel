from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from Vercel!"}

@app.post("/greet")
async def greet(request: Request):
    data = await request.json()
    name = data.get("name", "World")
    return JSONResponse({"message": f"Hello, {name}!"})