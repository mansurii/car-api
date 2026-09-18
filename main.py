from fastapi import FastAPI
from routes import router
app = FastAPI(
    title="Cars API",
    description="CRUD API powered by FastAPI + Superbase",
    version="1.0.0"
)

app.include_router(router, prefix="/cars", tags=["Cars"])
@app.get("/")
def health_check():
    return {"status": "ok", "framework": "FastAPI"}