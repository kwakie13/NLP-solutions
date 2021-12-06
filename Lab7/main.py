import spacy

# print("Enter sentence: ")
sentence = "turn down the music player"  # input()

nlp = spacy.load("en_core_web_sm")
doc = nlp(sentence)

# dzielenie na tokeny i oznaczenie części mowy odbywa się w dalszej części, ale jesli jest też wymagane osobno:
# print("Printing tokens and their part of speech")
# for token in doc:
#     print(token.text, token.pos_)

isOrder = True

for token in doc:
    if "subj" in token.dep_:
        if token.head.dep_ == "ROOT":
            isOrder = False
            break

if isOrder:
    action = ""

    for token in doc:
        if token.dep_ == "prt":
            if token.head.dep_ == "ROOT":
                action += token.text + " "
        elif token.dep_ == "ROOT":
            action += token.text + " "

    action_object = []
    children = []

    for token in doc:
        if token.dep_ == "ROOT":
            children = [child for child in token.children]

    for child in children:
        if "obj" in child.dep_:
            action_object.append(child)

    for token in action_object:
        for child in token.children:
            action_object.append(child)

    objects = ""

    for token in doc:
        if token in action_object:
            objects += token.text + " "

    print("akcja: {}, obiekt: {}".format(action[:-1], objects[:-1]))
