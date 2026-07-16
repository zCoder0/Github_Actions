from fastapi.responses import FileResponse
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def index():
    return FileResponse("index.html")