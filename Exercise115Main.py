from Exercise115 import Pig_Latin_translator
text = input('Enter a line of text: ')
b = text.split(" ")
length = len(b)
for num in range(length):
    print(Pig_Latin_translator(b[num]), end=" ")

