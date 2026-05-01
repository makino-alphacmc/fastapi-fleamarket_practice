from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

# アイテムのステータスを表す列挙型
class ItemStatus(Enum):
    ON_SALE = "on_sale"
    SOLD_OUT = "sold_out"

# アイテムのスキーマ定義
class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=20, examples=["PC"])
    price: float = Field(gt=0, examples=[10000])
    description: Optional[str] = Field(None, examples=["美品です"])

# アイテムの更新用スキーマ定義
class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=20, examples=["PC"])
    price: Optional[int] = Field(None, gt=0, examples=[10000])
    description: Optional[str] = Field(None, examples=["美品です"])
    status: Optional[ItemStatus] = Field(None, examples=[ItemStatus.ON_SALE, ItemStatus.SOLD_OUT])

# アイテムのレスポンス用スキーマ定義
class ItemResponse(BaseModel):
    id: int = Field(gt=0, examples=[1])
    name: str = Field(min_length=2, max_length=20, examples=["PC"])
    price: int = Field(gt=0, examples=[10000])
    description: Optional[str] = Field(None, examples=["美品です"])
    status: ItemStatus = Field(examples=[ItemStatus.ON_SALE, ItemStatus.SOLD_OUT])
