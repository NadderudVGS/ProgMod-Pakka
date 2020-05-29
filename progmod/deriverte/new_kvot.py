def new_kvot(funksjon, x_verdi=float, h=1e-8):
    ''' 
        Finner stigningstallet til grafen i funksjonen 
        i en bestemt x-verdi.
        ( Newtons Kvotient ) 
    '''
    fder = ( funksjon( x_verdi+h ) + funksjon( x_verdi ) ) / h
    return fder
