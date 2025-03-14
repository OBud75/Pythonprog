from src.board import Board

class BoardTest:
    @staticmethod
    def test_best_move(board: Board, move: tuple):
        """
        Teste si best_move joue le coup attendu.
        
        :param board: Plateau de jeu à tester.
        :param expected_move: Tuple (y, x) du coup attendu.
        """
        player = "O"
        board.make_best_move(player) 
        y, x = move
        assert board.position[y][x] == "O", f"Erreur : 'O' aurait dû jouer sur {move}, mais ne l'a pas fait."

    @staticmethod
    def run_tests():
        
        board1 = Board(position=[
            ["O", "O", " "],
            ["X", "X", " "],
            [" ", " ", " "]
        ])
        BoardTest.test_best_move(board1, (0, 2))
      
        board2 = Board(position=[
            ["X", "X", " "],
            ["O", "O", " "],
            [" ", " ", " "]
        ])
        BoardTest.test_best_move(board2, (0, 2))

        board3 = Board(position=[
            ["X", "O", " "],
            ["O", "X", " "],
            [" ", " ", " "]
        ])
        BoardTest.test_best_move(board3, (2, 2))
        # Je ne suis pas sur de comprendre les 3 premiers tests :
        # le plateau indique que X et O ont joués 2 fois, Ca serait donc à "X" de jouer non ?
        board4 = Board(position=[
            ["O", " ", " "],
            [" ", "X", " "],
            [" ", " ", "X"]
        ])
        BoardTest.test_best_move(board4, (0, 2)) 

        print("Tous les tests sont passés avec succès !")

# Exécution des tests
BoardTest.run_tests()
