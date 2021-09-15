import sys
str=raw_input("Enter String")
char=0
word=1
for i in  str:
    char=char+1
    if(i==''):
        word=word+1
        print("number of words in the given string",word)
        print("number of characters in the given string",char)
        print("number of space in the given string",(word-1))
