def reverse_words(input_str):
    # Split the input string into a list of words using space as the separator
    words = input_str.split(' ')

    # Initialize an empty list to store the reversed words
    reversed_words = []

    # Iterate through each word in the list
    for word in words:
        # Reverse the characters in the word and add it to the reversed_words list
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)

    # Join the reversed words into a single string with spaces in between
    reversed_str = ' '.join(reversed_words)

    return reversed_str


# Test the function with sample input
input_string = "This is an example!"
output_string = reverse_words(input_string)
print(output_string)

input_string = "double  spaces"
output_string = reverse_words(input_string)
print(output_string)

# def reverse_words(str):
#     return ' '.join(s[::-1] for s in str.split(' '))