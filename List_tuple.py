# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Get user input
values = input("Enter your comma separated values to be converted: ")

# Convert input to list
lst = values.split(",")

# convert list to tuple
tup = tuple(lst)

# Print both list and tuple
print("\n\nYour input converted to list is: ", lst)

print("\n\nYour input converted to list is: ", tup)
