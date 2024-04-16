# Определение алфавита и соответствующих чисел
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
numbers = list(range(33))

# Создание словаря для преобразования каждой буквы в соответствующее число
letter_to_number = dict(zip(alphabet, numbers))

# Создание словаря для преобразования каждого числа в соответствующую букву
number_to_letter = dict(zip(numbers, alphabet))


def encrypt(word, key):
    # Преобразование слова и ключа в числа
    word_numbers = [letter_to_number[letter] for letter in word]
    key_numbers = [letter_to_number[letter] for letter in key]

    # Расширение ключа до длины слова, если ключ короче
    extended_key_numbers = key_numbers + word_numbers
    extended_key_numbers = extended_key_numbers[:len(word)]

    # Шифрование слова
    encrypted_numbers = [(word_number + key_number) % 33 for word_number, key_number in
                         zip(word_numbers, extended_key_numbers)]

    # Преобразование зашифрованных чисел обратно в буквы
    encrypted_word = ''.join(number_to_letter[number] for number in encrypted_numbers)

    return encrypted_word



def decrypt(word, key):
    # Преобразование слова и ключа в числа
    word_numbers = [letter_to_number[letter] for letter in word]
    key_numbers = [letter_to_number[letter] for letter in key]

    # Расшифровка слова
    decrypted_numbers = [(word_number - key_number) % 33 for word_number, key_number in
                         zip(word_numbers, key_numbers)]

    # Преобразование расшифрованных чисел обратно в буквы
    decrypted_word = ''.join(number_to_letter[number] for number in decrypted_numbers)

    # Расширение ключа до длины слова, если ключ короче
    key_numbers = key_numbers + [letter_to_number[letter] for letter in decrypted_word]
    key_numbers = key_numbers[:len(word)]

    return decrypted_word



# Получение слов и ключа от пользователя
word = input("Введите слово: ")
key = input("Введите ключ: ")

# Проверка длины ключа и слова и соответствующие действия
if len(word) > len(key):
    key = key + word[:len(word) - len(key)]

# Шифрование и расшифровка слова
encrypted_word = encrypt(word, key)
decrypted_word = decrypt(encrypted_word, key)

print(f'Оригинальное слово: {word}')
print(f'Зашифрованное слово: {encrypted_word}')
print(f'Расшифрованное слово: {decrypted_word}')
