from random import choice
import string
import pandas as pd

tamanho = 5 #Quantidade de caracteres existe na senha
valores = string.ascii_lowercase + string.digits
senha = ''
list = []


for _ in range(40):# QUANTIDADE DE SENHAS A SEREM CRIADAS
    for i in range(tamanho):
        senha += choice(valores)
    list.append(senha)
    senha =" "

    saida_excel = pd.DataFrame(list) 
print(saida_excel)

saida_excel.to_excel(r'C:\Users\ygorx\Documents\senha.xlsx', index=False)
