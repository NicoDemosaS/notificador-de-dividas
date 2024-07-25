import sqlite3

def conectar_db():
    try:
        conn = sqlite3.connect('clientes.db')
        return conn, conn.cursor()

    except sqlite3.Error as erro:
        print(f'ERRO {erro}')
        return None, None

def desconectar_db(conn):
    if conn:
        conn.close()

class Clientes:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.divida = 0
    
    def __str__(self):
        return f'{self.nome} - {self.divida}'
    
    @classmethod
    def aumentar_divida(cls, cliente, divida):
        conn, cursor = conectar_db()
        try:

            cursor.execute(f"SELECT divida FROM clientes WHERE nome = '{cliente}'")
            divida_db = cursor.fetchone()

            nova_divida = divida_db[0] + divida
            cursor.execute(f"UPDATE clientes SET divida = {nova_divida} WHERE nome = '{cliente}';")

            conn.commit()
            conn.close()
        
        except sqlite3.Error as erro:
            print(f'ERRO {erro}')
        
        finally:
            desconectar_db(conn)
        
    @classmethod
    def diminuir_divida(cls, cliente, divida):
        conn, cursor = conectar_db()
        try:

            cursor.execute(f"SELECT divida FROM clientes WHERE nome = '{cliente}'")
            divida_db = cursor.fetchone()

            nova_divida = divida_db[0] - divida
            cursor.execute(f"UPDATE clientes SET divida = {nova_divida} WHERE nome = '{cliente}';")

            conn.commit()
            conn.close()
        
        except sqlite3.Error as erro:
            print(f'ERRO {erro}')
        
        finally:
            desconectar_db(conn)

        
    #Insere dados na DB
    def inserir_cliente_db(self):
        conn, cursor = conectar_db()
        try:

            # Usando '?' para passar parâmetros de forma segura e especificando os nomes das colunas
            cursor.execute('INSERT INTO clientes (nome, numero, divida) VALUES (?, ?, ?)', (self.nome, self.numero, self.divida))

            conn.commit()
            conn.close()
            print('Cliente adicionado com sucesso.')
        
        except sqlite3.Error as erro:
            print(f'Erro ao inserir cliente: {erro}')

        finally:
            desconectar_db(conn)
    
    def mostrar_db():
        conn, cursor = conectar_db()
        try:

            cursor.execute('SELECT * from clientes')
            clientes = cursor.fetchall()  # Recupera todos os registros da tabela 'clientes'

            for cliente in clientes:
                print(cliente)

            conn.close()
        
        except sqlite3.Error as erro:
            print(f'ERRO {erro}')
        
        finally:
            desconectar_db(conn)

    @classmethod
    def deletar_cliente(cls, nome):
        conn, cursor = conectar_db()
        try:

            cursor.execute('DELETE FROM clientes WHERE nome = ?', (nome,))

            conn.commit()
            conn.close()
        
            print(f'Cliente {nome} deletado com sucesso')

        except sqlite3.Error as erro:
            print(f'ERRO {erro}')
        
        finally:
           desconectar_db(conn)

    @classmethod
    def mostrar_um_cliente(cls, nome):
        conn, cursor = conectar_db()
        try:

            cursor.execute('SELECT * FROM clientes WHERE nome = ?', (nome,))
            cliente = cursor.fetchone()

            if cliente:
                print(f'Dados do cliente:')
                print(f'Nome: {cliente[1]}')  # Supondo que o nome está na primeira coluna
                print(f'Numero: {cliente[2]}')  # Supondo que outros dados estão na segunda coluna, e assim por diante
                print(f'Divida {cliente[3]}')
            else:
                print(f'Cliente {nome} não encontrado.')

            conn.commit()
            conn.close()
        

        except sqlite3.Error as erro:
            print(f'ERRO {erro}')
        
        finally:
           desconectar_db(conn)

    @classmethod
    def zerar_divida(cls, nome):
        try:
            conn, cursor = conectar_db()

            cursor.execute('UPDATE clientes SET divida = 0 WHERE nome = ?', (nome,))

            conn.commit()
            conn.close()

        except sqlite3.Error as erro:
            print(f'ERRO {erro}')
        
        finally:
            desconectar_db(conn)

if __name__ == '__main__':
    #criar = Clientes('Teste', 191920)
    #criar.inserir_cliente_db()
    Clientes.aumentar_divida('Teste', 10)
    #Clientes.deletar_cliente('Cliente')
    Clientes.mostrar_db()
    Clientes.zerar_divida('Teste')
    Clientes.mostrar_db()
