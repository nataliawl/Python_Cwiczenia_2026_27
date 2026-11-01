
## Zadanie 3.1.1
    
    x = 2;
    y = 3;
    if (x > y):
        result = x;
    else:
        result = y;

Program działa poprawnie, lecz nie jest poprawny składniowo.
W języku Python nie dodaje się średnika na końcu linii.

## Zadanie 3.1.2

    for i in "axby": if ord(i) < 100: print(i)

Program nie jest poprawnie składniowo, ponieważ if (nie jest to instrukcja prosta) nie może byc w tej samej linii co for.
Kod poprawnie wyglądałby tak:
    
    for i in "axby":
        if ord(i) < 100:
            print(i)

## Zadanie 3.1.3

    for i in "axby": print(ord(i) if ord(i) < 100 else i) 

Program działa i jest przypadkiem specialnym:
    wiersz nagłówka : instrukcja_prosta

## Zadanie 3.2.1

    L = [3, 5, 4];
    L = L.sort() <-- źle

Funkcja sort() nie zwraca niczego. W celu posortowania listy L wystarczy:

    L.sort()

## Zadanie 3.2.2

    x, y = 1, 2, 3 <-- żle

Jest za duzo wartości do przypisania zmiennym!
Poprawnie:
   
    x,y = 1, 2

## Zadanie 3.2.3

    X = 1, 2, 3
    X[1] = 4 <-- źle

Krotki sa niezmienne - raz przypisanej wartości nie zmienimy!
Jeśli chcemy moc zmieniać wartosci należy użyć listy

## Zadanie 3.2.4

    X = [1, 2, 3]
    X[3] = 4 <-- źle

Zły indeks - w listach indeksy są od 0 do n - 1, gdzie n to liczba elementów listy.

## Zadanie 3.2.5

    X = "abc";
    X.append("d") <-- źle

W pythonie nie możemy zmieniać elementów o typie string!

## Zadanie 3.2.6

    L = list(map(pow, range(8)))
                    ^
                    |
                   żle
Funckja pow() wymaga min. 2 argumentów : liczbe i jej potęgę. 
W przykładzie nie podano listy potęg\
    
    powers = 2, 2, 2, 2, 2, 2, 2, 2
    L = list(map(pow, range(8), powers))
    print(L)