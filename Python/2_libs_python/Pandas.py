# limpar dados

import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

df = pd.DataFrame(mydataset) # faz um tabelinha

# print(df)
# print(df.loc[0]) # encontra linha


import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"]) # faz um serie

# print(myvar)

df = pd.read_csv('Python/libs/data.csv') 
# df = pd.read_json('data.json') 

# print(df)
# print(df.head(1)) # n numero de linhas iniciais
# print(df.tail()) # finais

new_df = df.dropna()  # retira as linhas com campos vazios
new_df.dropna(inplace = True) # remove linhas com valores null
new_df.fillna(0, inplace = True) # troca valores null por 0
new_df["Calories"].fillna(130, inplace = True) # apenas colunas especificas

df['Date'] = pd.to_datetime(df['Date']) # converte data

print(new_df.to_string())

df.loc[7, 'Duration'] = 45 # muda valores
# da pra fazer loop

df.drop(2, inplace = True) # remover


df.drop_duplicates(inplace = True) # remove duplicatas
