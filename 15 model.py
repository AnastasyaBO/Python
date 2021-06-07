#Шифр Цезаря
alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
number = int(input("Введите чисто сдвига"))
summary = ''

def cesar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUp:
        return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
    else:
        return char


with open('filename.txt', encoding='utf8') as myfile:
    for line in myfile:
        for char in line:
            summary += cesar(char)

with open("output.txt", "w", encoding="utf8") as myfile:
    myfile.write(summary)

