from functions import *


def main():
    while True:
        print("""
            ================================
                 MINI PRODUCT SYSTEM
            ================================
            1. Show All Products
            2. Sort By Price (ascending)
            3. Sort By Price (descending)
            4. Search By Name
            5. Search By ID
            6. Find The Cheapest Product
            7. Find The Most Expensive Product
            8. Update Product
            0. Exit
            ================================
        """)
        
        choice = input("Enter your choice: ")

        try:
            
            if choice == "1":
                for product in getAllProducts():
                    print(
                        f"ID: {product["id"]}  "
                        f"Name: {product["name"]}  "
                        f"Price: {product["price"]}"
                    )
                
            elif choice == "2":
                for product in sortByPriceAsc():
                    print(
                        f"ID: {product["id"]}  "
                        f"Name: {product["name"]}  "
                        f"Price: {product["price"]}"
                    )

            elif choice == "3":
                for product in sortByPriceDesc():
                    print(
                        f"ID: {product["id"]}  "
                        f"Name: {product["name"]}  "
                        f"Price: {product["price"]}"
                    )

            elif choice == "4":
                productName = input("Enter the product name: ")
                product = searchByName(productName)
                print(
                    f"ID: {product["id"]}  "
                    f"Name: {product["name"]}  "
                    f"Price: {product["price"]}"
                )

            elif choice == "5":
                productID = int(input("Enter the product ID: "))
                product = searchById(productID)
                print(
                    f"ID: {product["id"]}  "
                    f"Name: {product["name"]}  "
                    f"Price: {product["price"]}"
                )

            elif choice == "6":
                product = getCheapestProduct()
                print(
                    f"ID: {product["id"]}  "
                    f"Name: {product["name"]}  "
                    f"Price: {product["price"]}"
                )

            elif choice == "7":
                product = getMostExpensiveProduct()
                print(
                    f"ID: {product["id"]}  "
                    f"Name: {product["name"]}  "
                    f"Price: {product["price"]}"
                )

            elif choice == "8":
                productID = int(input("Enter the product ID to update: "))
                productName = input("Enter the new product name: ")
                productPrice = input("Enter the new product price: ")
                product = updateProduct(productID, productName, productPrice)
                print(
                    f"Updated product: ID: {product["id"]}  "
                    f"Name: {product["name"]}  "
                    f"Price: {product["price"]}"
                )

            elif choice == "0":
                print("Exiting")
                break
            else:
                print("Invalid choice. Enter a number from 0 to 8.")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()