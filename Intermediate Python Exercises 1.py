def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

# Test the function
test_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(test_list)

# Print the result
print("Original List:", test_list)
print("List with Unique Elements:", result)



#2
def combine_dictionaries(dict_a, dict_b):
    combined_dict = {}

    # Find keys that are common to both dictionaries
    common_keys = set(dict_a.keys()).intersection(dict_b.keys())

    # Combine values for common keys in the new dictionary
    for key in common_keys:
        combined_dict[key] = dict_a[key] + dict_b[key]
#https://stackoverflow.com/questions/11157704/python-intersection-between-a-list-and-keys-of-a-dictionary

    return combined_dict

# Test the function
dictionary_a = {"apple": 3, "banana": 5, "orange": 2}
dictionary_b = {"banana": 2, "orange": 4, "grape": 1}
result_dictionary = combine_dictionaries(dictionary_a, dictionary_b)

# Print the result
print("Dictionary A:", dictionary_a)
print("Dictionary B:", dictionary_b)
print("Combined Dictionary:", result_dictionary)

#3
def count_letters(sentence):
    letter_count = {}

    # Remove spaces and convert to lowercase
    cleaned_sentence = sentence.replace(" ", "").lower()

    # Count the occurrences of each letter
    for char in cleaned_sentence:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count

# Take input from the user
user_sentence = input("Type a sentence: ")

# Call the function and print the result
result_dict = count_letters(user_sentence)
print("Letter Count in the Sentence:")
for letter, count in result_dict.items():
    print(f"{letter}: {count}")
#4
def get_valid_integer_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            # Try converting input to an integer
            return int(user_input)
        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter a valid whole number.")

# Take 5 integer inputs from the user
total_sum = 0
for i in range(5):
    user_number = get_valid_integer_input(f"Enter number #{i + 1}: ")
    total_sum += user_number

# Print the resulting sum
print("The sum of the entered numbers is:", total_sum)
