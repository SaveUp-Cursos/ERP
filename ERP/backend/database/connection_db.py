import mysql.connector

class ConnectionDb:
    def __init__(self, host, user, password, database):
        self.db_config = {
            # Configurações do banco de dados
            'host': 'localhost',       # Host do banco de dados
            'user': 'root',            # Usuário do banco de dados
            'password': '@#Biel040921@#',  # Senha do banco de dados
            'database': 'app_db'       # Nome do banco de dados
        }
        self.connect()

    def connect(self):
        self.db = mysql.connector.connect(**self.db_config)
        self.cursor = self.db.cursor()

    def close(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'db') and self.db:
            self.db.close()

    def execute_query(self, query, data=None):
        try:
            self.cursor.execute(query, data)
            self.db.commit()
        except mysql.connector.Error as err:
            print(f"Erro no banco de dados: {err}")
            self.db.rollback()

# Exemplo de uso:
# connection = ConnectionDb('localhost', 'root', '@#Biel040921@#', 'app_db')
# connection.execute_query("INSERT INTO tabela (coluna) VALUES (%s)", ('valor',))
# connection.close()
