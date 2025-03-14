with open('./input.txt', 'r') as fichier:
    
    ls1 = []
    ls2 = []
    
    total = 0
    
    for ligne in fichier:
        val = ligne.split("   ")
        val[1] = val[1].strip()
        ls1.append(val[0])
        ls2.append(val[1])

    # A partir d'ici on peut normalement refermer le fichier
    # car on a récupéré toutes les informations nécessaires.
    # Ca reviendrait à enlever l'indentation de la suite du code.
    ls1.sort()
    ls2.sort()

    for i,j in zip(ls1,ls2):
        somme = int(i) -int(j)
        total += abs(somme)
        
    print(total)

    # Regardez les "list comprehension", ainsi que les générateurs,
    # très puissantes en python et évitent l'approche fonctionnelle de "zip", "map" etc
    # On se retrouverait avec une expression telle que
    print(sum(abs(int(i) -int(j))) for i,j in zip(ls1,ls2))
    