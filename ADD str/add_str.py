class string:
    def __init__(self, value):
        if not all(c.isalpha() for c in value):
            raise ValueError("Tous les caractères doivent être des lettres alphabétiques.")
        self.value = value.lower()
        # Pas besoin de boucler sur les caractères, la méthode isalpha() le fait déjà
        if not value.isalpha():
            raise ValueError("Tous les caractères doivent être des lettres alphabétiques.")

    def __add__(self, other):
        if isinstance(other, string):
            if len(self.value) != len(other.value):
                raise ValueError("Les chaînes doivent avoir la même longueur pour être additionnées.")
            
            result = ""

            # A priori une string aura forcément value.isalpha() étant donné que la vérification est dans l'init.
            if self.value.isalpha() and other.value.isalpha():
                for char1, char2 in zip(self.value, other.value):
                    new_char = (ord(char1) - ord('a') + ord(char2) - ord('a')) + 1 % 26 + ord('a')
                    print(ord('a'))
                    print((ord(char1) - ord('a') + ord(char2) - ord('a')) % 26 + ord('a'))
                    if new_char > 122:
                        new_char = 97             
                        result += chr(new_char)
                    else:
                        result += chr(new_char)
                                          
            return string(result)
        return NotImplemented  # On aura tendance à raise les erreurs au lieu de les retourner.

        # Dans les cas comme ca, il est souvent préférable de faire de "l'early return"
        # On vérifie d'abord les cas qui nous font sortir de l'implémentation "normale"
        if not isinstance(other, string):
            raise NotImplemented
        if not len(self.value) == len(other.value):
            raise ValueError("Les deux chaînes doivent avoir la même longueur.")

        # Puis la logique de la fonction dans le cas "normal" se retrouve non indentée
        result = ""
        for char1, char2 in zip(self.value, other.value):
            ...
        return result

    def __str__(self):
        return self.value

if __name__ == "__main__":
    A = string("a")
    B = string("b")
    C = A + B
    print(f"{A} + {B} = {C}")

    Z = string("z")
    D = Z + A
    print(f"{Z} + {A} = {D}")

    E = string("abc")
    F = string("abc")
    G = E + F
    print(f"{E} + {F} = {G}")

