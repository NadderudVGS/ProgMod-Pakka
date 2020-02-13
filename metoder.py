from pylab import *

def plot_graf_simple(f, start, slutt):
    ''' 
        Lager enkel graf av funksjonen
        din. Passer fint for alle type grafer 
    '''

    x = linspace(start, slutt, 1000)
    y = f(x)

    xlabel("x")
    ylabel("y")

    plot(x, y)

def areal_rect(høyde, bredde):
    ''' Returnerer arealet til et rektangel   '''
    return høyde * bredde

def areal_trapes(sideEn, sideTo, høyde):
    ''' Returnerer arealet til et trapes   '''
    return ( ( sideEn+sideTo ) * høyde ) / 2

def num_int_rect(funksjon, start, slutt, antall):
    ''' 
        Returnerer arealet under grafen ved å
        bruke rektangler. ( Numerisk 
        Integrasjon med rektangler ) 
    '''
    bredde = ( slutt - start ) / antall
    A = 0
    for i in range(antall):
        A += areal_rect( f(start + bredde * i ), bredde)
    
    return A

def num_int_trap(funksjon, start, slutt, antall):
    ''' 
        Returnerer arealet under grafen ved å
        bruke trapeser. ( Numerisk 
        Integrasjon med trapeser ) 
    '''
    A = 0
    bredde = ( slutt - start ) / antall

    for i in range(antall):
        A += areal_trapes( f( start + bredde * i ),        
                           f( start + bredde * (i+1) ),    
                           bredde )

    return A

def new_kvot(funksjon, x_verdi, h=1e-8):
    ''' 
        Finner stigningstallet til grafen i funksjonen 
        i en bestemt x-verdi.
        ( Newtons Kvotient ) 
    '''
    fder = ( funksjon( x_verdi+h ) + funksjon( x_verdi ) ) / h
    return fder

def new_sym_kvot(funksjon, x_verdi, h=1e-8):
    ''' 
        Finner stigningstallet til funksjonen 
        i en bestemt x-verdi. 
        ( Newtons Symetriske Kvotient ) 
    '''
    fder = ( funksjon(x_verdi + h) - funksjon(x_verdi - h) ) / (2*h)
    return fder

def new_metode(funksjon, start, tol=1e-10, maxLoop=1000):
    ''' 
        Returnerer et nullpunkt i en graf
        ved å bruke f'(x). 
        ( Newtons Metode ) 
    '''
    c = 1
    a = start
    i = 0
    while abs(funksjon(c)) >= tol and i <= maxLoop:
        c = a - funksjon( a ) / new_sym_kvot( funksjon, a )
        a = c
        i += 1

    return c

def halv_metode(funksjon, start, slutt, tol=1e-10, maxLoop=1000):
    ''' 
        Returnerer et nullpunkt i en graf
        innenfor et bestemt ommråde.
        ( Halveringsmetoden ) 
    '''
    p = ( start+slutt ) / 2
    i = 0
    while abs(funksjon(p)) >= tol and i <= maxLoop:
        if funksjon(p) * funksjon(start) > 0 :
            p = ( p + slutt ) / 2
            start = p
        
        elif funksjon(p) * funksjon(start) < 0:
            p = ( start + p ) / 2
            slutt = p
            
        i += 1

    return p
