alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
initial_text = input("Type your message: ").upper()
shift_number = int(input("Type the shift number: "))

def caesar(start_text, shift, cipher_direction):
    end_text = ""

    if cipher_direction == 'encode':
        shift *= -1

    for char in start_text:

        if char in alphabet:

            position = alphabet.index(char)
            new_position = position + shift
            end_text += alphabet[new_position]
        else:
            end_text += char
    
    print(f"The result is {end_text}")

caesar(start_text=initial_text, shift=shift_number, cipher_direction=direction)

