from typing import Optional
from fastapi import APIRouter
from cruds import item as item_cruds
from schemas import ItemCreate, ItemUpdate, ItemStatus, ItemResponse

router = APIRouter(prefix="/items", tags=["items"])

# ルーティング
@router.get("", response_model=list[ItemResponse])
async def find_all():
    return item_cruds.find_all()

# idで検索するルーティング
@router.get("/{id}" , response_model=Optional[ItemResponse])
async def find_by_id(id: int):
    return item_cruds.find_by_id(id)

# nameを部分一致で検索するルーティング
@router.get("/", response_model=list[ItemResponse])
async def find_by_name(name: str):
    return item_cruds.find_by_name(name)

# アイテムを作成するルーティング
@router.post("", response_model=ItemResponse)
async def create(item_create: ItemCreate):
    return item_cruds.create(item_create)

# アイテムを更新するルーティング
@router.put("/{id}", response_model=Optional[ItemResponse])
async def update(id: int, item_update: ItemUpdate):
    return item_cruds.update(id, item_update)

# アイテムを削除するルーティング
@router.delete("/{id}", response_model=Optional[ItemResponse])
async def delete(id: int):
    return item_cruds.delete(id)