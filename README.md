# ProgMod-Pakka
Denne pakken skal hjelpe med å simplifisere/effektivisere programeringen av komplekse oppgaver i programmering og modelering. *(Pakken er spessielt rettet mot kappittel 7)*

## Inneholder

 - **[Areal](#areal)**
    - Rektangel
    - Sirkel
    - Trapes
 - **[Deriverte](#deriverte)**
    - Array
    - Dobbel deriverte
    - Newtons kvotient 
    - Newtons symetriske kvotient
 - **[Integrerte](#integrerte)**
    - Array
    - Rektangelmetoden 
    - Trapesmetoden 
 - **[Nullpunkt](#nullpunkt)**
    - Halveringsmetoden
    - Newtons metode
 - **[Plot](#plot)**
    - Enkel plot


## Hvordan bruke pakken?
Last ned mappen **progmod**. Derretter plaser progmod-mappen i samme mappe som programmet ditt. 


Supert! Nå burde alt være klart. Du kan teste med å skrive dette  i python filen din;
```python
from progmod import Areal

areal = Areal.sirkel(1) # radius

print(areal) # areal ≈ 3.14

```

## Areal

#### Rektangel
```python
areal = Areal.rektangel(float, float)  # Høyde * bredde
```

#### Sirkel
```python
areal = Areal.sirkel(float) # pi*radius^2
```

#### Trapes
```python
areal = Areal.trapes(float, float, float) # ( ( sideEn+sideTo ) * høyde ) / 2
```



## Deriverte
Her finner vi den deriverte numerisk, altso en tilnærmet verdi for stigningstallet. Videre kommer jeg til å bruke denne funksjonen som en eksempelfunksjon.
```python
def funksjon(x):

  y = x**2 + 2*x + 7

  return y
```

#### Array
Returnerer stigningstallet til et bestemt punkt i et array eller en liste. Gjelder ikke for endepunktene.

```python
s = Deriverte.array([1, 2, 3, 4], int) # int = posisjon til stigningstallet i arrayet. Her int = 1 & 2
```

#### Dobbel
Returnerer stigningstallet til den deriverte til funksjonen i en bestemt x-verdi. "Finner den dobbelderiverte til funksjonen"  *Gjelder for alle kuntinuerlige funksjoner.*

```python

s = Deriverte.dobbel(funksjon, x, h=1e-8) 
# x er punktet du vil finne stigningstallet, fks: 1.4
# h er en tilnærmet verdi for delta-x => 0, fra definisjonen til den deriverte
```


#### new_kvot
Returnerer stigningstallet til grafen i funksjonen i en bestemt x-verdi. *Bruker den klassiske definisjonen til den deriverte, for å estimere stigningstallet.*

```python

s = Deriverte.new_kvot(funksjon, x, h=1e-8) 
# x er punktet du vil finne stigningstallet, fks: 34.78
# h er en tilnærmet verdi for delta-x => 0, fra definisjonen til den deriverte
```

#### new_sym_kvot
Returnerer stigningstallet til grafen i funksjonen i en bestemt x-verdi. *Bruker bruker to ulike estimater av av stigningstallet for å finne et mere nøyaktig estimat.*

```python
s = Deriverte.new_sym_kvot(funksjon, x, h=1e-8) 
# x er punktet du vil finne stigningstallet, fks: 3.1
# h er en tilnærmet verdi for delta-x => 0, fra definisjonen til den deriverte
```


## Integrerte
Her finner vi den Integrerte ved hjelp av flere metoder (mest numeriske metoder). Dette er en eksempelfunksjon, som vil bli brukt for å vise fram metodene.

```python
def funksjon(x):

  y = -x**2 + 2*x + 7

  return y
```

#### array
Returnerer arealet for array med y verdier, med x-lengde 1 mellom dem.

```python
a = Integrerte.array([1, 2, 3, 4]) # ==>  a = 7.5
```

#### rektangel
Returnerer et estimat av arealet under en graf mellom to punkter. *Bruker rektangelmetoden for å estimere*


```python
a = Integrerte.rektangel(funksjon, start, slutt, antall)
# start = float , er startverdi
# slutt = float , er sluttverdi
# antall = int , er antall rektangler som brukes for estimeringen (desto fler, jo bedre)


```

#### trapes
Returnerer et estimat av arealet under en graf mellom to punkter. *Bruker trapesmetoden for å estimere, som er mer nøyaktig enn rektangelmetoden*

```python
a = Integrerte.trapes(funksjon, start, slutt, antall)
# start = float , er startverdi
# slutt = float , er sluttverdi
# antall = int , er antall trapes som brukes for estimeringen.

```


## Nullpunkt

#### halv_metode
Returnerer en estimering av x-verdien for et nullpunktet mellom to valgfrie punkter i en graf. *Brukes når vi vet at nullpunktet er mellom start- og sluttpunktet som ble satt*

```python
a = Nullpunkt.halv_metode(funksjon, start, slutt, tol=1e-10, maxLoop=1000)
# funksjon
# start = float , er startverdi
# slutt = float , er sluttverdi
# tol = float , er hvor nærme vi kan komme det ekte nullpunktet
# maxLoop = int , er hvor mange ganger vi vil lete etter nullpunktet (1000 er ofte nok)

```

#### new_metode
Returnerer en estimering av x-verdien for et nullpunktet til en graf, med ett startpunkt. *Brukes mere enn halveringsmetoden, fordi newtons metode er sjappere. 


```python
a = Nullpunkt.new_metode(funksjon, start, tol=1e-10, maxLoop=1000)
# funksjon
# start = float , er startverdi til søket
# tol = float , er hvor nærme vi kan komme det ekte nullpunktet
# maxLoop = int , er hvor mange ganger vi vil lete etter nullpunktet (1000 er ofte nok)

```


## Plot

#### simple
Lager et plott mellom to punkter til en funksjon.


```python
Plot.simple(funkjson, start=float, slutt=float, x_label="x", y_label="y"):
# funksjon
# start = float , er startverdi 
# slutt = float , er sluttverdi 
```
