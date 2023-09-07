from Classes.BAS_Generico import *

link = 'http://localhost:5000/ADRRBR/clientes/consultanome/'

#conteudoPesquisar = None
conteudoPesquisar = 'GUI'

if conteudoPesquisar != None:
    link += conteudoPesquisar

retorno = requests.get(link)
if str(retorno) != '<Response [200]>':
    sys.exit(f'A requisição falhou. {retorno}')

retorno = retorno.json()
status = retorno[[0][0]]
registros = retorno[[1][0]]

#print(registros['Registros:'])
#print(registros['Registros:'][0]['nome'])

#print(retorno[0]["Mensagem:"])
#print(retorno[0]["Quantidade:"])
#print(retorno[1]["Registros:"])
#print(retorno[1]["Registros:"][0]["nome"])

print()
print(f'Mensagem: {status["Mensagem:"]}')
print(f'Quantidade de registros encontrados: {status["Quantidade:"]}')
print()
print('****** Registros:')

for cliente in range(len(registros['Registros:'])):
    print('------------------------------------------')
    for chave, valor in registros['Registros:'][cliente].items():
        print(f'{str(chave)}: {valor}')




