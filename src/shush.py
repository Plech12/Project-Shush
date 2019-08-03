print("Let's code some messages!")

alphabet = 'abcdefghijklmnopqrstuvwxyz'


Keynumber = int(input("Enter the key :"))

newMessage = ''

message1 = input('Enter the message :')

for letter in message1:
    position = alphabet.find(letter)
    newPosition = (position + Keynumber)
    newCharacter = alphabet[newPosition]
    print('The message is :', newCharacter)
