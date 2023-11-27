class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        

class ShoppingCart():
    def __init__(self):
        self.items = []
    
    def add_product(self, product, quantity=1):
        self.items.append({'product': product, 'quantity': quantity}) 
    
    def remove_product(self):
        item_name = input('Please enter the name of product you want to remove: ')
        for item in self.items:
            if item['product'].name == item_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['product'].price * item['quantity']
        return total


class Checkout():
    def __init__(self, cart):
        self.cart = cart
    
    def process_payment(self):
        total = self.cart.calculate_total()
        return total
    
    def print_receipt(self):
        print("Thank you for your purchase!")
        print("Receipt:")
        for item in self.cart.items:
            print(f"{item['product'].name} - Quantity: {item['quantity']} - Price: ${item['product'].price}")

    
# Creating some products
product1 = Product("Shirt", 20)
product2 = Product("Jeans", 30)
product3 = Product("Shoes", 50)

# Creating a shopping cart
cart = ShoppingCart()

# Adding products to the cart
cart.add_product(product1, 2)
cart.add_product(product2)
cart.add_product(product3)
# cart.remove_product(product3)

# Checking out
checkout = Checkout(cart)
checkout.print_receipt()
total_amount = checkout.process_payment()
print(f"Total amount charged: ${total_amount}")
