from product import Product
from product_manager import ProductManager
if __name__ == "__main__":
    manager = ProductManager()
    
#Dodavanje proizvoda
manager.add_product(Product("Smart TV", 120000, 3))
manager.add_product(Product("Frizider", 85000, 5))
manager.add_product(Product("Blender", 70000, 4))
