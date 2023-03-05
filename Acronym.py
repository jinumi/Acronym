# Designed and Developed by Muhammad Umair Yaqub.
# Made in P A K I S T A N

# Prompt the user to enter a string
text = str(input("Enter a String\n"))

# Split the input string into a list of words
text = text.split()

# Initialize an empty string to store the acronym
acronym = ""

# Loop through each word in the list and append the first character to the acronym string
for i in text :
    acronym = acronym + str(i[0]).upper()

# Print the resulting acronym
print(acronym)