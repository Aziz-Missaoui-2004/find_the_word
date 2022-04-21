import random, sys, os

class Game():

    def __init__(self):
        self.name = "Find the Word"
        self.chosenWord = random.choice(list(set(map(lambda x: x.replace("\n", ""), open("words.txt").readlines()))))
        self.hiddenWord = list(self.chosenWord)
        self.hiddenLetters = self.hideWord()
        self.chances = 5
        self.helps = 2
        self.message = "enter a letter (one letter required): "

    def __repr__(self) -> str:
        return self.name

    def printHeader(self,):
        os.system('cls')
        sys.stdout.flush() 
        print("     chances: ", self.chances)
        print("     helps (type 'help' to get a help): ", self.helps)
        print("     the word: ", end="")
        self.printWord()
        print()
        if self.PlayerWon():
            print("congrats !! \n\n")
            quit()
        elif self.PlayerLost():
            print(f"you lost : {self.chosenWord}\n\n")
            quit()
        self.letter = self.getLetter()
        

    def hideWord(self):
        hiddenLetters = []
        for i in range(len(self.chosenWord) - 1):
            h = random.randint(0, len(self.chosenWord)-1) ; hiddenLetters.append(h)
        return list(set(hiddenLetters))

    def printWord(self):
        for i in self.hiddenLetters: 
            self.hiddenWord[i] = "_"
        print("".join(self.hiddenWord))
        
    def getLetter(self):
        return input(self.message)
        

    def CorrectLetter(self) :
        for i in self.hiddenLetters:
            if self.chosenWord[i] == self.letter and self.hiddenWord[i] == "_":
                return True
        return False
    
    def updateWord(self):
        for i in self.hiddenLetters:
            if self.chosenWord[i] == self.letter:
                self.hiddenLetters.remove(i)
                self.hiddenWord[i] = self.letter

    def updateChances(self):
        self.chances -= 1
    
    def updateHelps(self):
        self.helps -= 1
    
    def giveHelp(self):
        self.letter = self.chosenWord[random.choice(self.hiddenLetters)]
        self.helps -= 1

    def PlayerWon(self):
        return self.hiddenLetters == []

    def PlayerLost(self):
        return self.chances == 0 

        
#                --------------- Run Program -----------------


__Game__ = Game()
__Game__.printWord()

while True :
    __Game__.printHeader()
    
    if __Game__.letter == 'help' :
        if __Game__.helps > 0:
            __Game__.giveHelp()
        else:
            __Game__.message = "no more helps try again: "
            continue

    if __Game__.CorrectLetter():
        __Game__.updateWord()
    
    else:
        __Game__.updateChances()
        __Game__.message = 'incorrect , try again: '
        
    if __Game__.PlayerWon():
        __Game__.printHeader()
        break
    
        