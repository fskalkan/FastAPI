from fastapi import FastAPI, Path

app = FastAPI()

inventory = {
        1: {
            "name": "Milk",
            "price": 4.99,
            "brand": "Regular"
        }
    }

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, tanım = "görüntülemek istediğiniz öğenin ID'si")):
    return inventory[item_id]