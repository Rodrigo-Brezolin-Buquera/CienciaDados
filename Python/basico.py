#Declaração variáveis
num1 = 1
num2 = 2.5
text = "texto"
bol = False

# Imprimir valor
print("Aparece no console")

# Tipos
type(num1)
type(num2)
type(text)
type(bol)

# Conversão para outros tipos
int(num1)
str(num1)
float(num1)

# Operações matemáticas e concatenação de strings
num2 - num1
num2 + num1
num2 * num1
num2 / num1

text + " concatenado "

# Operações Lógicas
not bol #inverte valor
num2 > num1 #maior/menor
num2 <= num1 #maior/menor igual
num2 != num1 #diferente
num2 == num1 # igual
num2 == 1 and num1 == 1 # e
num2 == 1 or num1 == 1 # ou


# Condicionais
if (text == "texto"):
  print("é verdade a condição")
elif (num1 == 1):
  print("a primeira é falsa, a segunda é verdadeira")
else:
  print("as duas eram falsas, vem nessa depois de testar as outras")

# Loops
for i in range(5):
  print(i)
for i in range(2,5):  #  começa no 2
  print(i)
for i in range(10,0,-1):  # começa no 10, para no zero e decresce em 1
  print(i)

count = 0 #contador
while count < 5:
    print(count)
    count += 1 #incrementa 1 no contador

# Aprofundamento em loops
for i in range(10):
    if (i == 6):
      continue # pula essa interação
    if (i == 9):
      break # encerra o loop

# Funções

def nome_funcao(num1, num2):  # Declaração com os parametros (num1, num2)

  media = (num1+num2)/2       # Escopo da função

  return media                # Retorno da função

nome_funcao(5, 10) # Chamando/utilizando a função

def nome_funcao2(num1, num2): # Funções com mais de 1 retorno
  return int(num1), str(num2)

primeiro, segundo = nome_funcao2(5, 10) # Acessando os retornos
print(primeiro)
print(segundo)

# Entrado de dados

texto = input()  # entrada de dados pelo usuário

# Erros e bloco try/except

print("Entre com um número")
try:
  valor = int(input())
  if(valor > 100):
    raise Exception("entre com um número menor que 100")
  print(valor*2)
except: # ou except Exception as err:  para acessar o erro em si
  print("não foi digitado um número")

# Vetores(Arrays)
vetor = [1, "abc", True] # Declaração
vetor[0]                 # Acessando o primeiro item (0)
vetor[1]                 # Acessando o segundo item (1)

len(vetor)               # Retorna o comprimento do array

for i in range(len(vetor)):
  print(vetor[i])
# ou simplficando
for i in vetor:
    print(i)

# Alterando valores:
vetor[0] = "novo valor"
vetor[1], vetor[2] = "alterando", "mais de um item"

# adiciona um novo item no array ao final
vetor.append("novo item")

# remove último item do array
vetor.pop()

#  função de número aleatório entre 1 e 100
import random
print(random.randint(1,100))

# dicionario aka hashtable
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
print(dictionary['gato'])
dictionary.keys()
dictionary['swan'] = 'cygne'
del dictionary['cachorro']

# tupla
tuple = ("a", "b")
