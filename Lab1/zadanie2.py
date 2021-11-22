dot_1 = [natural ** 2 for natural in range(0, 51)]
print(dot_1)

dot_2 = (natural ** 3 for natural in range(20, 31))
for element in dot_2:
    print(element)

dot_3 = (3 * x - 2 for x in range(-5, 6))
for element in dot_3:
    print(element)

dot_4 = ((x, y) for x in range(10, 21) for y in range(5, 11))
for element in dot_4:
    print(element)

dot_5 = [(x, y) for x in range(4, 8) for y in ['jabłko', 'gruszka', 'komputer']]
print(dot_5)
