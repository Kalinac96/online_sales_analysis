from product import Product

class ProductManager:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        """Dodavanje proizvoda u listu dostupnih proizvoda."""
        self.products.append(product)
        print(f"Proizvod '{product.name}' je dodat.")
        
    def display_products(self):
        """Prikazuje informacije o svim dostupnim proizvodima."""
        if not self.products:
            print("Nema dostupnih proizvoda.")
        else:
            for product in self.products:
                product.display_info()
                
    def total_value(self):
        """Prikazuje ukupnu vrednost svih proizvoda."""
        total = sum(product.price * product.quantity for product in self.products)
        print(f"Ukupna vrednost svih proizvoda: {total:.2f} RSD")