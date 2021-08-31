#!/usr/bin/env python

import os

class _programms():

    def __init__(self) -> None:
        self.prompt = "De</>er"
        self.tips = "[?] type help() to display an help interface !"
        self.version = "v0.1"
        self.banner = """
____         __    ____            
|  _ \  ___  / /   / /\ \  ___ _ __ 
| | | |/ _ \/ /   / /  \ \/ _ \ '__|
| |_| |  __/\ \  / /   / /  __/ |   
|____/ \___| \_\/_/   /_/ \___|_|   
                
                - by Ryuka Copyright 2021

\tDe</>er allow user to decode or encode string!
"""
        self.help = """
De</>er allow you to de</>er your string !

[?] Who to use ?
    Type your string after the input prompt
[!] Typing on the following word will return action:
    quit :
        - This will quit the programs
    help :
        - This will display this helps
    version:
        - This will display the programms version
    changeKey: 
        - This will prompt you an interface to changing key
"""

    def showBanner(self):
        print(self.banner)

    def showVersion(self):
        print(self.version)

    def showHelp(self):
        print(self.help)
    
    def showTips(self):
        print(self.tips)

class _deer():

    alphabet =  "abcdefghijklmnopqrstuvwxyz"
        
    def __init__(self, key=12) -> None:
        self.changeKey(key)

    def changeKey(self,key) -> None:
        " Change the key encryption of the current De</>er session "
        if (key == "kha"):
            self.key = "kha"
            self.deerAlphabet = "qbcedrtykuiopnlmafzgjvwxhs"
        else: 
            try:
                int(key)                                                    # Test if the key is a type of int
                print("[*] Key is <class 'int'>")
                self.key = key
                self.deerAlphabet = self.createCodedAlphabet(self.key)      # Create the alphabet correponding to the key
            except:
                print("[!] Key Not Found\nChoosing old key")
        print("[*] New De</>er alphabet initialized.")

    def showKey(self):
        " View the current key "
        print(f"[*] This is the current Key value = '{self.key}'")
        print(f"[*] Normal Alphabet \t: {self.alphabet}")
        print(f"[*] De</>er Alphabet\t: {self.deerAlphabet}")

    def createCodedAlphabet(self, key:int) -> str:
        " Create a De</>er alphabet with a key <class 'int'> "
        result = ""
        for i in range(26):
            originalIndex = i                           # Handle the current index of the alphabet[i]
            deerIndex = (originalIndex + key) % 26      # Handle the new index of the alphabet[i] in the deerAlphabet
            result += self.alphabet[deerIndex]          # Construct the deerAlphabet

        return result

    def deerChar(self,char:str) -> str:
        " De</>erring only a char "
        char = char.lower()                     # Lowering the char to be supported by the codedAlphabet
        result = char                           # Initialize the result in case that char is not in codedAlphabet
        for i in range(26):
            if char == self.deerAlphabet[i]:    # Find the index of the char in the codeAlphabet
                result = self.alphabet[i]       # Result is the correpondant char with the same index in the alphabet
        
        return result

    def deerStr(self,string:str) -> str:
        " De</>erring a string"
        result = "" 
        self.initialString = string
        for char in self.initialString:         # Iterate the string char
            result += self.deerChar(char)       # Construct the deerString by deering char one by one

        self.deeredString =  result

    def showResult(self):
        " Print the current De</>erring"
        print(f'[*] "{self.initialString}" is De</>ered to "{self.deeredString}"\n')

def main():
    deerInterface = _programms()
    dip = deerInterface.prompt

    deerInterface.showBanner()
    deerInterface.showTips()
    
    deer = _deer()

    deer.showKey()

    run = True
    while run:
        userInput = str(input(f"[{dip}] > "))
        if (userInput in ["quit", "exit"]):
            run = False
            print("[!] If you leave , I'll be broken inside ...")
        elif (userInput == "clear"):
            cmd = "clear"
            os.system(cmd)
        elif (userInput == "help"):
            deerInterface.showHelp()
        elif (userInput == "version"):
            deerInterface.showVersion
        elif (userInput == "changeKey"):
            newKey = input(f"[{dip} / changeKey] > ")
            deer.changeKey(newKey)
        elif (userInput == "showKey"):
            deer.showKey()
        else:
            deer.initialString = userInput
            deer.deerStr(userInput)
            deer.showResult()
        pass

if (__name__ == '__main__'):
    main()
