def new_sym_kvot(funksjon, x_verdi=float, h=1e-8):
    ''' 
        Finner stigningstallet til funksjonen 
        i en bestemt x-verdi. 
        ( Newtons Symetriske Kvotient, derivasjon 1x ) 
    '''
    fder = ( funksjon(x_verdi + h) - funksjon(x_verdi - h) ) / (2*h)
    return fder