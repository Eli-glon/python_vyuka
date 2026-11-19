#for i in range(5) stejny jako (0,5) horní a dolní hranice, range bude dosazovat za i hodnoty 
#(2,8,2) - vypíše hodnoty po 2 = 2,4,6 (8 už není v intervalu) <2,8)
#když víme kolikrát se bude opakovat/chceme vědět v kolikátym kroku jsme 



for i in range (2,8,2):
    print("ahoj")
    print(i)

x=10
while (x > 10):
    print ("Ahoj")
    x=x-1
    if x==5:
        break

print ("konec")