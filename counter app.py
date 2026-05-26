import customtkinter as ctk
import sqlite3
from datetime import datetime

class POSApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Store POS System")
        self.geometry("1200x700")
        self.cart = []
        self.setup_database()
        self.create_ui()

    def setup_database(self):
        self.conn = sqlite3.connect('store.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                barcode TEXT UNIQUE,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER DEFAULT 0,
                category TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                receipt_no TEXT UNIQUE,
                total REAL,
                payment_method TEXT,
                sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sale_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sale_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                unit_price REAL,
                total_price REAL
            )
        ''')
        self.conn.commit()

    def create_ui(self):
        # Left Panel - Product Search & Selection
        left_frame = ctk.CTkFrame(self, width=400)
        left_frame.pack(side="left", fill="both", padx=10, pady=10)

        # Search Bar
        ctk.CTkLabel(left_frame, text="Search / Scan Barcode:",
        font=("Arial", 14)).pack(pady=5)
        self.search_var = ctk.StringVar()
        search_entry = ctk.CTkEntry(left_frame, textvariable=self.search_var,
        width=350, height=40, font=("Arial", 16))
        search_entry.pack(pady=5)
        search_entry.bind('<Return>', self.search_product)

        # Product List
        self.product_listbox = ctk.CTkTextbox(left_frame, width=350, height=500)
        self.product_listbox.pack(pady=10)

        # Right Panel - Cart & Checkout
        right_frame = ctk.CTkFrame(self, width=750)
        right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(right_frame, text="🛒 CART",
        font=("Arial", 20, "bold")).pack(pady=5)

        # Cart Display
        self.cart_display = ctk.CTkTextbox(right_frame, width=700, height=350,
        font=("Courier", 12))
        self.cart_display.pack(pady=5)

        # Totals
        totals_frame = ctk.CTkFrame(right_frame)
        totals_frame.pack(fill="x", padx=20, pady=10)

        self.subtotal_label = ctk.CTkLabel(totals_frame, text="Subtotal: ₹0.00",
        font=("Arial", 16))
        self.subtotal_label.pack()
        self.tax_label = ctk.CTkLabel(totals_frame, text="Tax: ₹0.00",                                       font=("Arial", 16))
        self.tax_label.pack()
        self.total_label = ctk.CTkLabel(totals_frame, text="TOTAL: ₹0.00",
        font=("Arial", 24, "bold"),
        text_color="green")
        self.total_label.pack()

        # Buttons
        btn_frame = ctk.CTkFrame(right_frame)
        btn_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkButton(btn_frame, text="💵 Cash Payment", width=200, height=50,
                      fg_color="green", command=self.cash_payment).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="💳 Card Payment", width=200, height=50,
                      fg_color="blue", command=self.card_payment).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="🗑️ Clear Cart", width=150, height=50,
                      fg_color="red", command=self.clear_cart).pack(side="left", padx=5)

    def search_product(self, event=None):
        query = self.search_var.get()
        self.cursor.execute(
            "SELECT * FROM products WHERE barcode=? OR name LIKE ?",
            (query, f"%{query}%")
        )
        results = self.cursor.fetchall()
        if results:
            for product in results:
                self.add_to_cart(product)
        self.search_var.set("")

    def add_to_cart(self, product):
        # product: (id, barcode, name, price, stock, category)
        item = {
            'id': product[0],
            'name': product[2],
            'price': product[3],
            'quantity': 1,
            'total': product[3]
        }

        # Check if already in cart
        for cart_item in self.cart:
            if cart_item['id'] == item['id']:
                cart_item['quantity'] += 1
                cart_item['total'] = cart_item['price'] * cart_item['quantity']
                self.update_cart_display()
                return

        self.cart.append(item)
        self.update_cart_display()

    def update_cart_display(self):
        self.cart_display.delete("1.0", "end")
        header = f"{'Item':<30} {'Qty':>5} {'Price':>10} {'Total':>10}\n"
        self.cart_display.insert("end", header)
        self.cart_display.insert("end", "-" * 60 + "\n")

        subtotal = 0
        for item in self.cart:
            line = f"{item['name']:<30} {item['quantity']:>5} {item['price']:>10.2f} {item['total']:>10.2f}\n"
            self.cart_display.insert("end", line)
            subtotal += item['total']

        tax = subtotal * 0.05  # 5% tax
        total = subtotal + tax

        self.subtotal_label.configure(text=f"Subtotal: ₹{subtotal:.2f}")
        self.tax_label.configure(text=f"Tax (5%): ₹{tax:.2f}")
        self.total_label.configure(text=f"TOTAL: ₹{total:.2f}")

    def cash_payment(self):
        self.process_payment("cash")

    def card_payment(self):
        self.process_payment("card")

    def process_payment(self, method):
        if not self.cart:
            return

        subtotal = sum(item['total'] for item in self.cart)
        tax = subtotal * 0.05
        total = subtotal + tax
        receipt_no = f"INV-{datetime.now().strftime('%Y%m%d%H%M%S')}"

        # Save to database
        self.cursor.execute(
            "INSERT INTO sales (receipt_no, total, payment_method) VALUES (?, ?, ?)",
            (receipt_no, total, method)
        )
        sale_id = self.cursor.lastrowid

        for item in self.cart:
            self.cursor.execute(
                "INSERT INTO sale_items (sale_id, product_id, quantity, unit_price, total_price) VALUES (?, ?, ?, ?, ?)",
                (sale_id, item['id'], item['quantity'], item['price'], item['total'])
            )
            # Update stock
            self.cursor.execute(
                "UPDATE products SET stock = stock - ? WHERE id = ?",
                (item['quantity'], item['id'])
            )

        self.conn.commit()
        self.print_receipt(receipt_no, total)
        self.clear_cart()

    def print_receipt(self, receipt_no, total):
        # Generate and print receipt
        print(f"Receipt {receipt_no} generated. Total: ₹{total:.2f}")

    def clear_cart(self):
        self.cart = []
        self.update_cart_display()

if __name__ == "__main__":
    app = POSApplication()
    app.mainloop()
