# Напишите программу, удаляющую из текста все слова, содержащие "абв"

text = input('Введите искомые символы: ')
with open('text2.txt', 'r', encoding = 'utf_8') as file:
    # list = [i for i in file.read().split() if text not in i]
    list = list(filter(lambda x: text not in x, file.read().split()))

print (list)