#def draw_stars(lst):
#    ast = "*"
#    for num in lst:
#        print ast * num

#x = [4, 6, 1, 3, 5, 7, 25]
#draw_stars(x)

def draw_stars(lst):
    for item in lst:
        if type(item) is str:
            char = item[0].lower()
            num = len(item)
        else:
            char = "*"
            num = item
        print char * num

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)

