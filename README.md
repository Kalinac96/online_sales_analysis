# online_sales_analysis
# Python Inventory Management System

Ovaj projekat omogućava upravljanje proizvodima u inventaru i dodavanje proizvoda u korpu kupca.

## 📌 Klase i funkcionalnosti

### 1️⃣ **Product (`product.py`)**
- **Atributi:** `name`, `price`, `quantity`
- **Metode:**
  - `display_info()`: Prikazuje informacije o proizvodu.
  - `update_quantity(amount)`: Ažurira količinu proizvoda.

### 2️⃣ **ProductManager (`product_manager.py`)**
- **Atribut:** `products` - lista proizvoda.
- **Metode:**
  - `add_product(product)`: Dodaje novi proizvod u inventar.
  - `remove_product(name)`: Uklanja proizvod iz liste na osnovu imena.
  - `display_products()`: Prikazuje sve proizvode.
  - `total_inventory_value()`: Računa ukupnu vrednost inventara.

### 3️⃣ **Cart (`cart.py`)**
- **Atribut:** `cart_items` - lista proizvoda u korpi.
- **Metode:**
  - `add_to_cart(product, quantity)`: Dodaje proizvod u korpu.
  - `total_price()`: Računa ukupnu cenu proizvoda u korpi.
  - `display_cart()`: Prikazuje sadržaj korpe.

### 4️⃣ **Main (`main.py`)**
- Kreira instancu `ProductManager` i dodaje proizvode.
- Kreira instancu `Cart` i dodaje nasumične proizvode u korpu.
- Prikazuje sadržaj korpe i ukupnu cenu za naplatu.

