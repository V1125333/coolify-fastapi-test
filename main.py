from fastapi import FastAPI

app = FastAPI(title="FastAPI Docker Test")

@app.get("/")
def root():
    return {"message": "Hi 👋 We are checking if coolify is working! and trilok is one of them"}

@app.get("/health")
def health():
    return {"status": "ok"}
