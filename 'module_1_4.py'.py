my_string = input("Введите произвольный текст: ")

print("Количество символов введённого текста:", len(my_string))
print("Текст в верхнем регистре:", my_string.upper())
print("Текст в нижнем регистре:", my_string.lower())
no_spaces_string = my_string.replace(" ", "")
print("Текст без пробелов:", no_spaces_string)
print("Первый символ строки:", my_string[0] if my_string else "Строка пустая")
print("Последний символ строки:", my_string[-1] if my_string else "Строка пустая")