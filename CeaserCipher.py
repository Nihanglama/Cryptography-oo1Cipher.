alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
name=input('Enter your name to Encrypt or Decrypt: ')
shift=int(input("Enter the Shift Value"))


def EncryptCeaser():
    encrypted=''
    for letter in name.upper():
        letters_index=alphabets.index(letter)
        encrypt_letter_index=(letters_index+shift)%26
        encrypted+=alphabets[encrypt_letter_index]
        
    return encrypted

def DecryptCeaser():
    decrypted=''
    for letter in EncryptCeaser():
        letters_index=alphabets.index(letter)
        encrypt_letter_index=(letters_index-shift)%26
        decrypted+=alphabets[encrypt_letter_index]
        

    return decrypted
print(EncryptCeaser())
print(DecryptCeaser())


