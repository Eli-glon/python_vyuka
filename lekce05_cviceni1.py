#uloha 1 vytvořte list o libovolnych 5 číslech a pomoci for cyklu spočítejte součet čísel v listu
muj_list = [1, 2, 3, 4, 5]

soucet=0# přidáme do součtu a budmeme si to pamatovat, duležitý krok tento řádek
for i in range(len(muj_list)):
    soucet = soucet + muj_list [i]

print (soucet)

#uloha 2 list 5 cisel pomoci for cyklu vypsat v opačném pořadí

for i in range (len(muj_list)-1, -1, -1):#len nám vrací počet čísel - tady 5 ..... [4, -1, -1] - pojedeme pozpatku
    #print(i)když nevim vypíšu
    print(muj_list[i])

#uloha 3 list 5 číslic, pomoci cisel aritmetricky pruměr
soucet = 0
for i  in range (len(muj_list)):
    soucet += muj_list[i] #x=x+1 stejny jako x+=1

prumer = soucet / len(muj_list)
print (prumer)


#uloha4 najdi nejvyšší číslo

max = muj_list[0]
for i in range (1,len(muj_list)): # nechceme porovnávat 0 s 0 - proto začínáme od 1
    if muj_list [i] > max: #víme kolikátý prvek listu máme 
        max = muj_list[i] 
print (max)



muj_list = ["ahoj", "nazdar", "cau", "servus", "čus"]
#s for pracujeme s celim tym seznamem 
for i in range(len(muj_list) - 1): #musi skončit dřiv aby nešel mimo
    print(str(i)+muj_list [i])
    print (muj_list [i + 1])

# comand item pracuje jenom s tím itemem 


#uloha 5: vypiš 2 největší čísla z listu
