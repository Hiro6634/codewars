def filter_list(l):
    res = []
    for elm in l:
        if isinstance(elm, int):
            res.append(elm)
    return res

if __name__=='__main__':
    lst = [1,2,'a','b']
    print("filter_list({0}) == {1}".format(lst, filter_list(lst)))
    lst = [1,'a','b',0,15]
    print("filter_list({0}) == {1}".format(lst, filter_list(lst)))
    lst = [1,2,'aasf','1','123',123]
    print("filter_list({0}) == {1}".format(lst, filter_list(lst)))
