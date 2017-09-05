def checkerboard(rows, cols):
    row = ["", ""]
    for i in range(cols):
        if i % 2 == 0:
            row[0] += "*"
            row[1] += " "
        else:
            row[0] += " "
            row[1] += "*"
    for j in range(rows):
        print row[j % 2]

checkerboard(8, 8)
