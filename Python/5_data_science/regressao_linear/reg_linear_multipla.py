import numpy as np
import pandas as pd

# # Pacotes gráficos
import matplotlib.pyplot as plt
import seaborn as sns
# from mpl_toolkits.mplot3d import Axes3D
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.animation
# %matplotlib widget

# # Pacotes de modelagem
import statsmodels.api as sm

df = pd.read_csv('./base_funcionarios_v3.csv',sep=',')
                  

# print(df.shape)
# print(df.head())

# gráficos

# fig, ((ax1,ax2)) = plt.subplots(1,2,sharey=True,figsize=(12,5))
# ax1.scatter(df['Anos_Educ_Superior'],
#             df['Salario']);
# m, b = np.polyfit(df['Anos_Educ_Superior'],
#                   df['Salario'], 1)
# ax1.plot(df['Anos_Educ_Superior'],
#          m*df['Anos_Educ_Superior'] + b);

# ax2.scatter(df['Tempo_Empresa'],
#             df['Salario']);
# m, b = np.polyfit(df['Tempo_Empresa'],
#                   df['Salario'], 1)
# ax2.plot(df['Tempo_Empresa'], 
#          m*df['Tempo_Empresa'] + b);

# plt.tight_layout()
# plt.show()

# Correlação Linear de Pearson
fig = plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), 
            cmap='RdBu_r',
            vmin=-1, vmax=1,
            annot=True);

# plt.title('Correlação entre variáveis')
# plt.tight_layout()
# plt.show()  # 👉 Isso faz o gráfico aparecer


# Gráfico de Dispersão 3D
# sns.set(style = "darkgrid")

# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')

# x = df['Anos_Educ_Superior']
# y = df['Tempo_Empresa']
# z = df['Salario']

# ax.set_xlabel("Anos Educação Superior")
# ax.set_ylabel("Tempo Empresa")
# ax.set_zlabel("Salário")

# ax.scatter(x, y, z)

# plt.show()


# Variável resposta
y = df['Salario']

# Variáveis explicativas
df['intercepto'] = 1 
x = df[['intercepto',
        'Anos_Educ_Superior',
        'Tempo_Empresa']]

# Ajusta o modelo e retorna os resultados
modelo = sm.OLS(y , x)
resultado = modelo.fit()

print(resultado.summary())