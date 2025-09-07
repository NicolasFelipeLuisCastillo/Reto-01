word: str = input("Enter a word: ")


def reverse_word(word):
    # Convert to lowercase to ensure the comparison is case-insensitive
    word = word.lower()
    result: str = ""

    # Reverse the word
    for letter in word:
        result: str = letter + result
        print(letter)
        print(result)
    # Check if the word is a palindrome
    if word == result:
        print(f"The word is a palindrome")
    else:
        print(f"The word is not a palindrome")


reverse_word(word)

# Explanation:

# The user's word is taken and lowercase. It is then inverted using an empty string to display 
# the result. A comparison is made to see if that word is equal to the original.