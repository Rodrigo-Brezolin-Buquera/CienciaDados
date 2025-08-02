array = [1, 5, 9, 10]
arr2 = [7, 1, 2, 0]

tupleA = ("a", "b")
tupleB = ("c", "d")

#  MAP
def sum10(n):
    return n +10
result = map(sum10, array) 
# print(list(result))
def sum(a,b):
    return a + b
res = map(sum, array, arr2)
# print(list(res))

# Filter
def fil(n):
    if(n>5): return True
    else: return False
filRes = filter(fil, array)
# print(list(filRes))

# enumerate => cria lista com objetos contendo os index e os valores / serve para dicionários também
en = enumerate(arr2)
# print(list(en))

# ZIP => junta 2 ou mais dentro de um array -> não junta 2 em 1, para concatenar é só somar os arrays
z1 = zip(tupleA, tupleB)
z2 = zip(array, arr2)
# print(list(z1), list(z2))

# Reduce
# operação acumulativa em uma sequência de dados 

from functools import reduce

def multiply(x, y):
    return x * y

result = reduce(multiply, array)
# ou
result1 = reduce(lambda x, y: x * y, array)

print(result1) 