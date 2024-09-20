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
    item = int(input("Choose product with number: "))
    for _ in products:
        if 1 <= item <= len(products):
            selected_product = products[item - 1]
            print(f"Ürün: {selected_product['name']}, Fiyat: {selected_product['price']}, Stok: {selected_product['stock']}")
            break
        else:
            print("Geçersiz ürün numarası.")
            break
    adet = int(input("Kaç adet almak istiyorsunuz:"))
    if selected_product['stock'] >= adet:
        print(f"Toplam fiyat: {selected_product['price']*adet} ürün sepete eklendi")
        selected_product['stock'] -= adet 
    else:
        print(f"Stokda yeterli ürün yok en fazla {selected_product['stock']} tane alabilirsiniz")
             
    

def show_cart():
    return 0
    
def checkout():
    return 0

def show_order_history():
     return 0   
 
def main():
  
    while True:
        print("\n1. Show products\n2. Add product to list(admin)\n3. Add product to cart\n4. Show cart\n5. Checkout\n6. View order history\n7. Exit")
        choice = int(input("Choose an option: "))
    
        match choice:
            case 1: 
                show_products()
            case 2:
                user = str(input("Username:"))
                passw= str(input("Password:"))
                if user == "admin" and passw == "0admin":
                    print("Login succesful")
                    name = str(input("Enter product name:"))
                    price = float(input("Enter product price:"))
                    stock = int(input("Enter product stock:"))
                    add_product(name,price,stock)
                else:
                    print("Invalid username or password, login failed")
                
            case 3: 
                add_to_cart()
            case 4: 
                show_cart()
            case 5: 
                checkout()
            case 6: 
                show_order_history()
            case 7: 
                return False
            case _: 
                print("Invalid number")
                 
                
                   
    
    
    
    
    
if __name__ == "__main__":
    main()    