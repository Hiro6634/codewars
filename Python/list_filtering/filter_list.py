def filter_list(lst):
    res = []
    for l in lst:
        if isinstance(l, int):
            res.append(l)
    return res

if __name__=='__main__':
    lst = [1,2,'a','b']
    print("filter_list({0}) == {1}".format(lst, filter_list(lst)))
    lst = [1,'a','b',0,15]
    print("filter_list({0}) == {1}".format(lst, filter_list(lst)))
    lst = [1,2,'aasf','1','123',123]
    print("filter_list({0}) == {1}".format(lst, filter_list(lst)))
