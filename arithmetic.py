import random


class AEA:

    def __init__(self):
        self.total = 5
        self.count = 0
        self.right = 0
        self.nums = list(range(2, 10))
        self.squares = list(range(11, 30))
        self.ops = ['+', '-', '*']
        self.exp = ""
        self.val = 0
        self.level = 0
        self.lmessage = {1: "simple operations with numbers 2-9",
                         2: "integral squares of 11-29"}

    def play(self):
        self.choose_level()
        while self.count < self.total:
            self.get_input()
            self.eval_answer()
            self.count += 1
        self.exit()

    def choose_level(self):
        while True:
            try:
                print("Which level do you want? Enter a number:")
                print(f"1 - {self.lmessage[1]}")
                print(f"2 - {self.lmessage[2]}")
                self.level = int(input())
                if self.level not in [1, 2]:
                    raise Exception
                break
            except:
                print("Incorrect format.")

    def get_input(self):
        if self.level == 1:
            [a, b] = random.choices(self.nums, k=2)
            exp = f"{a} {random.choice(self.ops)} {b}"
            print(exp)
        else:
            a = random.choice(self.squares)
            print(a)
            exp = f"{a} ** 2"
        self.exp = exp
        while True:
            try:
                self.val = int(input())
                break
            except:
                print("Incorrect format.")

    def eval_answer(self):
        if eval(self.exp) == self.val:
            print("Right!")
            self.right += 1
        else:
            print("Wrong!")

    def exit(self):
        print(f"Your mark is {self.right}/{self.total}. Would you like to save the result? Enter yes or no.")
        ans = input()
        if ans in ['yes', 'YES', 'y', 'Yes']:
            name = input("What is your name?\n")
            text = f"{name}: {self.right}/{self.total} in level {self.level} ({self.lmessage[self.level]})"
            with open("results.txt", "a") as f:
                f.write(text)
            print('The results are saved in "results.txt".')


AEA().play()
