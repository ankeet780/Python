import datetime

# This is a function to display the current furniture items in the store
def Display_furniture_list(furniture_list):
    '''
This function is designed to display a list of furniture items in a tabular format, with clear headers and divider,
making it easy to read and understand the information about each furniture item in the list. Each item is displayed
with its ID, Manufacturer, Product name, Quantity, and Price.
   '''

    print("\nAvailable Furniture:")
    print("ID | Manufacturer | Product | Quantity | Price")
    print("-" * 50)
    for furniture in furniture_list:
        print(str(furniture[0]) + " | " + furniture[1] + " | " + furniture[2] + " | " + str(furniture[3]) + " | $" + str(furniture[4]))
        print("-" * 50)


# This is a function to update the furniture list after a transaction
# It will increase or decrease stock quantity 
def update_furniture_list(furniture_list, furniture_id, quantity, is_purchase):
    '''
The purpose of the update_furniture_list function is to handle the furniture store's inventory by adjusting the quantity
of a particular item in stock depending on whether it is a purchase or a sale. A list of furniture items, the specific
item's ID, the quantity to change, and a boolean to determine if it is a purchase are required for the update process.
The function iterates over the furniture list to locate the item that has the same ID. If the item is discovered during
a purchase operation, the stock quantity will be incremented by the specified amount. It verifies whether there is
sufficient stock to complete the sale; otherwise, it provides an error message. If there is sufficient inventory,
it will reduce the amount appropriately. If successful, the function will return the updated furniture item; otherwise,
it will return None if there is not enough stock or an invalid ID.
   '''
    for furniture in furniture_list:
        if furniture[0] == str(furniture_id): #This is used to match the furniture ID
            if is_purchase:
                furniture[3] += quantity  #  It will increase stock if company  purchase item from manufacturer
            else:
                if quantity >= furniture[3]:
                    print("Not enough stock for " + furniture[2] + ". Available: " + str(furniture[3]))
                    return None #  it will return None if there isn't enough stock
                furniture[3] -= quantity  #  It will decrease stock if company sell item to customer
            return furniture #  it will return updated furniture details
    print("Furniture with ID " + str(furniture_id) + " not found.")
    return None #  it will return None if the furniture ID doesn't exist


# Function to validate number input from the user
def get_valid_number(choice):
    '''
 The get_valid_number function ensures the user inputs a valid integer by continuously asking for input until an integer is given.
 In case of invalid input like a string or a non-integer number, the function detects the error, notifies the user of the issue,
 and asks for input once more. When a legitimate integer is inputted, the function will give back that integer, making sure that
 the program gets the appropriate input type for additional operations.
   '''
    while True:
        try:
            value = int(input(choice)) #it convert input into integer
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.") #it will be display if input is not an integer


# Function to validate float input from the user
def get_valid_float(choice):
    '''
   The get_valid_float function ensures that the user provides a valid floating-point number by continuously prompting for input
   until a valid number is entered. If the user provides invalid input that cannot be converted to a float, the function catches
   the resulting error, informs the user of the mistake, and prompts them again. Once a valid floating-point number is entered,
   the function returns this number, ensuring the program receives the correct type of input for further calculations or processing.
   '''
    while True:
        try:
            value = float(input(choice)) # it convert input into integer
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.") # it will be display if input is not a float

def generate_invoice(transaction_type, person_name, items, shipping_cost=0, total_price=0):
    '''
    The generate_invoice function is responsible for creating a detailed invoice for a transaction.
    It generates a unique filename for the invoice based on the current date and time, initializes
    necessary variables to track costs, and prepares to build the content of the invoice.
    The function will continue by adding transaction details to the invoice_lines list,
    calculating totals, and eventually writing the invoice to the specified text file.
    '''
    now = datetime.datetime.now()  # Get the current date and time
    invoice_file = "invoice_" + transaction_type + "_" + now.strftime('%Y%m%d_%H%M%S') + ".txt"  # Unique invoice file name
    
    total_cost = 0  # Initialize the total cost variable
    invoice_lines = []  # Initialize a list to store invoice lines for printing

    # Add header details to the invoice
    invoice_lines.append("Transaction Type:" + transaction_type.capitalize())
    invoice_lines.append("Name: " + person_name)
    invoice_lines.append("Date & Time: " + now.strftime('%Y-%m-%d %H:%M:%S'))
    invoice_lines.append("\n")
    invoice_lines.append("ID | Manufacturer | Product | Quantity | Unit Price | total")
    invoice_lines.append("-" * 60)

    for item in items:
        total = item['quantity'] * item['price']  # Calculate the total for each item (quantity * unit price)
        total_cost += total  # Add the total to the total cost
        invoice_lines.append(str(item['id']) + " | " + item['manufacturer'] + " | " + item['product'] + " | " + str(item['quantity']) + " | $" + str(item['price']) + " | $" + str(total))

    invoice_lines.append("-" * 60)
    vat = total_cost * 0.13  # Calculate the VAT (13% of the total cost)
    total_with_vat = total_cost + vat  # Add the VAT to the total cost
    total_with_shipping = total_with_vat + shipping_cost  # Add the shipping cost to the total

    # Add totals to the invoice
    invoice_lines.append("Total (Before VAT): $" + str(total_cost))
    invoice_lines.append("VAT (13%): $" + str(vat))
    invoice_lines.append("Total (After VAT): $" + str(total_with_vat))
    invoice_lines.append("Shipping Cost: $" + str(shipping_cost))
    invoice_lines.append("Total Amount: $" + str(total_with_shipping))

    # Write the invoice to the file
    with open(invoice_file, 'w') as file:
            file.write("\t \t \t   BRJ Furniture  \t\t\tShop Bill No:\n ") 
            file.write("\t \t Durbarmarg, Kathmandu | Phone No: 9809757002\n ")
            for line in invoice_lines:
             file.write(line + "\n")  # Write each line to the file

    # Print the invoice to the console
    print("\t \t \t   BRJ Furniture  \t\t\tShop Bill No:\n ") 
    print("\t \t Durbarmarg, Kathmandu | Phone No: 9809757002\n ")
    print("\n--- Invoice ---")
    for line in invoice_lines:
        print(line)  # Print each line to the console

    print("Invoice generated: " + invoice_file)  # Notify the user that the invoice was generated
    return invoice_file  # Return the invoice file name

