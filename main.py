from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hi 👋 Coolify is working on Hetzner!"}
