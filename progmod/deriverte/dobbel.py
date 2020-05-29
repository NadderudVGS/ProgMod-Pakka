def dobbel(funksjon, x_verdi=float, h=1e-8):
    ''' 
        Finner stigningstallet til den deriverte
        til funksjonen i en bestemt x-verdi. 
        ( Derivasjon 2x ) 
    '''
    fder2 = ( funksjon( x_verdi + h ) - 2*funksjon(x_verdi) +  funksjon(x_verdi - h) ) / h**2
    return fder2