import re
patterns = ["(k|K)urw", "(P|p)izd", "(P|p)ierd", "(K|k)utas", "(C|c)ip", "(D|d)ziwk", "(J|j)eb", "(D|d)up", "(H|h)uj"]


def censor(imported_line):
    new_line = str()
    split_line = imported_line.split()
    print(split_line)

    for word in split_line:
        found_sth = False

        for pattern in patterns:
            if re.search(pattern, word):
                found_sth = True

        if found_sth:
            new_line += "-----" + " "
        else:
            new_line += word + " "

    return new_line


file = open("file.txt", "r", encoding="utf-8")

new_file_content = ""

for line in file:
    stripped_line = line.strip()
    censored_line = censor(stripped_line)
    new_file_content += censored_line + "\n"

file.close()

file = open("file.txt", "w", encoding="utf-8")
file.write(new_file_content)
file.close()
