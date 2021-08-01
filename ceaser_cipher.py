alphanum = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
            'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
            'z': 25}


def encipher(alpha,kw):
    ciphertext = str()
    for word in alpha:
        num = alphanum[word]
        num += kw
        for newword,value in alphanum.items():
            if num == value:
                ciphertext+=newword
    print(ciphertext.upper())


def decipher(alpha,kw):
    ciphertext = str()
    for word in alpha:
        num = alphanum[word]
        num -= kw
        for newword,value in alphanum.items():
            if num == value:
                ciphertext+=newword
    print(ciphertext.upper())


what = input("do you want to encipher or decipher, enter 1 for encipher , anykey for decipher:")

if what  == '1':
    en_word = (input("Enter a word to be enciphered: ").lower()).strip(" ")
    offset = input("Enter offset value(default =3,ceaser):")
    if offset =='':
        offset = 3
    encipher(en_word,int(offset))
else:
    dechiper = (input("Enter a word to be de-ciphered: ").lower()).strip(" ")
    offset = int(input("Enter offset value(default =3,ceaser):"))
    if offset =='':
        offset = 3
    decipher(dechiper,offset)



#make ceaser KW
#test