def trapes_areal(sideEn=float, sideTo=float, høyde=float):
    """ Returnerer arealet til et trapes   """
    return abs(( ( sideEn+sideTo ) * høyde ) / 2)


def array(array):
    ''' 
        Returnerer arealet til array
    '''
    A = 0
    bredde = 1
    for i in range(0, len(array)-1):
        A += trapes_areal( array[bredde * i],        
                           array[bredde * (i+1)],    
                           bredde )

    return A
