class PorterAlgorithmStemmer:
    def isConsonant(self, word, i):
        if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u' or (word[i] == 'y' and i - 1 >= 0 and self.isConsonant(word, i - 1)):
            return False
        else:
            return True

    def isVowel(self, word, i):
        return not (self.isConsonant(word, i))

    def containsVowel(self, word):
        for i in range(len(word)):
            if not self.isConsonant(word, i):
                return True
        return False

    def doubleConsonantEnd(self, word):
        if len(word) >= 2 and self.isConsonant(word, -1) and self.isConsonant(word, -2):
            return True
        else:
            return False

    def getForms(self, word):
        form = []
        form_string = ''
        for i in range(len(word)):
            if self.isConsonant(word, i):
                if i > 0 and form[-1] != 'C':
                    form.append('C')
                else:
                    form.append('C')
            else:
                if i > 0 and form[-1] != 'V':
                    form.append('V')
                else:
                    form.append('V')

        for j in form:
            form_string += j

        return form_string

    def getM(self, word):
        form = self.getForms(word)
        m = form.count('VC')

        return m

    def cvcEnding(self, word):
        if len(word) >= 3 and (self.isConsonant(word, -3) and self.isVowel(word, -2) and self.isConsonant(word, -1)) and (word[-1] != 'w' and word[-1] != 'x' and word[-1] != 'y'):
            return True

        return False

    def replace(self, original_word, to_remove, replacement, argument):
        if argument is None:
            return original_word[:original_word.rfind(to_remove)] + replacement
        elif argument == 0 and self.getM(original_word[:original_word.rfind(to_remove)]) > 0:  # M > 0
            return original_word[:original_word.rfind(to_remove)] + replacement
        elif argument == 1 and self.getM(original_word[:original_word.rfind(to_remove)]) > 1:  # M > 1
            return original_word[:original_word.rfind(to_remove)] + replacement

        return original_word

    def step1a(self, word):
        if word.endswith('sses'):
            word = self.replace(word, 'sses', 'ss', None)
        elif word.endswith('ies'):
            word = self.replace(word, 'ies', 'i', None)
        elif word.endswith('ss'):
            word = self.replace(word, 'ss', 'ss', None)
        elif word.endswith('s'):
            word = self.replace(word, 's', '', None)

        return word

    def step1b(self, word):
        flag = False

        if word.endswith('eed'):
            base = word[:word.rfind('eed')]
            if self.getM(base) > 0:
                word = base
                word += 'ee'
        elif word.endswith('ed'):
            base = word[:word.rfind('ed')]
            if self.containsVowel(base):
                word = base
                flag = True
        elif word.endswith('ing'):
            base = word[:word.rfind('ing')]
            if self.containsVowel(base):
                word = base
                flag = True

        if flag:
            if word.endswith('at') or word.endswith('bl') or word.endswith('iz'):
                word += 'e'
            elif self.doubleConsonantEnd(word) and not word.endswith('l') and not word.endswith('s') and not word.endswith('z'):
                word = word[:-1]
            elif self.getM(word) == 1 and self.cvcEnding(word):
                word += 'e'

        return word

    def step1c(self, word):
        if word.endswith('y'):
            base = word[:word.rfind('y')]
            if self.containsVowel(base):
                word = base
                word += 'i'

        return word

    def step2(self, word):
        if word.endswith('ational'):
            word = self.replace(word, 'ational', 'ate', 0)
        elif word.endswith('tional'):
            word = self.replace(word, 'tional', 'tion', 0)
        elif word.endswith('enci'):
            word = self.replace(word, 'enci', 'ence', 0)
        elif word.endswith('anci'):
            word = self.replace(word, 'anci', 'ance', 0)
        elif word.endswith('izer'):
            word = self.replace(word, 'izer', 'ize', 0)
        elif word.endswith('abli'):
            word = self.replace(word, 'abli', 'able', 0)
        elif word.endswith('alli'):
            word = self.replace(word, 'alli', 'al', 0)
        elif word.endswith('entli'):
            word = self.replace(word, 'entli', 'ent', 0)
        elif word.endswith('eli'):
            word = self.replace(word, 'eli', 'e', 0)
        elif word.endswith('ousli'):
            word = self.replace(word, 'ousli', 'ous', 0)
        elif word.endswith('ization'):
            word = self.replace(word, 'ization', 'ize', 0)
        elif word.endswith('ation'):
            word = self.replace(word, 'ation', 'ate', 0)
        elif word.endswith('ator'):
            word = self.replace(word, 'ator', 'ate', 0)
        elif word.endswith('alism'):
            word = self.replace(word, 'alism', 'al', 0)
        elif word.endswith('iveness'):
            word = self.replace(word, 'iveness', 'ive', 0)
        elif word.endswith('fulness'):
            word = self.replace(word, 'fulness', 'ful', 0)
        elif word.endswith('ousness'):
            word = self.replace(word, 'ousness', 'ous', 0)
        elif word.endswith('aliti'):
            word = self.replace(word, 'aliti', 'al', 0)
        elif word.endswith('iviti'):
            word = self.replace(word, 'iviti', 'ive', 0)
        elif word.endswith('biliti'):
            word = self.replace(word, 'biliti', 'ble', 0)

        return word

    def step3(self, word):
        if word.endswith('icate'):
            word = self.replace(word, 'icate', 'ic', 0)
        elif word.endswith('ative'):
            word = self.replace(word, 'ative', '', 0)
        elif word.endswith('alize'):
            word = self.replace(word, 'alize', 'al', 0)
        elif word.endswith('iciti'):
            word = self.replace(word, 'iciti', 'ic', 0)
        elif word.endswith('ful'):
            word = self.replace(word, 'ful', '', 0)
        elif word.endswith('ness'):
            word = self.replace(word, 'ness', '', 0)

        return word

    def step4(self, word):
        if word.endswith('al'):
            word = self.replace(word, 'al', '', 1)
        elif word.endswith('ance'):
            word = self.replace(word, 'ance', '', 1)
        elif word.endswith('ence'):
            word = self.replace(word, 'ence', '', 1)
        elif word.endswith('er'):
            word = self.replace(word, 'er', '', 1)
        elif word.endswith('ic'):
            word = self.replace(word, 'ic', '', 1)
        elif word.endswith('able'):
            word = self.replace(word, 'able', '', 1)
        elif word.endswith('ible'):
            word = self.replace(word, 'ible', '', 1)
        elif word.endswith('ant'):
            word = self.replace(word, 'ant', '', 1)
        elif word.endswith('ement'):
            word = self.replace(word, 'ement', '', 1)
        elif word.endswith('ment'):
            word = self.replace(word, 'ment', '', 1)
        elif word.endswith('ent'):
            word = self.replace(word, 'ent', '', 1)
        elif word.endswith('ou'):
            word = self.replace(word, 'ou', '', 1)
        elif word.endswith('ism'):
            word = self.replace(word, 'ism', '', 1)
        elif word.endswith('ate'):
            word = self.replace(word, 'ate', '', 1)
        elif word.endswith('iti'):
            word = self.replace(word, 'iti', '', 1)
        elif word.endswith('ous'):
            word = self.replace(word, 'ous', '', 1)
        elif word.endswith('ive'):
            word = self.replace(word, 'ive', '', 1)
        elif word.endswith('ize'):
            word = self.replace(word, 'ize', '', 1)
        elif word.endswith('ion'):
            base = word[:word.rfind('ion')]

            if self.getM(base) > 1 and (base.endswith('s') or base.endswith('t')):
                word = base

            word = self.replace(word, '', '', 1)

        return word

    def step5a(self, word):
        if word.endswith('e'):
            base = word[:-1]
            if self.getM(base) > 1:
                word = base
            elif self.getM(base) == 1 and not self.cvcEnding(base):
                word = base

        return word

    def step5b(self, word):
        if self.getM(word) > 1 and self.doubleConsonantEnd(word) and word.endswith('l'):
            word = word[:-1]

        return word

    def stemming(self, start_word):
        word = self.step1a(start_word)
        word = self.step1b(word)
        word = self.step1c(word)
        word = self.step2(word)
        word = self.step3(word)
        word = self.step4(word)
        word = self.step5a(word)
        word = self.step5b(word)

        return word


print("Welcome to Porter algorithm stemming programme.")
print("Keep writing input (words). If you want to exit, write 'Exit'.")
stemmer_object = PorterAlgorithmStemmer()

while True:
    word_input = input("Enter word: ")

    if word_input.lower() == "exit":
        break

    print("Stemmed word: " + stemmer_object.stemming(word_input))
