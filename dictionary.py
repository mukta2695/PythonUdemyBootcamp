import json
from difflib import get_close_matches

class Eng_Dict(object):
    def load_data(self,file_path):
        self.path=file_path
        file=open(self.path)
        return json.load(file)

    def print_output(self, meaning):
        self.meaning=meaning
        if type(self.meaning) == list:
            for item in self.meaning:
                print(item)
        else:
            print(self.meaning)
        print("\n")
    def translate(self,word,path):
        self.word=word.lower()
        self.file_path=path
        self.data=self.load_data(self.file_path)

        if self.word in self.data:
            print(f"Meaning of the word '{self.word}' is:")
            self.print_output(self.data[self.word])
        elif self.word.title() in self.data:
            print(f"Meaning of the word '{self.word.title()}' is:")
            self.print_output(self.data[self.word.title()])
        elif self.word.upper() in self.data:
            print(f"Meaning of the word '{self.word.upper()}' is:")
            self.print_output(self.data[self.word.upper()])
        else:
            matches=get_close_matches(word,self.data.keys())
            ask="n"
            for match in matches:
                ask=input(f"Do you want to know the meaning of the word '{match}' instead? Enter Y/N:\n ")
                if ask.lower()=="y":
                    print(f"Meaning of the word '{match}' is:")
                    self.print_output(self.data[match])
                    break
            if ask.lower() != "y":
                print("Word not found! Enter a valid word! \n")

if __name__=="__main__":
    engDict=Eng_Dict()
    go_on="y"
    path="dictionary_data.json"
    while(go_on.lower()=="y"):
        search_word = input("Enter the word to know its meaning: \n")
        engDict.translate(search_word,path)
        go_on=input("Would you like to find the meaning for another word? Enter Y/N: \n")
