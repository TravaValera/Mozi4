alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
numbers = list(range(33))


letter_to_number = dict(zip(alphabet, numbers))


number_to_letter = dict(zip(numbers, alphabet))


def encrypt(word, key):

    word_numbers = [letter_to_number[letter] for letter in word]
    key_numbers = [letter_to_number[letter] for letter in key]


    extended_key_numbers = key_numbers + word_numbers
    extended_key_numbers = extended_key_numbers[:len(word)]


    encrypted_numbers = [(word_number + key_number) % 33 for word_number, key_number in
                         zip(word_numbers, extended_key_numbers)]


    encrypted_word = ''.join(number_to_letter[number] for number in encrypted_numbers)

    return encrypted_word



def decrypt(word, key):

    word_numbers = [letter_to_number[letter] for letter in word]
    key_numbers = [letter_to_number[letter] for letter in key]


    decrypted_numbers = [(word_number - key_number) % 33 for word_number, key_number in
                         zip(word_numbers, key_numbers)]


    decrypted_word = ''.join(number_to_letter[number] for number in decrypted_numbers)


    key_numbers = key_numbers + [letter_to_number[letter] for letter in decrypted_word]
    key_numbers = key_numbers[:len(word)]

    return decrypted_word




word = input("Введите слово: ")
key = input("Введите ключ: ")


if len(word) > len(key):
    key = key + word[:len(word) - len(key)]


encrypted_word = encrypt(word, key)
decrypted_word = decrypt(encrypted_word, key)

print(f'Оригинальное слово: {word}')
print(f'Зашифрованное слово: {encrypted_word}')
print(f'Расшифрованное слово: {decrypted_word}')
