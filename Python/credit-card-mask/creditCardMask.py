def maskify(cc):
    msk = ""

    l = len(cc)
    for i in range(l):
        msk +=  cc[i]  if (i > l-5) else '#'

    return msk

if __name__=='__main__':
    card="4556364607935616"
    print("\"{0}\" --> \"{1}\"". format(card, maskify(card)))
    card="5616"
    print("\"{0}\" --> \"{1}\"". format(card, maskify(card)))    
    card="6"
    print("\"{0}\" --> \"{1}\"". format(card, maskify(card)))        
    card=""
    print("\"{0}\" --> \"{1}\"". format(card, maskify(card)))        