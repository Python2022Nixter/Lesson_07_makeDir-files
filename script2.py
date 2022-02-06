import email


CUSTOMERS_FILE = "customers/customers.csv"


# Open the file for reading
with open(CUSTOMERS_FILE, "r") as f:
    file_data = f.read()
    pass

# Convert to list
customer_list1 = file_data.split("\n")


customer_list2 = []
for next_customer in customer_list1:
    customer_list2.append(next_customer.split(";"))

# get email

for cust in customer_list2:
    if cust[1] == "Leia":
        print(cust[3])
        break
    pass