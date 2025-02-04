from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []
        
    def add_to_cart(self, product, quantity):
        """Dodaje proizvod u korpu ako postoji na stanju."""
        if product.quantity >= quantity:
            self.cart_items.append((product, quantity))
            product.update_quantity(-quantity)
            print(f"Dodato {quantity} x {product.name} u korpu")
        else:
            print(f"Nedovoljno na stanju za proizvod: {product.name}")
            
    def total_price(self):
        """Racuna ukupnu vrednost proizvoda u korpi."""
        return sum(product.price * quantity for product, quantity in self.cart_items)
    
    def display_cart(self):
        """Prikazuje sadrzaj korpe."""
        if not self.cart_items:
            print("Korpa je prazna.")
        else:
            print("Sadrzaj korpe:")
            for product, quantity in self.cart_items:
                print(f"{quantity} x {product.name} - {product.price * quantity:.2f} RSD")
            print(f"Ukupna vrednost za naplatu: {self.total_price():.2f} RSD") 