alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
name=input('Enter your name to Encrypt or Decrypt: ')
key=[[17,17,5]
    ,[21,18,21]
    ,[2,2,19]]
num_name=[]
for letters in name:
    num_name.append(alphabets.index(letters))



