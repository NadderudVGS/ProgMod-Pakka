def new_metode(funksjon, start=float, tol=1e-10, maxLoop=1000):
    ''' 
        Returnerer et nullpunkt i en graf
        ved å bruke f'(x). 
        ( Newtons Metode ) 
    '''
    c = 1
    a = start
    i = 0
    while abs(funksjon(c)) >= tol or i <= maxLoop:
        try:
            c = a - funksjon( a ) / new_sym_kvot( funksjon, a )
            a = c
            i += 1
        except:
            return c
    return c