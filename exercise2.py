# shift lowercase letters to the front and remove spaces

# Take input from the user
user_input = input("Enter a string: ")

# Initialize variables for lowercase and uppercase letters
lowercase_letters = ""
uppercase_letters = ""

# Iterate through each character in the input string
for char in user_input:
    if char.islower():
        lowercase_letters += char
    elif char.isupper():
        uppercase_letters += char

# Combine the lowercase and uppercase letters, ignoring spaces
result_string = lowercase_letters + uppercase_letters

# Print the result
print("Modified String:", result_string)
