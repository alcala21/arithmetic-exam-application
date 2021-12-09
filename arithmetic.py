# write your code here
import random

[a, b] = random.choices(range(2, 10), k=2)
op = random.choice(['+', '-', '*'])
outs = {True: "Right!", False: "Wrong!"}

exp = f"{a} {op} {b}"
print(exp)
ans = input()
print(outs[eval(exp) == eval(ans)])

