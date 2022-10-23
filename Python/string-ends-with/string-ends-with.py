def solution(string,ending):
    lend = len(ending)
    lstr = len(string)
    i = lstr - lend
    return string[i:] == ending

if __name__=='__main__':
    str = 'escolopendra'
    end = 'ra'

    print("solution(\'{0}\', \'{1}\') -> {2}".format(str,end,solution(str,end)))
