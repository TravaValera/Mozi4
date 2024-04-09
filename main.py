# Определение алфавита и соответствующих чисел
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
numbers = list(range(33))

# Создание словаря для преобразования каждой буквы в соответствующее число
letter_to_number = dict(zip(alphabet, numbers))

# Создание словаря для преобразования каждого числа в соответствующую букву
number_to_letter = dict(zip(numbers, alphabet))

# Определение ключа
key = 'сон'

# Преобразование ключа в числа
key_numbers = [letter_to_number[letter] for letter in key]


def encrypt(word):
    # Преобразование слова в числа
    word_numbers = [letter_to_number[letter] for letter in word]

    # Расширение ключа до длины слова
    extended_key_numbers = key_numbers * (len(word) // len(key_numbers)) + key_numbers[:len(word) % len(key_numbers)]

    # Шифрование слова
    encrypted_numbers = [(word_number + key_number) % 33 for word_number, key_number in
                         zip(word_numbers, extended_key_numbers)]

    # Преобразование зашифрованных чисел обратно в буквы
    encrypted_word = ''.join(number_to_letter[number] for number in encrypted_numbers)

    return encrypted_word


def decrypt(word):
    # Преобразование слова в числа
    word_numbers = [letter_to_number[letter] for letter in word]

    # Расширение ключа до длины слова
    extended_key_numbers = key_numbers * (len(word) // len(key_numbers)) + key_numbers[:len(word) % len(key_numbers)]

    # Расшифровка слова
    decrypted_numbers = [(word_number - key_number) % 33 for word_number, key_number in
                         zip(word_numbers, extended_key_numbers)]

    # Преобразование расшифрованных чисел обратно в буквы
    decrypted_word = ''.join(number_to_letter[number] for number in decrypted_numbers)

    return decrypted_word


# Тестирование функций
word = 'материя'
encrypted_word = encrypt(word)
decrypted_word = decrypt(encrypted_word)

print(f'Оригинальное слово: {word}')
print(f'Зашифрованное слово: {encrypted_word}')
print(f'Расшифрованное слово: {decrypted_word}')

