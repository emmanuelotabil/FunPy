# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Take user input of comma separated words
words = input("Enter your comma separated words: ")

words.split(",").sort()

# print outcome
print("".join(words))
