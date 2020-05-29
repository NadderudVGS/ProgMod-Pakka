def trapes_areal(sideEn=float, sideTo=float, høyde=float):
    """ Returnerer arealet til et trapes   """
    return ( ( sideEn+sideTo ) * høyde ) / 2


def trapes(funksjon, start=float, slutt=float, antall=int):
    ''' 
        Returnerer arealet under grafen ved å
        bruke trapeser. ( Numerisk 
        Integrasjon med trapeser ) 
    '''

    bredde = ( slutt - start ) / antall

    A = 0
    for i in range(0, antall):
        A += abs(trapes_areal( funksjon( start + bredde * i ),        
                           funksjon( start + bredde * (i+1) ),    
                           bredde ))

    return A