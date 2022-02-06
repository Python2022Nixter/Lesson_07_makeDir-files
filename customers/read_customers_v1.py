CUSTOMERS_FILE = "customers/customers.csv"


# Open the file for reading
f = open(CUSTOMERS_FILE, "r")
file_data = f.read()
f.close()

print(file_data)