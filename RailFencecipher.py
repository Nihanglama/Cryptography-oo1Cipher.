
def encrpted()


if __name__ == "__main__":
    alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    name=input('Enter your name to Encrypt or Decrypt: ')
    depth=int(input("Enter the depth"))
    if len(key)!=len(name):
        print("key length should be equal to length of name.")
    else:
        encrypted_name=encrypt(key,name,alphabets)
        print(encrypted_name)
        print(decrypt(key,encrypted_name,alphabets))