from fastapi import FastAPI
from settings import setting

app = FastAPI(
    title=setting.app.name, version=setting.app.version, debug=setting.app.debug
)


@app.get("/")
async def read_root():
    return {"message": "Hello World"}
