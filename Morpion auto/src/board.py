import random

class Board:

    def __init__(self, position, children = None, parents = None):
        self.position = position

        if children == None:
            self.children = []
        else:
            self.children = children       
        for chlid in self.children:
            chlid.parents.append(self)

        if parents == None:
            self.parents = []
        else:
            self.parents = parents
        for parent in self.parents:
            parent.children.append(self)

    def __str__(self):
        return "\n".join(f"{row}" for row in self.position)
    
    @property
    def empty_cells(self):
        return [
            (x, y)
            for x, row in enumerate(self.position)
            for y, cell in enumerate(row)
            if cell == " "
        ]

    
    def is_won(self, player):
        winning_combinations = [
            [[0, 0], [0, 1], [0, 2]],  # Ligne 1
            [[1, 0], [1, 1], [1, 2]],  # Ligne 2
            [[2, 0], [2, 1], [2, 2]],  # Ligne 3
            [[0, 0], [1, 0], [2, 0]],  # Colonne 1
            [[0, 1], [1, 1], [2, 1]],  # Colonne 2
            [[0, 2], [1, 2], [2, 2]],  # Colonne 3
            [[0, 0], [1, 1], [2, 2]],  # Diagonale principale
            [[0, 2], [1, 1], [2, 0]]   # Diagonale secondaire
        ]

        # Vérifie si une combinaison est gagnante
        return any(all(self.position[row][col] == player for row, col in combination)
                   for combination in winning_combinations)
    
    def make_random_move(self, player):
        if not self.empty_cells:
            return False  
        x, y = random.choice(self.empty_cells)
        self.position[x][y] = player
        return True
    
    def min_max(self, player):
        if self.is_won("O"):
            return  1
        
        if self.is_won("X"):
            return -1
        
        if not self.empty_cells:
            return 0
        
        if player == "O":
            best_score = float('-inf')
            for (x,y) in self.empty_cells:
                self.position[x][y] = player
                score = self.min_max("X")
                self.position[x][y] = " "
                best_score = max(score, best_score)
            return best_score
        else: 
            best_score = float('inf')
            for (x, y) in self.empty_cells:
                self.position[x][y] = player
                score = self.min_max("O")
                self.position[x][y] = " "
                best_score = min(score, best_score)
            return best_score
            
        
    def make_best_move(self, player):
        best_score = float("-inf")
        move = None
                 
        for (x, y) in self.empty_cells:
            self.position[x][y] = player
            score = self.min_max("X")
            self.position[x][y] = " "

            if score > best_score:
                best_score = score
                move = (x, y)
                
        if move:
            x, y = move
            self.position[x][y] = player
            return True
    



