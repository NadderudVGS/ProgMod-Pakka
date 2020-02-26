# ProgMod-Pakka
Alle funksjoner du trenger for å fullføre faget: programmering og modellering x

## Inneholder

 - [Enkel graf tegner](#enkel-graf-tegner)
 - [Numerisk integrasjon](#numerisk-integrasjon)
 - [Newton's kvotient](#newtons-kvotient)
 - [Newton's symmetriske kvotient](#newtons-symmetriske-kvotient)
 - [Newton's metode](#newtons-metode)
 - [Halverings metoden](#halverings-metoden)
 

## Hvordan bruke pakken
Last ned filen `metoder.py` og plaser den i samme mappe som programmet ditt. Deretter importer pakken med å skrive i hovedprogrammet; 

`from metoder import *`

Supert! Nå burde alt være klart.

## Enkel graf tegner
Plotter automatisk en graf i et området, etter funksjonen har blit kalt. 

`plot_graf_simple( funksjon, start, slutt )`

 - `funksjon` - f(x), funksjonen som du vil plotte. Må returnere funksjonsutrykket.
 - `start` - fra denne x-verdien 
 - `slutt` - til denne x-verdi 
  
 ## Numerisk integrasjon
Estimerer arealet under en graf i et bestemt området. Fra y = 0

 ### Numerisk integrasjon med rektangler
 Bruker rektangler til å estimere arealet under grafen. Flere rektangler gir en bedre estimering.
 
`num_int_rect( funksjon, start, slutt, antall )`

 - `funksjon` - f(x), funksjonen som du vil regne arealet til. Må returnere funksjonsutrykket.
 - `start` -  fra denne x-verdien 
 - `slutt` - til denne x-verdi 
 - `antall` - hvor mange rektangler som blir brukt. 
 
 
  ### Numerisk integrasjon med trapeser
  Bruker trapeser til å estimere arealet under grafen. Flere trapeser gir en bedre estimering. ( denne metoden er mer nøyaktig enn rektangel-metoden )
  
`num_int_trap( funksjon, start, slutt, antall )`

 - `funksjon` - f(x), funksjonen som du vil regne arealet til. Må returnere funksjonsutrykket.
 - `start` -  fra denne x-verdien 
 - `slutt` - til denne x-verdi 
 - `antall` - hvor mange trapeser som blir brukt. Flere trapeser -> mer nøyaktig
 
 
 ## Newtons kvotient
 Metoden finner stigningstallet til til en funksjon i et punkt. Bruker den klassiske definisjonen til den deriverte, for å estimere stigningstallet.
 
 `new_kvot( funksjon, x_verdi, h=1e-8 )`
 
 - `funksjon` - f(x), funksjonen som du vil finne stigningstallet til. Må returnere funksjonsutrykket.
 - `x_verdi` - f'(x_verdi), hvor du vil finne stigninstallet
 - `h` - En estimering av delta-x fra definisjonen.
 
 
  ## Newtons symmetriske kvotient
   Metoden finner stigningstallet til til en funksjon i et punkt. Bruker bruker to ulike estimater av av stigningstallet for å finne et mere nøyaktig estimat
 
 `new_sym_kvot( funksjon, x_verdi, h=1e-8 )`
 
 - `funksjon` - f(x), funksjonen som du vil finne stigningstallet til. Må returnere funksjonsutrykket.
 - `x_verdi` - f'(x_verdi), hvor du vil finne stigninstallet
 - `h` - En estimering av delta-x fra definisjonen.
 
 
  ## Newtons metode
   Metoden et nullpunkt i en graf ved bruk av tangenter. Returnerer 
 
 `new_sym_kvot( funksjon, x_verdi, h=1e-8 )`
 
 - `funksjon` - f(x), funksjonen som du vil finne stigningstallet til. Må returnere funksjonsutrykket.
 - `x_verdi` - f'(x_verdi), hvor du vil finne stigninstallet
 - `h` - En estimering av delta-x fra definisjonen.
 
  ## Halverings metoden
  kommer snart...
 
  
