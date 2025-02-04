class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_info(self):
        """Prikazuje informacije o proizvodu"""
        print(f"Proizvod: {self.name}, Cena: {self.price:.2f} RSD, Kolicina: {self.quantity}")
        
    def update_quantity(self, amount):
        """Azurira kolicinu proizvoda dodavanjem ili oduzimanjem vrednosti amount."""
        if self.quantity + amount >=0:
            self.quantity += amount
            print(f"Nova kolicina proizvoda '{self.name}': {self.quantity}")
        else:
            print("Greska: Nedovoljno proizvoda na stanju!")
            