import sqlite3 as sql  #Importa o sqlite3 e o apelida como sql.

class TransactionObject():#Classe que representa transação com o banco de dados SQLite.
    database = "clientes.db"
    conn = None     #Objeto de conexão com o banco de dados SQLite.
    cur = None      #Objeto de cursor para executar comandos SQL.
    conected = False # Indicador do estado da conexão.
    
    def connect(self): #  conecta ao banco de dados SQLite. Inicializa conn e cur.
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected =True
        
    def disconnect(self): # desconecta do banco de dados SQLite, fechando a conexão.
        TransactionObject.conn.close()
        TransactionObject.connected = False
        
    def execute(self, sql, parms=None):#executa comandos SQL.Aceita parâmetros opcionais.
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False
        
    def fetchall(self): #retorna todas as linhas resultantes de uma consulta.
        return TransactionObject.cur.fetchall()

    def persist(self): #confirma (commit) as mudanças no banco de dados.
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False
'''
cria uma instância de TransactionObject, conecta ao banco de dados, 
cria uma tabela chamada "clientes" se ela não existir, persiste as mudanças
e desconecta.
'''        
def initDB(): 
    trans = TransactionObject() #'trans' referência de "TranssactionObject"
    trans.connect()
    
    trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY,"
                  "nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
    trans.persist() 
    trans.disconnect()
    
def insert(nome, sobrenome, email, cpf):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO clientes VALUES(NULL, ?,?,?,?)", (nome, sobrenome, email, cpf))
    trans.persist()
    trans.disconnect()
  
#conecta-se ao banco de dados, executa uma consulta SQL para selecionar todos os 
# registros da tabela "clientes", recupera todas as linhas resultantes e, em seguida, 
# desconecta-se do banco de dados antes de retornar as linhas.  
def view(): 
    trans = TransactionObject()
    trans.connect()
    trans.execute("select * from clientes")
    rows = trans.fetchall()
    trans.disconnect()
    return rows
#realiza uma busca na tabela "clientes" com base nos parâmetros fornecidos (nome, 
# sobrenome, email ou cpf). Cria uma instância de TransactionObject, conecta-se ao 
# banco de dados, executa uma consulta SQL parametrizada e retorna as linhas 
# resultantes após desconectar-se.
def search(nome="", sobrenome="", email="", cpf=""):
    trans = TransactionObject()
    trans.connect()
    
    trans.execute("SELECT * FROM  clientes WHERE nome=? or sobrenome=? or email=? or cpf=?",
                  (nome, sobrenome, email, cpf))
    rows = trans.fetchall()
    trans.disconnect()
    return rows
#exclui um registro da tabela "clientes" com o ID fornecido. Cria uma instância de 
# TransactionObject, conecta-se ao banco de dados, executa uma instrução SQL para
# excluir o registro com o ID específico, persiste as mudanças e desconecta-se.
def delete(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM clientes WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()
#atualiza um registro na tabela "clientes" com os valores fornecidos e o ID correspondente. 
#Cria uma instância de TransactionObject, conecta-se ao banco de dados, executa uma 
#instrução SQL de atualização, persiste as mudanças e desconecta-se.    
def update(id, nome, sobrenome, email, cpf):
    trans = TransactionObject()
    trans.connect()
    
    trans.execute("UPDATE clientes SET nome =? , sobrenome=?, email=?, cpf=? WHERE id =?",
                  (nome, sobrenome, email, cpf, id))
    trans.persist()
    trans.disconnect()
#initDB()é chamada para garantir que a tabela "clientes" seja criada no banco de dados 
# ao iniciar o programa.  
initDB()




        