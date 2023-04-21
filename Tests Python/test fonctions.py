# example fonction mathematique
f = lambda x: x**2

print(f(3))

def e_potentielle(masse,hauteur,e_limite,g=9.81):
    E = masse * hauteur * g
    if(E >= e_limite):
        print(E, 'Joules', e_limite, 'WIN')
    else:
        print(E,e_limite, 'Wrong try again')
    return E

print('bonjour')
resultat = e_potentielle(masse=80,hauteur=5,e_limite=3258)