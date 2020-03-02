import random
word = ""
letter = ""
updatedspaces = []
def intialize ():
    wordBank = ['keyboard', 'computer', 'mouse', 'application']
    word = random.choice(wordBank)
    updatedspaces = []
    spaces = "___"
    print(spaces), len(word)
    
def getLetter():
    letter = raw_input('Guess a letter ')
    global letter
    letterList = []
    global letterList  
    letterList.append(letter)
    

def checkifWon ():
    if len(letterList) == len(word): 
        print('Good job, you won!')
        
    else:
        getLetter()
            

def main ():
    intialize()
    getLetter()
    checkifWon()

main()

main()
word = ("Anir")
wordList = list(word.lower())
updatedSpaces = []
wordLen = len(word)
lives = 5
letter = " "

for i in range (0, int(wordLen)):
    updatedSpaces.append("_")
    
def getLetter():
    global letter
    letter = raw_input ("Enter a letter guess    ")

def check():
    global updatedSpaces
    global lives
    global letter
    for x in range(0, int(wordLen)):
        if letter == wordList[x]:
            updatedSpaces[x] = wordList[x]
            print(updatedSpaces)
            print("You have:   ", lives, "   lives left!")
            checklist = "".join(updatedSpaces)
            master = "".join(wordList)
            if checklist == master:
                print("Congrats you solved the word!    ")
                #break
            else:
                getLetter()
        else:
            lives -= 1
            if lives != 0:
                print("You have:  " + str(lives) + "  lives left!")
                print(updatedSpaces)
                getLetter()
            else:
                print("Game Over   ")
                
def game():
    getLetter()
    check()
    
game()