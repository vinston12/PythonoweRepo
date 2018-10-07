
# nr 1
n = 5
print("code "*n) # wyświetla code 'n' razy
# nr 2
a = 5
b = 10
b, a = a, b
print(a," ",b) # swap dwóch zmiennych
# nr 3
from collections import Counter
def is_anagram(a, b):
    return Counter(a) == Counter(b)
print(is_anagram("pierd","iderp")) # sprawdza czy wyrazy są anagramami
# nr 4
a = "Dórms"
print("Wyraz: ",a)
print("Odwrocone: ",a[::-1]) # wypisuje od tylu
# nr 5
a = [1,2,3]
x,y,z = a
print("x = ",x, " y = ",y, " z = ",z) # przypisanie elementow tablicy do zmiennych po kolei
# nr 6
a=5
b=10
c=15
a,b,c=c,b,a
print(a,b,c)
print("epic fail")