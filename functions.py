import json


def loadProducts():
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            return json.load(file)
        
    except json.JSONDecodeError as error:
        raise ValueError("The products JSON file is corrupted.") from error


def saveProducts(products):
    with open("products.json", "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4, ensure_ascii=False)


def productNotFound():
    raise ValueError("Product not found.")


def validateProductName(name):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Product name cannot be empty.")
    return name.strip()


def validateProductPrice(price):
    try:
        price = float(price)
    except (TypeError, ValueError) as error:
        raise ValueError("Product price must be a number.") from error

    if price < 0:
        raise ValueError("Product price cannot be negative.")
    return int(price) if price.is_integer() else price


def getAllProducts():
    return loadProducts()


def searchByName(productName):
    products = loadProducts()

    for product in products:
        if product["name"].casefold() == productName.strip().casefold():
            return product

    productNotFound()


def searchById(productID):
    products = loadProducts()

    for product in products:
        if product["id"] == productID:
            return product

    productNotFound()


def sortByPriceAsc():
    return sorted(loadProducts(), key=lambda product: product["price"])


def sortByPriceDesc():
    return sorted(
        loadProducts(), key=lambda product: product["price"], reverse=True
    )


def getCheapestProduct():
    products = loadProducts()
    if not products:
        productNotFound()
    return min(products, key=lambda product: product["price"])


def getMostExpensiveProduct():
    products = loadProducts()
    if not products:
        productNotFound()
    return max(products, key=lambda product: product["price"])


def updateProduct(productID, name, price):
    products = loadProducts()

    for product in products:
        if product["id"] == productID:
            product["name"] = validateProductName(name)
            product["price"] = validateProductPrice(price)
            saveProducts(products)
            return product

    productNotFound()
