from Classes.BAS_Generico import *
from Classes.BAS_Arquivo import *
from Classes.SIS_Conexao import clsConexaoBancoDados
from Classes.APL_Clientes import clsClientes

app = Flask(__name__)

# -------------------------------- ARQUIVOS DE LOG
def preparaLog():
    caminho = os.getcwd() + "\ ".strip()

    dt = dtm.now()
    dtf = dt.strftime('%Y%m%d_%H%M%S')
    arquivoLogExecucao = f'LogExecucao_{dtf}.log'

    logExec = CriaArquivo(caminho, arquivoLogExecucao)
    return logExec

def conectaBancoDados():
    conexao = clsConexaoBancoDados.ConexaoSQLServer()
    conexao.servidor = 'LAPTOP-NC2UQK3P\SQLEXPRESS'
    conexao.bancoDados = 'DB_T_PYTHON'
    conexao.conectaAutentWindows()
    return conexao

#-----------------------------------------------------------------------------------

@app.route('/ADRRBR/clientes/consultanome/<string:nome>',methods=['GET'])
def consultaClientesNome(nome=''):
    logExec = preparaLog()
    if not logExec:
        mensagem = {'Mensagem:': 'Arquivo de LOG: ' + caminho + arquivoLogExecucao}
        return jsonify(mensagem)

    conexao = conectaBancoDados()
    if conexao.status != StatusExecucao.Sucesso:
        mensagem = {'Mensagem:': conexao.mensagem}
        return jsonify(mensagem)

    if not conexao.conectado:
        mensagem = {'Mensagem:': 'Não foi possível conectar ao SQL Server.'}
        return jsonify(mensagem)

    clientes = clsClientes.Clientes()
    clientes.conexao = conexao

    sWhere   = ''

    if nome != '':
        sWhere = f"WHERE NOME LIKE '{nome}%'"

    clientes.consulta(sWhere,'')
    if clientes.status != StatusExecucao.Encontrado:
        mensagem = {'Mensagem:': clientes.mensagem}
        return jsonify(mensagem)

    RegistraLinhaArquivo(logExec, clientes.JSONClientes, True)

    return clientes.JSONClientes

app.run(port=5000,host='localhost',debug=True)

# --------------------------------

