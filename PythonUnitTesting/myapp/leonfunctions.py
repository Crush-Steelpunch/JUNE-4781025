# example function

# def <name>():
#    code to run


# example function

def printhelloworld():
    print("Hello World")

#hellocount = int(input('How many? '))
#for i in range(hellocount):
    #printhelloworld()


# Input parameters


def addfivetoeverything(inputvar):
    print(inputvar + 5)

#anumber = int(input('number in: '))

#addfivetoeverything(anumber)


# returns data 


def reverseaword(inputword):
    lettercount = len(inputword)-1
    reversedword = ''
    for letterindex in range(lettercount,-1,-1):
        reversedword = reversedword + inputword[letterindex]
    return reversedword

#theword = input('Type a word: ')

#returnword = reverseaword(theword)
#print(returnword)



def testfunction1(inputnum):
    if inputnum > 0:
        return "positive"
    else:
        return "negative"


def seenohearno(whatno='evil'):  # example of default argument
    reversedwhat = reverseaword(whatno)  # calling functions in functions
    hearno = "Hear No " + reversedwhat.capitalize()
    seeno = "See No " + whatno.capitalize()
    speakno = "Speak No " + whatno.capitalize()
    return [hearno,seeno,speakno]

#print(seenohearno('bread'))

