from product import Product
from product_manager import ProductManager

if __name__ == "__main__":
    manager = ProductManager()
    
#Dodavanje proizvoda
manager.add_product(Product("Televizor", 120000, 3))
manager.add_product(Product("Frizider", 85000, 2))
manager.add_product(Product("Ves masina", 70000, 4))

#Prikaz proizvoda i ukupne vrednosti
print("\nDostupni proizvodi:")
manager.display_products()

print("\nUkupna vrednost inventara:")
manager.total_value()