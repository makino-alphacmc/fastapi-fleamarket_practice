from fastapi import FastAPI, Body
from cruds import item as item_cruds

#インスタンス作成
app = FastAPI()

# ルーティング
@app.get("/items")
async def find_all():
    return item_cruds.find_all()

# idで検索するルーティング
@app.get("/items/{id}")
async def find_by_id(id: int):
    return item_cruds.find_by_id(id)

# nameを部分一致で検索するルーティング
@app.get("/items/")
async def find_by_name(name: str):
    return item_cruds.find_by_name(name)

# アイテムを作成するルーティング
@app.post("/items")
async def create(item_create=Body()):
    return item_cruds.create(item_create)

# アイテムを更新するルーティング
@app.put("/items/{id}")
async def update(id: int, item_update=Body()):
    return item_cruds.update(id, item_update)

# アイテムを削除するルーティング
@app.delete("/items/{id}")
async def delete(id: int):
    return item_cruds.delete(id)