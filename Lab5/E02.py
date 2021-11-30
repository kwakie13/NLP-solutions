import string


def splitting_text_to_list(text):
    split_text = list()
    for letter in text:
        if letter == " ":
            split_text += ['<w>']
        else:
            split_text += letter

    return split_text


def get_subwords(text):
    subwords = list(dict.fromkeys(text))

    return subwords


def get_bigrams(text_list):
    bigrams_list = list()
    for i in range(len(text_list) - 1):  # finding all bigrams
        bigram = text_list[i] + text_list[i + 1]
        list_entry = [bigram, text_list[i], text_list[i + 1], 0]

        if list_entry not in bigrams_list:  # checking for duplicates - we don't want them
            bigrams_list.append(list_entry)

    for i in range(len(text_list) - 1):  # counting occurrences of bigrams
        for bigram_entry in bigrams_list:
            if text_list[i] == bigram_entry[1] and text_list[i + 1] == bigram_entry[2]:
                bigram_entry[3] += 1

    return bigrams_list


def find_most_common(bigrams_list):
    occurrences = 0
    bigram = None
    for element in bigrams_list:
        if element[3] > occurrences:
            occurrences = element[3]
            bigram = element

    return bigram


def algorithm_step(list_element, text_as_list):
    bigram_left = list_element[1]
    bigram_right = list_element[2]

    indexes_to_del = list()

    for i in range(len(text_as_list) - 1):
        if text_as_list[i] == bigram_left and text_as_list[i + 1] == bigram_right:
            text_as_list[i] = list_element[0]  # put bigram in text list
            indexes_to_del.append(i + 1)  # delete spare part of bigram (the right side of it)

    for i in range(len(indexes_to_del)):
        del text_as_list[indexes_to_del[i] - i]  # delete spare ones, but remember about shrinking the list due to deleting

    return text_as_list


print("Program dla przykładu z wykładu\n")

print("Enter text:  Hurry on, Harry, hurry on! ")
input_text = " Hurry on, Harry, hurry on! "  # input()
input_text = input_text.translate(str.maketrans('', '', string.punctuation)).lower()

print("Enter dictionary entries: 11")
entries = 11  # input()

split_text_as_list = splitting_text_to_list(input_text)  # list with separate bigrams
sub_words = get_subwords(split_text_as_list)

while len(sub_words) < entries:
    bigrams = get_bigrams(split_text_as_list)
    most_common_bigram = find_most_common(bigrams)
    sub_words.append(most_common_bigram[0])
    algorithm_step(most_common_bigram, split_text_as_list)

print("\nOutput (subwords dictionary): ", sub_words)