def manage_purchase(furniture_list):
    '''
   The manage_purchase function is responsible for facilitating the purchase of furniture items from a manufacturer.
   It prompts the user for the employee’s name, initializes variables to track the purchased items and total price,
   and then proceeds to handle the details of the purchase. The function will continue by allowing the user to
   input details about the furniture being purchased, update the inventory, and eventually generate an invoice for the purchase.
   This function ensures that the purchase process is organized, documented, and reflected in the store's inventory and financial records.
   '''
    print("\n--- Purchase Furniture From manufacture ---")
    # Input validation employee's name
    while True:
        try:
            employee_name = input("Enter the Employee's name: ")
            if employee_name.isdigit():  # Check if the input is a number
                 print("Employee's name cannot be a number. Please enter a valid name.")
                 continue
            break
        except ValueError:
            print("Employee's name cannot be a number. Please enter a valid name.")
    
    purchased_items = []
    total_price = 0
    while True:
        while True:
            try:
                furniture_id = int(input("Enter the furniture ID to purchase: "))
                if furniture_id < 1 or furniture_id > len(furniture_list):
                    print("This error in furniture Id is invalid.You must Enter (1 to 6)")
                    continue
                break
            except ValueError:
                print("Your input is invalid. please enter your furniture id.")
                continue
        while True:
            try:
                quantity = int(input("Enter the quantity to purchase: "))
                if quantity <= 0:
                    print("your quantity is must be positive.")
                    continue
                break
            except ValueError:
                print("your input is invalid.Enter a number.")
                continue
        updated_furniture = update_furniture_list(furniture_list, furniture_id, quantity, is_purchase=True)
        if updated_furniture:
            purchased_items.append({'id': updated_furniture[0], 'manufacturer': updated_furniture[1], 'product': updated_furniture[2], 'quantity': quantity, 'price': updated_furniture[4]})
            total_price += updated_furniture[4] * quantity

        more_purchase = input("Do you want to purchase more? (yes/no): ").strip().lower()
        if more_purchase != 'yes':
            break

    if purchased_items:
        generate_invoice('purchase', employee_name, purchased_items, total_price)  # generate a invoice if update is successful


def manage_sale(furniture_list):
    '''
The manage_sale function is designed to manage the entire process of selling furniture to a customer.
It collects the customer's name, tracks items being sold, calculates the total sale price, and ensures
the sale is properly documented and invoiced. This function helps streamline the sales process, maintain
accurate inventory records, and provide a clear record of transactions for both the business and the customer.
   '''
    print("\n--- Sell Furniture To Customer ---")
    # Input validation for customer's name
    while True:
        try:
            customer_name = input("Enter the customer's name: ")
            if customer_name.isdigit():  # Check if the input is a number
                 print("Customer's name cannot be a number. Please enter a valid name.")
                 continue
            break
        except ValueError:
            print("Customer'sname cannot be a number. Please enter a valid name.")
    items_to_sell = []  # empty list to keep track of items being sold
    total_price = 0
    while True:
        while True:
            try:
                furniture_id = int(input("Enter the furniture ID to sell: "))
                if furniture_id < 1 or furniture_id > len(furniture_list):
                    print("This error in furniture Id is invalid.You must Enter (1 to 6)")
                    continue
                break
            except ValueError:
                print("Your input is invalid. Please enter your furniture id.")
                continue
        while True:
            try:
                quantity = int(input("Enter the quantity to sell: "))
                if quantity <= 0:
                    print("Your input must be positive.")
                    continue
                if quantity > int(furniture_list[furniture_id-1][3]):
                    print("out of stock you can sell only avialable quantity :")
                    continue
                break
            except ValueError:
                print("Your input is invalid enter in no formate.")
                continue

        updated_furniture = update_furniture_list(furniture_list, furniture_id, quantity, is_purchase=False)
        if updated_furniture:
            items_to_sell.append({'id': updated_furniture[0], 'manufacturer': updated_furniture[1], 'product': updated_furniture[2], 'quantity': quantity, 'price': updated_furniture[4]})
            total_price += updated_furniture[4] * quantity

        more_sale = input("Do you want to sell more furniture? (yes/no): ").strip().lower()
        if more_sale != 'yes':
            break

    if items_to_sell:
        shipping_cost = get_valid_number("Enter the shipping cost: ")
        generate_invoice('sale', customer_name, items_to_sell, shipping_cost, total_price)  # generate a invoice if update is successful
