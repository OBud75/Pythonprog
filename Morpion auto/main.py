from src.board import Board


empty = Board(position = [
            [" ", " ", " "], 
            [" ", " ", " "], 
            [" ", " ", " "]])

def play_game(board):
    print("Début de la partie :")
    print(board)

    players = ["X", "O"]
    turn = 0

    # Boucle principale du jeu
    while board.empty_cells:
        current_player = players[turn % 2]

        if current_player == "X":
            print("\nÀ vous de jouer (X) ! Entrez la position (ligne, colonne) :")
            try:
                move = input("Format: ligne,colonne (exemple: 1,2): ").strip()
                row, col = map(int, move.split(","))
                if (row, col) in board.empty_cells:
                    board.position[row][col] = "X"
                else:
                    print("Position invalide ou déjà occupée. Essayez à nouveau.")
                    continue
            except (ValueError, IndexError):
                print("Entrée invalide. Essayez à nouveau.")
                continue
        else:
            
            board.make_best_move("O")
            print("\nTour de O (best move) :")

        print(board)

        if board.is_won(current_player):
            print(f"\n{current_player} a gagné !")
            return

        turn += 1

    print("\nMatch nul !")

play_game(empty)

