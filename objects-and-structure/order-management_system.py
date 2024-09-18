products = [
    {"name": "Phone", "price": 500, "stock": 10},
    {"name": "Laptop", "price": 1500, "stock": 5},
    {"name": "Headphones", "price": 150, "stock": 20},
    {"name": "Tablet", "price": 300, "stock": 7}
]

def add_product(name,price,stock):
    products.append({"name": name, "price": price, "stock": stock})

def show_products():
    print("--Product Catalog--")
    for i ,product in enumerate(products, start=1):
        print(f"Product {i}:",product["name"])

def add_to_cart():
    show_products()

def show_cart():
    return 0
    
def checkout():
    return 0

def show_order_history():
     return 0   
 
def main():
    
    while True:
        print("\n1. Show products\n2.Add product to list\n3. Add product to cart\n4. Show cart\n5. Checkout\n6. View order history\n7. Exit")
        choice = input("Choose an option: ")
    
        match choice:
            case 1: show_products()
            case 2: add_product(name,price,stok)
            case 3: add_to_cart()
            case 4: show_cart()
            case 5: checkout()
            case 6: show_order_history()
            case 7: return False
            case _: print("Invalid number")
                 
                
                   
    show_products()
    add_product("Router",120,5)
    
    
    
if __name__ == "__main__":
    main()    