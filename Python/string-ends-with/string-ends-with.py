def solution(str,end):
    lend = len(end)
    lstr = len(str)
    i = lstr - lend
    return str[i:] == end

if __name__=='__main__':
    str = 'escolopendra'
    end = 'ra'

    print("solution(\'{0}\', \'{1}\') -> {2}".format(str,end,solution(str,end)))
