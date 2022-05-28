# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from collections import Counter

def read_file_content(filename):

    content = ''

    with open(filename, 'r') as f:
        content += f.read()

    return content


def count_words():

    text = read_file_content("./story.txt")
    
    list_words = text.split(' ')
    list_words = [word.lower() for word in list_words]

    for i in range(len(list_words)):

        new_word = ''

        for j in range(len(list_words[i])):

            if list_words[i][j].isalnum():
                new_word += list_words[i][j]
            else:
                list_words.append(list_words[i][j])

        list_words[i] = new_word

    return dict(Counter(list_words))

print(count_words())