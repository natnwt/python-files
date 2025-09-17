import decimal
def zapisTrojkowy(n):
    trojkowy = ""
    while n > 0:
        reszta = n % 3
        trojkowy = str(reszta) + trojkowy
        n = n // 3
    return trojkowy


znaki = []
with open('symbole.txt', 'r') as file:
    for line in file:
        linia = list(line.strip())
        znaki.append(linia)
    print(znaki)
for i in range(len(znaki) - 2):
    for j in range(len(znaki[i]) - 2):
        if znaki[i][j] == znaki[i][j + 1] == znaki[i][j + 2] == znaki[i + 1][j] == znaki[i + 1][j + 1] == znaki[i + 1][j + 2] == znaki[i + 2][j] == znaki[i + 2][j + 1] == znaki[i + 2][j + 2]:
            print(i+2,j+2)

l_trojkowa = ''
tab_trojkowe = []
for i in range(len(znaki)):
    l_trojkowa = ''
    for j in range(len(znaki[i])):
        if znaki[i][j] == '+':
            l_trojkowa += "1"
        elif znaki[i][j] == '*':
            l_trojkowa += "2"
        else:
            l_trojkowa += "0"
    tab_trojkowe.append(l_trojkowa)
print(tab_trojkowe)

tab_tr_na_dec = []
for i in range(len(tab_trojkowe)):
    tr_na_dec = int(tab_trojkowe[i], 3)
    tab_tr_na_dec.append(tr_na_dec)
print(max(tab_tr_na_dec))

for i in range(len(tab_trojkowe)):
    if tab_tr_na_dec[i] == max(tab_tr_na_dec):
        print(i)
print(znaki[142])

suma = 0
for i in range(len(tab_tr_na_dec)):
    suma += tab_tr_na_dec[i]

print(suma)
dozamiany = zapisTrojkowy(suma)
zmieniony = ''
for i in range(len(dozamiany)):
    if dozamiany[i:i+1:] == "1":
        zmieniony += "+"
    elif dozamiany[i:i+1:] == "2":
        zmieniony += "*"
    else:
        zmieniony += "o"
print(zmieniony)











