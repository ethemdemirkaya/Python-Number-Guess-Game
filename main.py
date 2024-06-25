from random import randint


class gueesGame:
    def __init__(self):
        self.computerNumber = randint(1, 100)
        self.myNumber = 0
        self.TryTimes = 0

    def startGame(self):
        print("------------- Welcome number guess game --------------")
        print("A number between 1 and 100 will be selected for you, and you will be asked to guess it.")

    def playGame(self):
        while self.myNumber != self.computerNumber:
            self.myNumber = int(input("Enter your guess: "))
            if self.myNumber > self.computerNumber:
                print("Enter a lower number")
            elif self.myNumber < self.computerNumber:
                print("Enter a higher number")
            self.TryTimes += 1
        print(f'You guessed the correct number in {self.TryTimes} attempts. Number is {self.computerNumber}')


game1 = gueesGame()
game1.startGame()
game1.playGame()
