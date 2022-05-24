# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import collections


def read_file_content(filename):
    # [assignment] Add your code here 
    f = open(filename, "r")
    file_contents = f.read()
    f.close()
    return file_contents


def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    contents_as_list = text.split()
    occurance_count = collections.Counter(contents_as_list)

    return occurance_count


dic = count_words()
print(dic)
