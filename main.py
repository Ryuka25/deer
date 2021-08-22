#!/usr/bin/env python

print("""
 ____         __    ____            
|  _ \  ___  / /   / /\ \  ___ _ __ 
| | | |/ _ \/ /   / /  \ \/ _ \ '__|
| |_| |  __/\ \  / /   / /  __/ |   
|____/ \___| \_\/_/   /_/ \___|_|   
                
                - by Ryuka Copyright 2021
""")
print("\tDe</>er allow user to decode or encode string!\n")

alphabet = "abcdefghijklmnopqrstuvwxyz"
key  = 12

def changeKey():
    while True:
        try:
            global key
            key  = int(input("[?] Enter a number of chiffrement : "))
            if (key < 0):
                pass
            else:
                print("[*] Success ... Key number has been changed !")
                break
        except:
            print("[ERROR] Please enter a valid number")

def encodeChar(char):
    
    if (char in alphabet): 
        decodedIndex = alphabet.index(char) 
        encodedIndex = (decodedIndex + key) % 26    

        return alphabet[encodedIndex]
    else:
        return char 

def encodeString():
    encode = True
    while encode:
        encodedString = ""
        print('[?] Please enter the strings you want to encode !')
        decodedString = str(input(' [menu/encoder] > '))
    
        if (decodedString == "99"):
            encode = False
        else:
            for char in decodedString:
                encodedString = encodedString + encodeChar(char)
            print(f'[*] The encoded string is : "{encodedString}"\n')

def decodeChar(char):

    if (char in alphabet):
        encodedIndex = alphabet.index(char)
        decodedIndex = (encodedIndex - key) % 26

        return alphabet[decodedIndex]
    else:
        return char

def decodeString():
    decode = True
    while decode:
        decodedString = ""
        print('[?] Please enter the strings you want to decode !')
        encodedString = str(input(' [menu/decoder] > '))

        if (encodedString == '99'):
            decode = False
        else:
            for char in encodedString:
                decodedString = decodedString + decodeChar(char)
            print(f'[*] The decoded string is : "{decodedString}"\n')

def main():
    run = True
    print('[?] Enter what tools do you want to use from the bellows :\n\n\t1- Encoder\n\t2- Decoder\n\t3- Change the key\n\n\n\t99- Exit\n')
    while run:
        choose = True
        while choose:
            try:
                tool = str(input(' [menu] > '))
                if (tool in {'1','2','3','99'}):
                    break
                else:
                    print('[!] Please choose a valid number !')
                    pass
            except:
                print('[!] Please choose a valid number !')
                pass
        if (tool == '99'):
            run = False
        else:
            print('[!] Input 99 to return to the menu !')
            if (tool == '1'):
                encodeString()
            elif (tool == '3'):
                changeKey()
            elif (tool == '2'):
                decodeString()

if (__name__ == '__main__'):
    main()
