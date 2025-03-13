import mysql.connector
from mysql.connector import Error

class MySQLConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        """Estabelece a conexão com o banco de dados MySQL."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)  # 🔹 Adicionando dictionary=True
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
    
    def execute_query(self, query, params=None):
        """Executa uma consulta SQL (INSERT, UPDATE, DELETE)."""
        if self.connection and self.cursor:
            try:
                if params:
                    self.cursor.execute(query, params)
                else:
                    self.cursor.execute(query)
                self.connection.commit()  # Confirma a execução da consulta
            except Error as e:
                print(f"Erro ao executar consulta: {e}")
    
    def fetch_all(self, query, params=None):
        """Executa uma consulta SELECT e retorna todos os resultados como lista de dicionários."""
        if self.connection and self.cursor:
            try:
                if params:
                    self.cursor.execute(query, params)
                else:
                    self.cursor.execute(query)
                return self.cursor.fetchall()  # 🔹 Retorna os resultados como dicionário
            except Error as e:
                print(f"Erro ao buscar dados: {e}")
                return None
    
    def fetch_one(self, query, params=None):
        """Executa uma consulta SELECT e retorna um único resultado como dicionário."""
        if self.connection and self.cursor:
            try:
                if params:
                    self.cursor.execute(query, params)
                else:
                    self.cursor.execute(query)
                return self.cursor.fetchone()  # 🔹 Retorna um único resultado como dicionário
            except Error as e:
                print(f"Erro ao buscar dados: {e}")
                return None

    def close(self):
        """Fecha o cursor e a conexão com o banco de dados."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

# Exemplo de uso da classe:
if __name__ == "__main__":
    # Crie uma instância da classe de conexão
    db = MySQLConnection(
        host="localhost",      # Endereço do servidor MySQL
        user="root",           # Nome de usuário do MySQL
        password="sua_senha",  # Senha do usuário
        database="nome_do_banco"  # Nome do banco de dados
    )

    # Conectando ao banco de dados
    db.connect()

    # Executando uma consulta de inserção (INSERT)
    insert_query = "INSERT INTO sua_tabela (coluna1, coluna2) VALUES (%s, %s)"
    db.execute_query(insert_query, ('valor1', 'valor2'))

    # Executando uma consulta de seleção (SELECT)
    select_query = "SELECT * FROM sua_tabela"
    resultados = db.fetch_all(select_query)

    # 🔹 Agora cada 'resultado' será um dicionário
    if resultados:
        for resultado in resultados:
            print(resultado)  # Exibe os resultados como dicionários

    # Fechando a conexão
    db.close()
