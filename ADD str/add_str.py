class string:
    def __init__(self, value):
        if not all(c.isalpha() for c in value):
            raise ValueError("Tous les caractères doivent être des lettres alphabétiques.")
        self.value = value.lower()

    def __add__(self, other):
        if isinstance(other, string):
            if len(self.value) != len(other.value):
                raise ValueError("Les chaînes doivent avoir la même longueur pour être additionnées.")
            
            result = ""
            
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
        return NotImplemented

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

