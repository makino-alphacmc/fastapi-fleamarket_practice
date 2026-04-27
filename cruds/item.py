from typing import Optional
from schemas import ItemCreate, ItemStatus, ItemUpdate

# アイテムのCRUD操作を行うモジュール

# アイテムクラス
class Item:
    def __init__(
            self,
            id: int,
            name: str,
            price: int,
            description: Optional[str],
            status: ItemStatus,
    ): #コンストラクタ
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.status = status

# モックデータ
items = [
    Item(1, "iPhone 12", 799, "A brand new iPhone 12", ItemStatus.ON_SALE),
    Item(2, "MacBook Pro", 1299, "A powerful laptop for professionals", ItemStatus.ON_SALE),
    Item(3, "AirPods Pro", 249, "Noise-cancelling wireless earbuds", ItemStatus.SOLD_OUT),
]

# 全てのアイテムを取得する関数
def find_all():
    return items

# idで検索する関数
def find_by_id(id: int):
    for item in items:
        if item.id == id:
            return item
    return None

# nameを部分一致で検索する関数
def find_by_name(name: str):
    filtered_items = []

    for item in items:
        if name in item.name:
            filtered_items.append(item)
    return filtered_items

# アイテムを作成する関数
def create(item_create: ItemCreate):
    new_item = Item(
        len(items) + 1,  # 新しいIDを生成
        item_create.name,
        item_create.price,
        item_create.description,
        ItemStatus.ON_SALE,  # 新しいアイテムは販売中がデフォルト
    )
    items.append(new_item)
    return new_item

# アイテムを更新する関数
def update(id: int, item_update: ItemUpdate):
    for item in items:
        if item.id == id:
            item.name = item.name if item_update.name is None else item_update.name
            item.price = item.price if item_update.price is None else item_update.price
            item.description = item.description if item_update.description is None else item_update.description
            item.status = item_update.status if item_update.status is None else item_update.status
            return item
    return None

# アイテムを削除する関数
def delete(id: int):
    for item in items:
        if item.id == id:
            items.remove(item)
            return item
    return None