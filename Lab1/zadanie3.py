POL_ENG_dict = {"chłopak": "boy", "dziewczyna": "girl", "jabłko": "apple", "banan": "banana", "małpa": "monkey",
                "słoń": "elephant", "pies": "dog", "kot": "cat", "żyrafa": "giraffe", "szczur": "rat"}

print("Podaj słowo w języku polskim")
word = str(input())

try:
    print(POL_ENG_dict[word])
except:
    print("W słowniku nie ma takiego słowa")
