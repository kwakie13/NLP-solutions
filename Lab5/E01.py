import sys

sys.setrecursionlimit(10000)
dictionary = {}


def MaxMatch(sentence, dictionary_d):
    if len(sentence) == 0:
        return []

    for i in range(len(sentence), 0, -1):
        first_word = sentence[:i]
        remainder = sentence[i:]

        if first_word in dictionary_d:
            return [first_word] + MaxMatch(remainder, dictionary_d)

    # no word was found, so make a one-character word
    first_word = sentence[0]
    remainder = sentence[0:]
    return [first_word] + MaxMatch(remainder, dictionary_d)


with open("PoliMorf-0.6.7.tab", 'r', encoding='utf-8') as imported_dict:
    for line in imported_dict:
        words = line.split("\t")
        word = words[0]
        dictionary[word] = line

print("Enter sentence as one word: ")
sentence = MaxMatch(input(), dictionary)
print("Separated words: ", sentence)
