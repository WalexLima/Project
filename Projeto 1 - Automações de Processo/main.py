### Importar Arquivos e Biblioteca
import pandas as pd

### Importar Base de Dados
email = pd.read_excel(r'Bases de Dados/Emails.xlsx')
lojas = pd.read_csv(r'Bases de Dados/Lojas.csv', encoding='latin1', sep=';')
vendas = pd.read_excel(r'Bases de Dados/Vendas.xlsx')

### Incluir o nome da loja em Vendas
vendas = vendas.merge(lojas, on="ID Loja")

### Obter todas as lojas
dicionario_array = {}
for loja in lojas['Loja']:
    dicionario_array[loja] = vendas.loc[vendas['Loja']==loja,:]
print(dicionario_array['Norte Shopping'])