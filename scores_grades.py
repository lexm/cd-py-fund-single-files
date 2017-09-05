import random
import string

def gen_score():
    return random.randint(60,100)
def gen_line():
    score = gen_score()
    if score == 100:
        grade_idx = 0
    else:
        grade_idx = (99 - score) / 10
    grade = string.ascii_uppercase[grade_idx]
    return "Score: {}; Your grade is {}".format(score, grade)
for _ in range(10):
    print gen_line()
