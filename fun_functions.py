def odd_even(start, end):
    for i in range(start, end + 1):
        line = "Number is " + str(i) + ". This is an "
        if i % 2 == 0:
            line += "even"
        else:
            line += "odd"
        line += " number."
        print line
# odd_even(1, 2000)

a = [2,4,10,16]

def multiply(lst, mult):
    result = []
    for x in lst:
        result.append(x * mult)
    return result
# print multiply(a, 5)

def layered_multiples(arr):
    new_array = []
    one = [1]
    for x in arr:
        new_array.append(one * x)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
# print x
