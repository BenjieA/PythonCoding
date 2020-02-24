# TOE: Write a program that will find all such numbers which are divisible by 7, but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be returned in a comma-separated sequence on a single line.


def multi_finder(maxval, minval, tohave, toavoid):
    trutharray = []
    for i in range(maxval):
        if i>minval and i % tohave == 0 and i % toavoid != 0:
            trutharray.append(i)
    print(str(trutharray).strip('[]'))

multi_finder(3200,2000, 7, 5)

