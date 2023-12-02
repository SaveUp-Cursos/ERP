# main.py

from backend.login.persons import MyRequestHandler, run
from backend.database.connection_db import ConnectionDb

def main():
    # Configuração da conexão com o banco de dados
    db_connection = ConnectionDb('localhost', 'root', '@#Biel040921@#', 'app_db')

    # Criação de uma instância da classe MyRequestHandler
    request_handler = MyRequestHandler

    # Inicialização do servidor
    run(handler_class=request_handler)

    # Fechamento adequado do banco de dados
    db_connection.close()

if __name__ == '__main__':
    main()
