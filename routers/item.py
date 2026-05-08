from fastapi import APIRouter, Path, Query, HTTPException
from starlette import status
from cruds import item as item_cruds
from schemas import ItemCreate, ItemUpdate, ItemStatus, ItemResponse

router = APIRouter(prefix="/items", tags=["items"])

# ルーティング
@router.get("", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
async def find_all():
    return item_cruds.find_all()

# idで検索するルーティング
@router.get("/{id}" , response_model=ItemResponse)
async def find_by_id(id: int = Path(gt=0)):
    found_item = item_cruds.find_by_id(id)
    if not found_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return found_item

# nameを部分一致で検索するルーティング
@router.get("/", response_model=list[ItemResponse])
async def find_by_name(name: str = Query(min_length=1, max_length=20)):
    return item_cruds.find_by_name(name)

# アイテムを作成するルーティング
@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create(item_create: ItemCreate):
    return item_cruds.create(item_create)

# アイテムを更新するルーティング
@router.put("/{id}", response_model=ItemResponse  , status_code=status.HTTP_200_OK)
async def update(item_update: ItemUpdate, id: int = Path(gt=0)):
    updated_item = item_cruds.update(id, item_update)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not updated")
    return updated_item

# アイテムを削除するルーティング
@router.delete("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def delete(id: int = Path(gt=0)):
    delete_item = item_cruds.find_by_id(id)
    if not delete_item:
        raise HTTPException(status_code=404, detail="Item not deleted")
    return delete_item