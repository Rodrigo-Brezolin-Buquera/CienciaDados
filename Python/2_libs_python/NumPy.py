# serve para manipular arrays de forma mais rápida que a list nativa 
import numpy as np

arr = np.array([1, 2, 3, 4, 5]) #1D

arr = np.array([[1, 2, 3], [4, 5, 6]]) #2D

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) #3D

# print(arr.ndim) # num de dimensões
# print(arr)

arr = np.array([1, 2, 3, 4], ndmin=5) # definindo manualmente
# print(arr)
# print('number of dimensions :', arr.ndim)


# divindo arrays

arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[4:]) # index 4 pra frente
# print(arr[:4]) # até o index 4
# print(arr[::2]) # pulando de 2 em 2
# print(arr[1:5:2]) # 1 até 5 indo de 2 em 2

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1, 1:4]) # do segundo, retorna index 1 a 4 
# print(arr[0:2, 2]) # das 2, retorna o index 2

# tipos

arr = np.array([1, 2, 3, 4])

# print(arr.dtype) # verificar tipo

arr = np.array([1, 2, 3, 4], dtype='S') # define tipo

# print(arr)
# print(arr.dtype)

newarr = arr.astype(int) # converte

# Copy e View

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy() # faz cpóia independente
arr[0] = 42

# print(arr)
# print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view() # faz uma nova view, mas o array é o mesmo
arr[0] = 42

# print(arr)
# print(x)

# formatos

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# print(arr.shape) # estrutura da matriz

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3) # faz 4 arrays com 3 itens

# print(newarr)

newarr = arr.reshape(2, 3, 2) # a ultima dimensão tera 3 arrays com 2 itens

# print(newarr)

# interação -> usar for

# JUNTAR
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1) # junta nas mesmas dimensoes
# print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1) # index com index
# print(arr)

arr = np.hstack((arr1, arr2)) # na linha
# print(arr)

arr = np.vstack((arr1, arr2)) # na coluna
# print(arr)

# DIVIDIR

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3) # divide em 3 arrays iguais

# print(newarr)

# BUSCAR
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4) # buscar linear, retorna os indices
# print(x)

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7) # buscar binaria, retorna os indices

# print(x)

# ORDENAÇÂO
arr = np.array([3, 2, 0, 1])
# print(np.sort(arr))  

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42 # condicao

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)