l1 = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical','unicorns']

def type_list(lst):
    has_str = False
    has_num = False
    full_str = ""
    sum = 0
    for ele in lst:
        if isinstance(ele, int):
            has_num = True
            sum += ele
        elif isinstance(ele, str):
            if has_str:
                full_str += " "
            has_str = True
            full_str += ele
    if (has_str and has_num):
        ltype = "mixed"
    elif has_str:
        ltype = "string"
    elif has_num:
        ltype = "integer"
    else:
        ltype = "empty"
    print "The list you entered is of", ltype, "type"
    if has_str:
        print "String:", full_str
    if has_num:
        print "Sum:", sum

type_list(l1)
type_list(l2)
type_list(l3)
