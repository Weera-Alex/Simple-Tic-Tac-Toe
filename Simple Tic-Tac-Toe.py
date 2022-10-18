text = "         "

letter = [x for x in text]
text = letter

print("---------")
print(f"""| {text[0]} {text[1]} {text[2]} |
| {text[3]} {text[4]} {text[5]} |
| {text[6]} {text[7]} {text[8]} |""")
print("---------")

counter = 0
counter2 = 0
counter4 = 0
b = 0
a = ""
for x in text:
    if x == "x" or x == "X":
        counter += 1
    elif x == "o" or x == "O":
        counter2 += 1
    elif x == " ":
        counter4 += 1
letter_input = "X"
letter_input2 = "O"
jaja = True
while counter4 != 0:
    if jaja:
        XOXO = letter_input
        jaja = False
    else:
        XOXO = letter_input2
        jaja = True

    new_array = input()
    new_array2 = new_array.replace(" ", "")
    z = False

    d = new_array2 != "11" and new_array2 != "12" and new_array2 != "13" and new_array2 != "21" and new_array2 != "22" and new_array2 != "23" and new_array2 != "31" and new_array2 != "32" and new_array2 != "33"
    if d:
        print("Coordinates should be from 1 to 3!")
    elif not new_array2.isnumeric():
        print("You should enter numbers!")
    elif new_array == "1 1" and text[0] != "O" and text[0] != "X":
        text[0] = XOXO
        z = True
        counter4 -= 1
    elif new_array == "1 2" and text[1] != "O" and text[1] != "X":
        text[1] = XOXO
        z = True
        counter4 -= 1
    elif new_array == "1 3" and text[2] != "O" and text[2] != "X":
        text[2] = XOXO
        z = True
        counter4 -= 1
    elif new_array == "2 1" and text[3] != "O" and text[3] != "X":
        text[3] = XOXO
        z = True
        counter4 -= 1
    elif new_array == "2 2" and text[4] != "O" and text[4] != "X":
        text[4] = XOXO
        z = True
        counter4 -= 1
    elif new_array == "2 3" and text[5] != "O" and text[5] != "X":
        text[5] = XOXO
        z = True
        counter4 -= 1
    elif new_array == "3 1" and text[6] != "O" and text[6] != "X":
        text[6] = XOXO
        z = True
        counter4 -= 1
    elif new_array == "3 2" and text[7] != "O" and text[7] != "X":
        text[7] = XOXO
        z = True
        counter4 -= 1
    elif new_array == "3 3" and text[8] != "O" and text[8] != "X":
        text[8] = XOXO
        z = True
        counter4 -= 1
    else:
        print("This cell is occupied! Choose another one!")

    if z:
        print("---------")
        print(f"""| {text[0]} {text[1]} {text[2]} |
| {text[3]} {text[4]} {text[5]} |
| {text[6]} {text[7]} {text[8]} |""")
        print("---------")

        if text[0] == text[1] and text[0] == text[2] and text[0] != " ":
            a = f"{text[0]} wins"
            b += 1
        if text[3] == text[4] and text[3] == text[5] and text[3] != " ":
            a = f"{text[3]} wins"
            b += 1
        if text[6] == text[7] and text[6] == text[8] and text[6] != " ":
            a = f"{text[6]} wins"
            b += 1
        if text[0] == text[3] and text[0] == text[6] and text[0] != " ":
            a = f"{text[0]} wins"
            b += 1
        if text[1] == text[4] and text[1] == text[7] and text[1] != " ":
            a = f"{text[1]} wins"
            b += 1
        if text[2] == text[5] and text[2] == text[8] and text[2] != " ":
            a = f"{text[2]} wins"
            b += 1
        if text[0] == text[4] and text[0] == text[8] and text[0] != " ":
            a = f"{text[4]} wins"
            b += 1
        if text[6] == text[4] and text[6] == text[2] and text[6] != " ":
            a = f"{text[2]} wins"
            b += 1
        if b == 1:
            print(a)
            break
        elif counter4 == 0:
            print("Draw")