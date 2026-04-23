from typing import Optional
from enum import Enum
# アイテムのCRUD操作を行うモジュール

# アイテムのステータスを表す列挙型
class ItemStatus(Enum):
    ON_SALE = "on_sale"
    SOLD_OUT = "sold_out"

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
def create(item_create):
    new_item = Item(
        len(items) + 1,  # 新しいIDを生成
        item_create.get("name"),
        item_create.get("price"),
        item_create.get("description"),
        ItemStatus.ON_SALE,  # 新しいアイテムは販売中がデフォルト
    )
    items.append(new_item)
    return new_item

# アイテムを更新する関数
def update(id: int, item_update):
    for item in items:
        if item.id == id:
            item.name = item_update.get("name", item.name)
            item.price = item_update.get("price", item.price)
            item.description = item_update.get("description", item.description)
            item.status = item_update.get("status", item.status)
            return item
    return None

# アイテムを削除する関数
def delete(id: int):
    for item in items:
        if item.id == id:
            items.remove(item)
            return item
    return None