import random
class DiceSim(object):
    def generate_face_value(self):
        return random.randint(1,6)

    def call_dice(self):
        self.val= self.generate_face_value()
        if self.val==1:
            print("-------------")
            print("|           |")
            print("|     *     |")
            print("|           |")
            print("-------------")
        elif self.val==2:
            print("-------------")
            print("|           |")
            print("|   *   *   |")
            print("|           |")
            print("-------------")
        elif self.val==3:
            print("-------------")
            print("|     *     |")
            print("|     *     |")
            print("|     *     |")
            print("-------------")
        elif self.val==4:
            print("-------------")
            print("| *       * |")
            print("|           |")
            print("| *       * |")
            print("-------------")
        elif self.val==5:
            print("-------------")
            print("| *       * |")
            print("|     *     |")
            print("| *       * |")
            print("-------------")
        elif self.val==6:
            print("-------------")
            print("| *       * |")
            print("| *       * |")
            print("| *       * |")
            print("-------------")
if __name__=="__main__":
    dice=DiceSim()
    user_input=input("Do you want to roll the dice? Input Y/N: \n")
    while user_input.lower() == "y":
        dice.call_dice()
        user_input = input("Do you want to continue? Input Y/N: \n")
