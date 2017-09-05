import string
test_str = "The quick brown fox"
test_str2 = "     more stuff here     "
test_list = ["Here's", "a", "test", "list"]

print test_str.find("o")
print test_str.rfind("o")
print test_str.rfind("z")
print test_str.index("o")
# print test_str.rindex("z")
print test_str.count("o")
print test_str.lower()
print test_str.split()
print test_str.split("o")
print test_str.split(" ", 2)
print test_str.rsplit(" ", 2)
print string.join(test_list)
print "*" + test_str2.lstrip() + "*"
print "*" + test_str2.rstrip() + "*"
print "*" + test_str2.strip() + "*"
print test_str.swapcase()
print test_str.translate(None, "aeiou")
print "*" + test_str.ljust(25) + "*"
print "*" + test_str.rjust(25) + "*"
print "*" + test_str.center(25) + "*"
print "25".zfill(5)
print test_str.replace("quick", "slow")
print test_list[1:3]
print len(test_list)
print test_list[-2]
print test_list * 2
print "a" in test_list
print "b" in test_list
for wrd in test_list: print wrd
print test_list[1], test_list[-2]
print cmp(test_str.split(), test_list)
test_list.extend(test_str.split())
print test_list
test_list.append("test")
print test_list
print test_list.count("test")
print test_list.index("brown")




