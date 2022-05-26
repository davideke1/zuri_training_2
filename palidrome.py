# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

st = input("enter the word --> ")


def find_anagrams(word):
    # [assignment] Add your code here
    reversed_word = ""
    for i in word:
        reversed_word = i + reversed_word
    if reversed_word == word:
        return True
    else:
        return False


print(find_anagrams(st))
