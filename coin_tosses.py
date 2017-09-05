import random
def coin_tosses(num):
    count = {
        "head": 0,
        "tail": 0
        }
    line = "Attempt #{}: Throwing a coin... It's a {}! ... "
    line += "Got {} head(s) so far and {} tail(s) so far"
    for i in range(1, num + 1):
        toss = round(random.random())
        if toss == 0:
            toss_str = "head"
        else:
            toss_str = "tail"
        count[toss_str] += 1
        print line.format(i, toss_str, count["head"], count["tail"])
coin_tosses(5000)
