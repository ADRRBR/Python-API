from Classes.BAS_Generico import *

conteudoPesquisar = 'A'
link = f'http://localhost:5000/ADRRBR/clientes/consultanome/{conteudoPesquisar}'

retorno = requests.get(link)
print(retorno)
retorno = retorno.json()
print(retorno)

