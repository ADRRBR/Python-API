from Classes.BAS_Generico import *

link = 'http://localhost:5000/ADRRBR/clientes/consultanome/'

#conteudoPesquisar = None
conteudoPesquisar = 'G'

if conteudoPesquisar != None:
    link += conteudoPesquisar

retorno = requests.get(link)
print(retorno)
retorno = retorno.json()
print(retorno)

