def array(array, x_verdi=int):
    ''' 
        Finner stigningstallet til et array 
        i en bestemt x-verdi. Ikke de 2
        yttersete punktene!
    '''
    if x_verdi == len(array)-1:
        pass
    elif x_verdi == 0:
        pass
    else:
        fder = ( array[x_verdi +1] - array[(x_verdi - 1)] ) / (2)
        return fder

    return None