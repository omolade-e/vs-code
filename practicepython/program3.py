value = input("Enter your shift value: ")
while not value.isnumeric(): # making sure the shift value is an actual number
    print("Invalid shift value.")
    value = input("Enter your shift value: ")
alphabets1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = input("Enter your message: ")
new_encrypted_message = ""
i = 0
new_index = [] # the new indexes of the shifted characters
for character in message.upper():
    if character in alphabets1:
        move = alphabets1.index(character) + int(value) # changing the characters by the shift value.
        while move >= len(alphabets1):
            move = move - len(alphabets1)
        new_index.append(move)
        new_encrypted_message += alphabets1[move]
    else:
        new_index.append(character) # if the character is a letter, just append it
        new_encrypted_message += character
print(new_encrypted_message)
print("Hint, the shift value is " + str(value) + ".")