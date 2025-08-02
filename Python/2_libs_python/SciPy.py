from scipy import constants

# usa o numpy por baixo e foca em ciencia de dados

# print(constants.liter) # 1L em metro cubico
# print(constants.pi)
# print(dir(constants)) # lista todas

# raiz quadrada equações
from scipy.optimize import root
from math import cos

# def eqn(x):
#   return x + cos(x)

# myroot = root(eqn, 0) # o 0 é o chute inicial para resovler a equação

# print(myroot.x)


# encontrar o ponto minimo de uma curva
from scipy.optimize import minimize

def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS') # varios outros métodos

print(mymin)