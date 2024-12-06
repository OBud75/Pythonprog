with open('./input.txt', 'r') as fichier:
    
    ls1 = []
    ls2 = []
    
    total = 0
    
    for ligne in fichier:
        val = ligne.split("   ")
        val[1] = val[1].strip()
        ls1.append(val[0])
        ls2.append(val[1])

    ls1.sort()
    ls2.sort()

    for i,j in zip(ls1,ls2):
        somme = int(i) -int(j)
        total += abs(somme)
        
    print(total)

    
    