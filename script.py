# Importação das bibliotecas necessárias
import pandas as pd
import os


# indicação do diretório para encontrar os arquivos

diretorio = './diretorio/'

# Criação de array para armazenar os dados de cada planilha
dataframes = []

# Listar os arquivos no diretório
arquivos = os.listdir(diretorio)

# Loop através de cada arquivo na pasta
for arquivo in arquivos:
    if arquivo.endswith('.xls'):  # Verifica se o arquivo é uma planilha de Excel
        caminho_completo = os.path.join(diretorio, arquivo)
        
        # Leia o arquivo Excel em um DataFrame
        df = pd.read_excel(caminho_completo, skiprows=9) #Pule a quantidade de linhas necessárias para obter cabeçalho correto (no exemplo, pularam-se 9 linhas)
        
        # Adicione o DataFrame à lista
        dataframes.append(df)


# Agora, dataframes contém os DataFrames de todas as planilhas na pasta

# Criar duas variáveis para acumulação
entradaFinal = 0
saidaFinal = 0

# Exemplo de como acessar e trabalhar com os DataFrames
for i, df in enumerate(dataframes):
    # Calcular o total de entradas (soma dos números positivos)
    total_entradas = df[df['valor (R$)'] > 0]['valor (R$)'].sum()
    entradaFinal += total_entradas

    # Calcular o total de saídas (soma dos números negativos)
    total_saidas = df[df['valor (R$)'] < 0]['valor (R$)'].sum()
    saidaFinal += total_saidas
    
    print(f'DataFrame {i + 1}:')
    print(total_entradas) 
    print(total_saidas)

print("Entrada total:", entradaFinal)
print("Saída total:", saidaFinal)
