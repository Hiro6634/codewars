def array_diff(a, b):
    for _b in b:
        while _b in a:
            a.remove(_b) 
    return a

if __name__=='__main__':
    print("{0} {1}".format(array_diff([1,2], [1]), "a was [1,2], b was [1], expected [2]"))
    print("{0} {1}".format(array_diff([1,2,2], [1]), "a was [1,2,2], b was [1], expected [2,2]"))
    print("{0} {1}".format(array_diff([1,2,2], [2]), "a was [1,2,2], b was [2], expected [1]"))
    print("{0} {1}".format(array_diff([1,2,2], []), "a was [1,2,2], b was [], expected [1,2,2]"))
    print("{0} {1}".format(array_diff([], [1,2]), "a was [], b was [1,2], expected []"))
    print("{0} {1}".format(array_diff([1,2,3], [1, 2]), "a was [1,2,3], b was [1, 2], expected [3]"))
