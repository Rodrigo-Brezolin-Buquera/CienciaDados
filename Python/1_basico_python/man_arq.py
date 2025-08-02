# txt

texto = open("Python/arquivos/texto.txt", "a")
# 'r': modo de leitura, o arquivo deve existir previamente
# 'w': modo de escrita, se o arquivo não existir, ele será criado
# 'a': modo de anexar, adiciona informações ao final do arquivo
# 'x': modo exclusivo, cria um novo arquivo somente se ele não existir
# 'b': modo binário, usado para arquivos binários, como imagens ou vídeos
# 't': modo de texto, usado para arquivos de texto

texto.write("\n")
texto.write("Escrevendo algo\n")
# print(texto.read()) # le inteiro
# print(texto.read(10)) # numero de chars

frases = list()

frases.append("TreinaWeb \n")
frases.append("Python \n")
frases.append("Arquivos \n")
frases.append("Django \n")

texto.writelines(frases)
texto.close() # para a edicao
leitura = open("Python/arquivos/texto.txt", "r")

# print(leitura.readlines()) # le tudo
# print(leitura.readlines(1)) # linha especifica

leitura.close()

# csv

import csv
#leitura
with open("Python/arquivos/tabela.csv", "r") as tabela:
    leitor = csv.reader(tabela)
    next(leitor)  # pula a primeira linha (cabeçalho)
    for linha in leitor:
        print(linha)

#escrita
dados = [
    ['Nome', 'Idade', 'País'],
    ['João', '25', 'Brasil'],
    ['Maria', '30', 'Portugal'],
    ['José', '35', 'Espanha']
]

with open("Python/arquivos/escrita.csv", 'w', newline='') as arquivo:
    escritor_csv = csv.writer(arquivo)
    for linha in dados:
        escritor_csv.writerow(linha)


#json

import json

with open('Python/arquivos/json.json', 'r', encoding='utf-8') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)