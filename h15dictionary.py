def faktoriyel(n, d):
    d[n] = 1 if n == 1 else n * faktoriyel(n - 1, d)
    return d[n]

sayi = int(input("Bir sayı gir: "))
d = {}
faktoriyel(sayi, d)
print(d)