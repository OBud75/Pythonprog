def afficher_jeu(jeu):
    print(f"{jeu[0]} {jeu[1]} {jeu[2]}")
    print(f"{jeu[3]} {jeu[4]} {jeu[5]}")
    print(f"{jeu[6]} {jeu[7]} {jeu[8]}")

def verifier_victoire(jeu, joueur):
    # Combinaisons gagnantes : lignes, colonnes et diagonales
    combinaisons = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    # Ne pas hésiter à remplacer les commentaires par des variables explicites
    lines = [0, 1, 2], [3, 4, 5], [6, 7, 8]
    columns = [0, 3, 6], [1, 4, 7], [2, 5, 8]
    diagonals = [0, 4, 8], [2, 4, 6]
    combinaisons = lines + columns + diagonals

    return any(all(jeu[pos] == joueur for pos in combo) for combo in combinaisons)

def morpion():
    jeu = [" " for _ in range(9)]  # Jeu sous forme de liste plate
    joueurs = ["X", "O"]
    tour = 0

    while tour < 9:
        joueur = joueurs[tour % 2]
        print(f"Au tour de {joueur}")

        # Entrée utilisateur
        try:
            case = int(input("Choisissez une case (0-8) : "))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un chiffre entre 0 et 8.")
            continue

        if case not in range(9):
            print("Case invalide. Choisissez un chiffre entre 0 et 8.")
            continue

        if jeu[case] != " ":
            print("Case déjà occupée. Réessayez.")
            continue

        # Met à jour le jeu
        jeu[case] = joueur
        afficher_jeu(jeu)

        # Vérifie la victoire
        if verifier_victoire(jeu, joueur):
            print(f"Félicitations ! Le joueur {joueur} a gagné !")
            return

        tour += 1

    print("Match nul !")

if __name__ == "__main__":
    morpion()
