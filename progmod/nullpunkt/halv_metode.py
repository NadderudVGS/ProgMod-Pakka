def halv_metode(funksjon, start, slutt, tol=1e-10, maxLoop=1000):
    ''' 
        Returnerer et nullpunkt i en graf
        innenfor et bestemt ommråde.
        ( Halveringsmetoden ) 
    '''
    p = ( start+slutt ) / 2
    i = 0
    while abs(funksjon(p)) >= tol and i <= maxLoop:
        p = ( start + slutt ) / 2
        if funksjon(p) * funksjon(start) > 0 :
            start = p
        
        elif funksjon(p) * funksjon(start) < 0:
            slutt = p
            
        i += 1

    return p