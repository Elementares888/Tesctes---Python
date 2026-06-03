# Biblioteca math


from math import pi
from math import tau, e

print(pi)
print(tau, e)


# Definição da função antes de ser usada
def obtem_rodape():
    return "Programação Estruturada e Orientada a Objetos em Python"


# Rodapé será uma constante. Assim, seu valor não será alterado

rodape = "Programação Estruturada e Orientada a Objetos em Python"
print(rodape)

constante = obtem_rodape()
print(constante)
