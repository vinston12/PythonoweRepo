# zamiana wartosci dwoch zmiennych bez zmiennej pomocniczej

pierwszaZmienna = 5

drugaZmienna = 10

pierwszaZmienna = pierwszaZmienna + drugaZmienna

drugaZmienna = pierwszaZmienna - drugaZmienna

pierwszaZmienna = pierwszaZmienna - drugaZmienna

print("Wartosci pierwszej = " + str(pierwszaZmienna) + " wartosc drugiej = " + str(drugaZmienna))

# łatwiejszy sposob
a = 5
b = 10
b, a = a, b
print("a = " + str(a))
print("b = " + str(b))



















