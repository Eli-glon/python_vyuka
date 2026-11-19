vektor = [1, 2, 3] # dýlka 3 - 0,1,2 prvek
#ůžu tam narvat desetiný číslo, string ...
print (vektor)
print (type(vektor))# typ tý proměný - list
print(len(vektor))#délka 
print(vektor [0])#vrátí hodnotu na pozici
print(type(vektor [0]))#vrátí typ int - jenom typ toho údaje v seznamu 

vektor [1] = 8 #přepíše mi číslo na prvním místě (2) na 8 - [1,8,3]
print (vektor)
# nepojmenovavat proměný aby to nebylo klíčový slovo


muj_list = [1, 2, 3, 4, 5, 6, 7]

for i in range (len(muj_list)):#i mužeme měnit, mužem si dát co chceme, jakoukoli proměnou, význam má v tom cykolu
    print(muj_list[i])# i hodnota=0,1,2,3,4,5, ..... [] hodnota=0,1,2.....