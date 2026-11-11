from fastapi import FastAPI

app = FastAPI(title="Carfolio")


@app.get("/")
async def root():
    return {"message": "Carfolio API работает"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
