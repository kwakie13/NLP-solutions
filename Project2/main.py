import spacy
import os

nlp = spacy.load("pl_core_news_sm")

programms = {"notatnik": ("notepad.exe", "notepad.exe"), "kalkulator": ("calc.exe", "CalculatorApp.exe"),
             "pogodę": ("msnweather:", "Microsoft.Msn.Weather.exe"), "ustawienia": ("ms-settings:", "SystemSettings.exe"),
             "przeglądarkę": ("chrome.exe", "chrome.exe"), "worda": ("WINWORD.EXE", "WINWORD.EXE"),
             "excela": ("EXCEL.EXE", "EXCEL.EXE")}

documents = {"dokument testowy": "C:/Users/Piotr/Desktop/test.docx"}


def get_essentials(text):
    doc = nlp(text)

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

        return action[:-1], objects[:-1]


while True:
    print("\nPodaj komendę: ", end="")
    command = str(input())

    action, action_object = get_essentials(command)
    print("akcja: {}, obiekt: {}\n".format(action, action_object))

    if len(action) > 0:
        if (action == "uruchom" or action == "zamknij") and len(action_object) > 0:  # programy
            try:
                programms[action_object]
            except:
                print("Nieprawidłowa komenda!")
            else:
                if action == "uruchom":  # uruchamianie programu
                    os.system(str("start " + programms[action_object][0]))
                else:  # zamykanie programu
                    os.system(str("taskkill /f /im " + programms[action_object][1]))

        elif action == "otwórz" and len(action_object) > 0:  # otwieranie dokumentu
            try:
                documents[action_object]
            except:
                print("Nie wiem, co mam otworzyć:/")
            else:
                os.system(str("start " + documents[action_object]))

        elif action == "wyszukaj":  # wyszukiwanie w Google
            information = str()
            for element in command.split()[1:]:
                information += "+" + element

            if len(information) > 0:
                os.system(str("start https://google.com/search?q=" + information))
            else:
                print("Ale co mam wyszukać?:)")

        else:
            print("Mów do mnie po polsku, bo Cię nie rozumiem :(")

    else:
        print("Nieprawidłowa komenda!")
