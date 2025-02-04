from product import Product
from product_manager import ProductManager
from cart import Cart

if __name__ == "__main__":
    manager = ProductManager()
    
#Dodavanje proizvoda u listu
product1 = Product("Televizor", 120000, 3))
product2 = Product("Frizider", 85000, 2))
product3 = Product("Ves masina", 70000, 4))
product4 = Product("Mikrotalasna", 15000, 5)
product5 = Product("Usisivac", 25000, 6)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.add_product(product4)
manager.add_product(product5)

#Prikaz proizvoda i ukupne vrednosti
print("\nDostupni proizvodi:")
manager.display_products()

#Kreiranje korpe
cart = Cart()

#Nasumicno dodavanje 3 proizvoda u korpu
selected_products = random.sample(manager.products, 3)
for product in selected_products:
    cart.add_to_cart(product, 1)
    
#Prikaz sadrzaja korpe
print("\nSadrzaj korpe:")
cart.display_cart()