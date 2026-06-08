#============================================================
#product sales system
#Integrative Activity - Programming Fundamentals
#============================================================

#-----------------------------------------------------------
#Definition of VAT and Discount
#-----------------------------------------------------------
VAT = 0.16
DISCOUNT = 0.10

#-----------------------------------------------------------
#Customer and product information
#-----------------------------------------------------------

print("=" * 50)
print("     sistem of product sale - welcome customer")
print("=" * 50)

Name_customer = input("Enter the customer's name: ")
Name_product =  input("Enter the product's name: ")
Price_str =     input("Enter the unit price: ")
Quantity_str =  input("Enter the quantity of pieces: ")

#-----------------------------------------------------------
#Change of variables
#-----------------------------------------------------------

Price = float(Price_str)      # Change str to float
Quantity = int(Quantity_str)  # Change str to int

#-----------------------------------------------------------
#Purchase calculations including VAT and the discount imposed by the SAT
#-----------------------------------------------------------

Subtotal = Price * Quantity             # I multiply the quantity by the price
Amount_discount = Subtotal * DISCOUNT    #I multiply the subtotal by the discount
Total_amount = Subtotal - Amount_discount  # remainder in subtotal for the discount obtained
VAT_amount = Total_amount * VAT          # I multiply the total amount by the VAT to obtain the VAT amount
Total_to_pay = Total_amount + VAT_amount # I add the total amount with the VAT amount to obtain the total to pay

#-----------------------------------------------------------
#Identification of data types with type()
#-----------------------------------------------------------

type_name_customer = type(Name_customer)
type_price = type(Price)
type_quantity = type(Quantity)
type_subtotal = type(Subtotal)
type_vat_constant = type(VAT)

#-----------------------------------------------------------
#PRINTING THE PURCHASE TICKET
#-----------------------------------------------------------

print("\n")
print("=" * 50)
print(" " * 10 +"Purchase ticket")
print("=" * 50)

#-----------------------------------------------------------
#Customer
#-----------------------------------------------------------
print(" " * 12 + f"Customer: {Name_customer}")
print("-" * 50)

#-----------------------------------------------------------
#Product data
#-----------------------------------------------------------

print(f"Name product:     {Name_product}")
print(f"Price product:    ${Price:.2f}")
print(f"Product quantity:  {Quantity} pza")
print("-" * 50)

#-----------------------------------------------------------
#Data types
#-----------------------------------------------------------

print("      IDENTIFIED DATA TYPES:")
print(f"Name customer:  {type_name_customer}")
print(f"Price:          {type_price}")
print(f"Quantity:       {type_quantity}")
print(f"Subtotal:       {type_subtotal}")
print(f"VAT:            {type_vat_constant}")
print("-" * 50)

#-----------------------------------------------------------
#Calculation summary
#-----------------------------------------------------------

print("      Calculation summary:")
print(f"Gross subtotal: ${Subtotal:.2f}")
print(f"Discount:       ${Amount_discount:.2f}")
print(f"Net subtotal:   ${Total_amount:.2f}")
print(f"VAT  (16%):     ${VAT_amount:.2f}")
print("  " + "-" * 30)
print(f"Total to pay:   ${Total_amount:.2f}")
print("=" * 50)
print(f" " * 3 + "!Thank you for your purchase! {}".format(Name_customer))
print("=" * 50)