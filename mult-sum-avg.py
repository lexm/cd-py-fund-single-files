# Multiples part I:

def print_odds(start, end):
    if(start % 2 == 0):
        start += 1
    for i in range(start, end, 2):
        print i
# print_odds(1,1000)

# Multiples part 2:
def mult_fives(end):
    for j in range(5, end + 1, 5):
        print j
# mult_fives(1000000)

# Sum List:
a = [1, 2, 5, 10, 255, 3]

def sum_list(lst):
    result = 0
    for k in lst:
        result += k
    print result

sum_list(a)

# Average List

def average_list(lst):
    sum = 0
    for l in lst:
        sum += l
    print sum / len(lst)

average_list(a)
