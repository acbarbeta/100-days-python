alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
initial_text = input("Type your message: ").lower()
shift_number = int(input("Type the shift number: "))

def caesar_decryption(start_text, shift):
    end_text = ""

    for char in start_text:

        if char in alphabet:

            position = alphabet.index(char)
            new_position = position - shift_number
            end_text += alphabet[new_position]

    print(f"The decoded text is {end_text}")

