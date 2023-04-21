# example fonction mathematique
f = lambda x: x**2

print(f(3))

# example declaration fonction
def e_potentielle(masse,hauteur,e_limite,g=9.81):
    E = masse * hauteur * g
    solution = False
    if(E >= e_limite):
        print(E, 'Joules', e_limite, 'WIN')
        solution = True
    else:
        print(E,e_limite, 'Wrong try again')
    return solution

print('bonjour')
print(e_potentielle(masse=80,hauteur=5,e_limite=3258))