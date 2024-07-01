#day 6 act 2
row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))

i = 0
while i < row:
    if i == 0 or i == row - 1:
        print("*" * column)
    else:
        print("" + " " * (column - 2) + "")
    i += 1