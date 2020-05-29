def rektangel_areal(høyde=float, bredde=float):
    ''' Returnerer arealet til et rektangel   '''
    return høyde * bredde

def rektangel(funksjon, start=float, slutt=float, antall=int):
    ''' 
        Returnerer arealet under grafen ved å
        bruke rektangler. ( Numerisk 
        Integrasjon med rektangler ) 
    '''
    bredde = ( slutt - start ) / antall
    A = 0
    for i in range(antall):
        A += abs(rektangel_areal( funksjon(start + bredde * i ), bredde))
    
    return A