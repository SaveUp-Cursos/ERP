# persons.py

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from ..database.connection_db import ConnectionDb

class MyRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        self.db_connection = ConnectionDb('localhost', 'root', '@#Biel040921@#', 'app_db')
        super().__init__(request, client_address, server)

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('/frontend/templates/index.html', 'rb') as file:
                self.wfile.write(file.read())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        params = parse_qs(post_data.decode('utf-8'))

        nome = params['nome'][0]
        cpf = params['cpf'][0]

        insert_query = "INSERT INTO pessoas (nome_pessoa, cpf_pessoa) VALUES (%s, %s)"
        self.db_connection.execute_query(insert_query, (nome, cpf))

        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()

    def finish(self):
        super().finish()
        self.db_connection.close()

# Função para executar o servidor
def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}')
    httpd.serve_forever()

    # Junior Grecco
