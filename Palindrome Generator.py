def Main():
    Palindrome("dog")
def Palindrome (word) :
    pal = ""
    lnumber = len(word) - 1
    for letter in word:
        pal = word[lnumber] + pal + word[lnumber]
        lnumber = lnumber - 1
    print(pal)


Main()