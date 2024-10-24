
def is_palindrome (stroka):
    cleaned_stroka = ''.join(stroka.split()).lower()
    return cleaned_stroka == cleaned_stroka[::-1]
while True:
    try:
        user_input = input("Введите что хотите, но не цифры: ")
        if not all(c.isalpha() or c.isspace() for c in user_input):
            raise ValueError("Ввод должен содержать только буквы и пробелы.")
        break
    except ValueError as e:
        print(f"Ошибка: {e}")
test = [user_input]
for s in test:
    if is_palindrome(s):
        print(f'"{s}" является палиндромом.')
    else:
        print(f'"{s}" не является палиндромом.')
