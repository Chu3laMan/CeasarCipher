alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n");
text = input("Type your message:\n").lower();
shift = int(input("Type the shift number:\n"));

def ceasar(start_text, shift_amount, direction):
    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift);
    else:
        decrypt(decrypted_text=text, shift_amount=shift)


def encrypt(plain_text, shift_amount):
    cipher_text = "";
    for letter in plain_text:
        position = alphabet.index(letter);
        new_position = position + shift_amount;
        new_letter  = alphabet[new_position];
        cipher_text += new_letter;
    print(f"the encoded text is {cipher_text}");

# encrypt(plain_text=text, shift_amount=shift);

def decrypt(decrypted_text, shift_amount):
    decrypted = "";
    for letter in decrypted_text:
        position = alphabet.index(letter);
        new_position = position - shift_amount;
        new_letter = alphabet[new_position];
        decrypted += new_letter;
    print(f"the decrypted text is {decrypted}");

# decrypt(decrypted_text=text, shift_amount=shift);

ceasar(start_text=text, shift_amount=shift, direction=direction);

