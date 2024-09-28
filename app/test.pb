from typing import Dict, Union

from fastapi import FastAPI
from pydantic import BaseModel
from settings import setting

app = FastAPI(
    title=setting.app.name, version=setting.app.version, debug=setting.app.debug
)

test: Dict[int, str] = {}


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = (None,)


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    item = test.get(item_id, {})
    return {"item": item, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    test[item_id] = item

    return {"name": item.name, "price": item.price, "is_offer": item.is_offer}
