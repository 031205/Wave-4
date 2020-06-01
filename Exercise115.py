def Pig_Latin_translator(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0] in vowels:
        return word + 'way'
    else:
        length = len(word)
        for i in range(0, length):
            if word[i] in vowels:
                break
            else:
                i = i + 1
        firstpart = word[0:i]
        secondpart = word[i:]
        return secondpart + firstpart + 'ay'


