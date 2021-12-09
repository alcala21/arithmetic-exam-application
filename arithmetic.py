import random


class AEA:

    def __init__(self):
        self.total = 5
        self.count = 0
        self.right = 0
        self.nums = list(range(2, 10))
        self.ops = ['+', '-', '*']
        self.exp = ""
        self.val = 0

    def play(self):
        while self.count < self.total:
            self.get_input()
            self.eval_answer()
            self.count += 1
        print(f"Your mark is {self.right}/{self.total}.")

    def get_input(self):
        [a, b] = random.choices(self.nums, k=2)
        self.exp = f"{a} {random.choice(self.ops)} {b}"
        print(self.exp)
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


AEA().play()
