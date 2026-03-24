from fastapi import FastAPI

app = FastAPI(title="Python Pipeline Blueprint")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/convert")
def convert(data: dict):
    return {"received": data, "converted": True}