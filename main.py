from fastapi import FastAPI

app = FastAPI(title="FastAPI Docker Test")

@app.get("/")
def root():
    return {"message": "Hi 👋 We are checking if coolify is working!"}

@app.get("/health")
def health():
    return {"status": "ok"}
