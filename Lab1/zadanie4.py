f = open("letter.txt", "r", encoding="utf-8")
c = open("censored_letter.txt", "w", encoding="utf-8")

line_number = 0

for line in f:
    line_number += 1

    words = line.split()

    if line_number % 3 == 0:
        words = ['*****']

    censor = False

    for word in words:
        if word.lower().strip(",.") == "kocham":
            censor = True

    if censor:
        words = ['*****']

    c.write(" ".join(words))
    c.write("\n")

f.close()
c.close()
