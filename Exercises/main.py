def isPrime(x):
    half = x/2                  
    for i in range(2, int(half)): #i startuje od 2 do polowy, bo 1 nas nie obchodzi, int(half) to zamiana wyniku dzielenia '1.0' (typ float) na '1' (l.calk), bo python nie podzieli nam przez floata. Zobacz "casting" w tutorialach
        if x % i == 0:            #jesli znajdzie sie dzielnik bez reszty, drukujemy go, zwracamy falsz, bo nie jest to l.p. i konczymy dzialanie funkcji
            print(str(x) + ' can be divided by ' + str(i))
            return False
    return True                   #jesli w petli 'for' nie znajdzie sie dzielnik, to wykona sie ta linijka kodu, w innym wypadku wykona sie linjka 6 i do 7 nigdy nie dojdzie
prime = 17
comp = 12                         #to np Twoje liczby z pliku
print(isPrime(prime))             #tu sie najpierw wykona funkcja wewnatrz nawiasow, czyli isPrime, ktorej przekazalismy argument prime
print(isPrime(comp))              #najpierw sie wyswietli True, potem tekst i False
