import pandas as pd

# df = pd.read_excel("Python/exer/dados.xlsx")
df = pd.read_excel("dados.xlsx")
# df.info()

# 1. 
df["tempo_atendimento"] = df["fim_atendimento"] - df["inicio_atendimento"]


q1 = df['tempo_atendimento'].quantile(.25)
q2 = df['tempo_atendimento'].quantile(.50)
q3 = df['tempo_atendimento'].quantile(.75)

print(q1, q2, q3)
# 18min

# 2. 

freq_turnos = df["turno"].value_counts().reset_index()
freq_turnos.columns = ["turno", "Freq. Absoluta"]
freq_turnos['Frequência Relativa']=freq_turnos['Freq. Absoluta']/freq_turnos['Freq. Absoluta'].sum()
# print(freq_turnos)
# noite, 42%

#3

df['Faixas TMA'] = pd.Series(pd.cut(df['tempo_atendimento'], 3,precision=0))

freq_TMA = df["Faixas TMA"].value_counts().reset_index()
freq_TMA.columns = ["Faixas TMA", "Freq. Absoluta"]
freq_TMA['Frequência Relativa']=freq_TMA['Freq. Absoluta']/freq_TMA['Freq. Absoluta'].sum()
freq_TMA.sort_values(by="Faixas TMA", inplace=True)
print(freq_TMA)

#4 

freq_conversao_atendimento  = df["conversao_atendimento"].value_counts().reset_index()
freq_conversao_atendimento .columns = ["conversao_atendimento", "Freq. Absoluta"]
freq_conversao_atendimento['Frequência Relativa']=freq_conversao_atendimento['Freq. Absoluta']/freq_conversao_atendimento['Freq. Absoluta'].sum()
print(freq_conversao_atendimento)

#5

freq_atendente_nome   = df["atendente_nome"].value_counts().reset_index()
freq_atendente_nome  .columns = ["atendente_nome", "Freq. Absoluta"]
freq_atendente_nome ['Frequência Relativa']=freq_atendente_nome ['Freq. Absoluta']/freq_atendente_nome ['Freq. Absoluta'].sum()
print(freq_atendente_nome )