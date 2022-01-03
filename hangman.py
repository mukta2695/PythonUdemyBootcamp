import random

class Hangman(object):
    def welcome(self):
        name=input("Hello! Enter your name: \n")
        print(f"Hello, {name}! Let's play Hangman!")
        print("_________________________________________")

    def print_rules(self):
        print("RULES:")
        print("_________________________________________")
        print("1. You need to the guess the secret word by guessing a letter every round")
        print("2. You have 10 lives in total. You will lose one life everytime you guess a wrong letter.")
        print("3. If you guess the word within the 10 lives, you win! Else, if you lose all the 10 lives, you will be hanged, and you lose the game!")
        print("GOODLUCK!")

    def generate_word(self,path):
        self.path=path
        file=open(self.path)
        word_list=[]
        for word in file:
            word_list.append(word.split())
        self.random_word=random.choice(word_list)[0]
        return self.random_word.upper()

    def hm(self,path):
        self.word=self.generate_word(path)

        #Uncomment for testing purpose
        #print(self.word)

        self.lives=10
        self.validletters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.guessed=''

        while len(self.word)>0:
            self.main_word=''

            for letter in self.word:
                if letter in self.guessed:
                    self.main_word = self.main_word + letter
                else:
                    self.main_word = self.main_word + "_" + " "
            print(self.main_word)
            if self.main_word == self.word:
                print(f"The secret word is {self.main_word}")
                print("You Win!")
                break

            self.user_input = input("Input a letter: \n")

            if self.user_input.upper() not in self.validletters:
                print("Invalid letter!\n")
                self.user_input = input("Input a letter: \n")
            else:
                self.guessed=self.guessed+self.user_input.upper()

            if self.user_input.upper() not in self.word:
                self.lives -= 1
                print(f"{self.lives} turns left")
                if self.lives == 9:
                    print("  --------  ")
                if self.lives == 8:
                    print("  --------  ")
                    print("     O      ")
                if self.lives == 7:
                    print("  --------  ")
                    print("     O      ")
                    print("     |      ")
                if self.lives == 6:
                    print("  --------  ")
                    print("     O      ")
                    print("     |      ")
                    print("    /       ")
                if self.lives == 5:
                    print("  --------  ")
                    print("     O      ")
                    print("     |      ")
                    print("    / \     ")
                if self.lives == 4:
                    print("  --------  ")
                    print("   \ O      ")
                    print("     |      ")
                    print("    / \     ")
                if self.lives == 3:
                    print("  --------  ")
                    print("   \ O /    ")
                    print("     |      ")
                    print("    / \     ")
                if self.lives == 2:
                    print("  --------  ")
                    print("   \ O /|   ")
                    print("     |      ")
                    print("    / \     ")
                if self.lives == 1:
                    print("You have one last life remaining! Make sure you guess the correct letter")
                    print("  --------  ")
                    print("   \ O_|/   ")
                    print("     |      ")
                    print("    / \     ")
                if self.lives == 0:
                    print("Bummer! You lost!")
                    print("You are now dead!")
                    print("  --------  ")
                    print("     |        ")
                    print("    *_*     ")
                    print("    /|\      ")
                    print("    / \     ")

                    print(f"The secret word was {self.word}")

                    break
if __name__=="__main__":
    hangman=Hangman()
    hangman.welcome()
    hangman.print_rules()
    path="words.txt"
    play_again="y"
    while play_again.lower()=="y":
        hangman.hm(path)
        play_again=input("Do you want to play again? Enter Y/N: \n")
