class LambdaTerm:
    def __init__(self, term):
        self.term = term
    
    def de_bruijn(self, term=None, bound_vars=None):
        if bound_vars is None:
            bound_vars = []
        if term is None:
            term = self.term

        if isinstance(term, str):
            # If the variable is found in the list of bound variables, return the De Bruijn index
            if term in bound_vars:
                return str(len(bound_vars) - bound_vars.index(term))
            else:
                return term
        elif isinstance(term, tuple):
            operator = term[0]
            if operator == 'λ':
                # Handle lambda abstraction
                bound_var = term[1]
                body = term[2]
                return f"λ{self.de_bruijn(body, bound_vars + [bound_var])}"
            else:
                # Handle function application
                left = self.de_bruijn(term[0], bound_vars)
                right = self.de_bruijn(term[1], bound_vars)
                return f"({left}{right})"
    
    def __str__(self):
        return self.de_bruijn()

# Test cases as nested tuples
terms = [
    ('λ', 'x', ('λ', 'z', ('x', 'z'))),  # λxz.xz should output λλ21
    ('λ', 'x', ('λ', 'y', ('x', 'y'))),  # λxy.xy should output λλ21
    (('x', 'z'), ('λ', 'x', ('λ', 'y', ('x', 'y'))))  # xz(λxy.xy) should output xz(λλ21)
]

for term in terms:
    l = LambdaTerm(term)
    print(l)  # Converts and prints De Bruijn index representation
