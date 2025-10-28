from app.schemas.item_schema import Item
from app.utils.exceptions import ItemNotFoundError
"""
 Input: 1, name: "Item1", value: 10.5
db[1] = Item(id=1, name="Item1", value=10.5)
 
 
"""

db: dict[int, Item] = {}


def create_item(item: Item):
    db[item.id] = item
    return item


def get_item(item_id: int) ->Item:
    if item_id not in db:
        raise ItemNotFoundError(f"Item with id {item_id} not found.")
    return db.get(item_id)


def update_item(item_id: int, item: Item) -> Item:
    if item_id not in db:
        raise ItemNotFoundError(f"Item with id {item_id} not found.")
    db[item_id] = item
    return item

def delete_item(item_id: int) -> None:
    if item_id not in db:
        raise ItemNotFoundError(f"Item with id {item_id} not found.")
    del db[item_id]
    
    
def list_items() -> list[Item]:
    return list(db.values())
    