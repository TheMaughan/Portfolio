#- Python program created by Bryce Maughan
class Product: #- This Class gathers all the product's data and returns a few calculations concerning
    #-                  the individual products only:
    def __init__(self, id, name, price, quantity): #- Initializes to the values that were passed:
        #- The variable deffinitions in the "init"'s parenthesis are created in the main funtion.
        
        #- In main function: variable = Class(bool, str, float, int)
        #- The values in the parenthesis are possible variable types that can be called in 
        #-      an '__init__' function's '()'.

        #- The class variables below uses the values in the init parenthesis in thie order:
        #-      'str', 'str', float, integer
        self.id = id #- 'str'
        self.name = name #- 'str'
        self.price = price #- float
        self.quantity = quantity #- integer

    
    def get_total_price(self): #- Multiply the price of the product with the number of the same product ordered:
        return self.price * self.quantity #- Class functions can behave like variables, in this case the multiple
        #- of the two variables is saved within 'self.get_total_price()'.
    
    def display(self): #- Displays the products name, quantity, and price:
        #- I can also get the same results with "__str__(self)", but that
        #-      forces the class to only return a string.
        print("Product Selected: {}".format(self.name))
        print("Product Id: {}".format(self.id))
        print("Quantity being ordered: {}".format(self.quantity))
        print("Total Price: {}".format(self.price))
        print("----")
    
    def summary(self): #- Summary of Product selection:
        print("{} ({}) - ${:.2f}".format(self.name, self.quantity, self.get_total_price()))


class Order: #- Gathers data from all the products ordered in an instance:
    def __init__(self): #- Initializes to id="", and products to an empty list []
        self.id = "" #- The 'id' could represent a date and time a product is 
        #-                  ordered, along with any other info about a number 
        #-                  of products ordered at a given date and time.
        
        self.products = [] #- An empty list to be used:
        
    def add_product(self, p_number): #- Adds the provided product to 'products' list:
        self.products.append(p_number)

    def get_subtotal(self): #- Sums the price or each product and returns it:
        order_subtotal = 0
        for p in self.products:
            #- Using the 'for' loop I am able to save individual values in 'p'
            #-      by looping through the appened list of "self.products".
            #-      The variable 'p' represents the class being appended to 
            #-      self.products and be used like a 'variable.class_function()'
            order_subtotal += p.get_total_price() #- order_subtotal adds the next value in p.get_total_price()
        return order_subtotal #- The current function will be defined by whatever 'order_subtotal' represents:

    def get_tax(self): #- Returns 6.5% times the subtotal:
        return self.get_subtotal() * 0.065
        

    def get_total(self): #- Returns the subtotal plus the tax:
         return self.get_subtotal() + self.get_tax()
    
    def display_receipt(self): #- Displays a recept:
        print("Confirmation Number: {}".format(self.id))

        for product_details in self.products: #- Order Summary:
            product_details.display()

        print("------------------------------------------")
        print("Subtotal: ${:.2f}".format(self.get_subtotal()))
        print("Tax: ${:.2f}".format(self.get_tax()))
        print("Total: ${:.2f}".format(self.get_total()))

    def product_summary(self):
        for new_products in self.products: #- Order Summary:
            new_products.summary()


class Customer: #- This class gathers a customer's details and purchase history to a receipt:
    def __init__(self): #- Initialize id="", name="", and 'orders' list:
        self.id = ""
        self.name = ""
        self.orders = []

    def add_order(self, order_number): #- Adds the provided order to a list of orders called 'self.orders':
        self.orders.append(order_number)

    def get_order_count(self): #- Returns the number of orders made:
        order_number = 0
        for counting in self.orders:
            order_number += 1
        return order_number

    def get_total(self): #- Returns the total price of all orders combined:
        grand_total = 0
        for price in self.orders:
            grand_total += price.get_total()
        return grand_total

    def display_summary(self): #- Displays a short summary of purchases made:
        print("---------- Purchace Summary ----------")
        print("Customer Account Id: {}".format(self.id))
        print("Customer Name: {}".format(self.name))
        print("Number of orders made: {}".format(self.get_order_count()))

        for p_summary in self.orders: #- Order Summary:
            p_summary.product_summary()

        print("Total: ${:.2f}".format(self.get_total()))
        print()

    def display_receipts(self): #- Displays Purchase History:
        print("---------- Customer Details ----------")
        print("Customer Account Id: {}".format(self.id))
        print("Detailed receipts for customer '{}'".format(self.name))
        print("---------- Receipt ----------")

        for single_order in self.orders: #- Displays all the orders created:
            single_order.display_receipt()
            print()


def main():

    #- Customer is logged in:
    c = Customer()
    #- Customer details are obtained:
    c.id = "aa32"
    c.name = "Gandalf"

    #- Customer starts an order:
    order1 = Order()
    order1.id = "1138" #- order id generated

    #- Selecting Products:
    p1 = Product("1238223", "Sword", 1899.99, 10)
    order1.add_product(p1)
    p2 = Product("838ab883", "Shield", 989.75, 6)
    order1.add_product(p2)

    # Customer completes the order
    order1.get_subtotal()

    # The Receipt is printed:
    c.add_order(order1)
    c.display_summary()
    c.display_receipts()

    # Add another product and order and display again
    order2 = Order()
    order2.id = "1277182"
    # Selecting products:
    p3 = Product("2387127", "The Ring", 1000000, 1)
    order2.add_product(p3)
    p4 = Product("1828191", "Wizard Staff", 199.99, 3)
    order2.add_product(p4)

    # Print updated receipt:
    c.add_order(order2)
    c.display_summary()
    c.display_receipts()


if __name__ == "__main__":
    main()