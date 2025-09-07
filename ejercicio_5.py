words: list = ["amor", "roma", "alerta", "ratela", "python", "java", "perro", "vaja"]


def find_anagrams(words):
    anagrams: list = []

    # Look for the first word
    for previous_word in range(len(words)):

        # Compare it with the rest of the words
        for next_word in range(previous_word + 1, len(words)):

            # Sort the letters of both words and compare them
            if sorted(words[previous_word]) == sorted(words[next_word]):
                if words[previous_word] not in anagrams:
                    anagrams.append(words[previous_word])
                if words[next_word] not in anagrams:
                    anagrams.append(words[next_word])

    print(f"The anagrams are: {anagrams}")


find_anagrams(words)


# Explanation:

# The list of words is taken and each word is compared with the rest by sorting their letters.
# If two words have the same letters, they are anagrams and are added to the list of anagrams, 
# which is then printed.