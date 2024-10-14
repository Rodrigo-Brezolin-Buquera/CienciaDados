import re

# verificar padrão
telefone = "Meu número é 9333-456-7890."
padrao = r"\d{3}-\d{3}-\d{4}" # minimo de char
resultado = re.search(padrao, telefone)

if resultado:
    print("Número válido encontrado:", resultado.group())
else:
    print("Formato inválido.")


# substiruir padrão
texto = "Para mais informações, contate info@exemplo.com ou suporte@exemplo.com."
padrao = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
substituido = re.sub(padrao, "<e-mail ocultado>", texto)
print(substituido)

# encontrar todos
# Procurando todas as ocorrências de palavras em uma string
texto = "O preço é R$20. O desconto foi de 10%."
padrao = r'\b\w+\b'  # Corresponde a todas as palavras

resultado = re.findall(padrao, texto) # retorna string
print(resultado)

# char especiais

# Padrão para caracteres especiais (exclui letras, números e espaços)
padrao = r"[^\w\s]"
texto = "Olá, mundo! Isso custa R$50,00. #Python"
print(re.search(padrao, texto)) # true
print(re.findall(padrao, texto)) # array
