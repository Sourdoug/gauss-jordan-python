def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Fraction:
    def __init__(self, numerateur, denominateur):
        self.numerateur = numerateur
        self.denominateur = denominateur
        self.simplifier()
        
    def __add__(self, other):
        denominateur = self.denominateur * other.denominateur
        numerateur = self.numerateur * other.denominateur + other.numerateur * self.denominateur
        return Fraction(numerateur, denominateur)
    
    def __sub__(self, other):
        denominateur = self.denominateur * other.denominateur
        numerateur = self.numerateur * other.denominateur - other.numerateur * self.denominateur
        return Fraction(numerateur, denominateur)
    
    def __mul__(self, other):
        denominateur = self.denominateur * other.denominateur
        numerateur = self.numerateur * other.numerateur
        return Fraction(numerateur, denominateur)
    
    def __truediv__(self, other):
        denominateur = self.denominateur * other.numerateur
        numerateur = self.numerateur * other.denominateur
        return Fraction(numerateur, denominateur)
    
    def __str__(self):
        return f"{self.numerateur}/{self.denominateur}"
    
    def simplifier(self):
        diviseur = pgcd(self.numerateur, self.denominateur)
        self.numerateur //= diviseur
        self.denominateur //= diviseur

def gauss_jordan(A, b):
    n = len(A)
    m = len(A[0])
    for i in range(n):
        # Recherche du pivot
        pivot = None
        for j in range(i, n):
            if A[j][i] != 0:
                pivot = j
                break
        if pivot is None:
            # Le système n'a pas de solution unique
            return "Le système n'a pas de solution unique"
        # Échange de la ligne du pivot avec la ligne i
        A[i], A[pivot] = A[pivot], A[i]
        b[i], b[pivot] = b[pivot], b[i]
        # Normalisation de la ligne i
        diviseur = A[i][i]
        for j in range(m):
            A[i][j] /= diviseur
        b[i] /= diviseur
        # Élimination des autres termes de la colonne i
        for j in range(n):
            if j != i:
                facteur = A[j][i]
                for k in range(m):
                    A[j][k] -= facteur * A[i][k]
                b[j] -= facteur * b[i]
    # Vérification de la dernière ligne
    for j in range(m):
        if A[n-1][j] != 0:
            # Le système n'a pas de solution unique
            return "Le système n'a pas de solution unique"
    # Construction de la solution
    solution = [None] * n
    for i in range(n):
        solution[i] = b[i]
    return solution
