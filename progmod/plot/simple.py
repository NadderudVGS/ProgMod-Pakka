from pylab import linspace, xlabel, ylabel, plot, show, grid

def simple(funkjson, start=float, slutt=float, x_label="x", y_label="y"):
    ''' 
        Lager enkel graf av funksjonen
        din. Passer fint for alle type grafer 
    '''

    x = linspace(start, slutt, 1001)
    y = funkjson(x)

    xlabel(x_label)
    ylabel(y_label)
    grid()
    plot(x, y)


