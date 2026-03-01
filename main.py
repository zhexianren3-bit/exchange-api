from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "汇率API"}
@app.get("/rate")
def rate(from_: str = "USD", to: str = "CNY"):
    return {"success": True, "rate": 7.2, "from": from_, "to": to}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
