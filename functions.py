import json


def loadProducts():
    try:
        with open("products.json", "r", encoding="utf-8") as f:
            products = json.load(f)

            return products

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        raise ValueError("JSON file is corrupted")

def saveExpenses(expenses):
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4, ensure_ascii=False)


def getAllProducts():
    return loadProducts()


def serachByName(productName):
    products = loadProducts()

    for p in products:
        if p["name"] == productName:
            return p
        
def searchByID(productID):
    products = loadProducts()
    
    for p in products:
        if p["id"] == productID:
            return p
