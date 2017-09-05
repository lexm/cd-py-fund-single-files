def compare_lists(list1, list2):
    if len(list1) !=  len(list2):
        print "The lists are not the same."
        return
    else:
        for idx in range(len(list1)):
            if list1[idx] != list2[idx]:
                print "The lists are not the same."
                return
        print "The lists are the same"

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compare_lists(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
compare_lists(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
compare_lists(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
compare_lists(list_one, list_two)


