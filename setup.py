import os
from main import Clientes
from whatzapchrome import *

def iniciar_whatssap():
    # seleniumstuff();
    # Open the web whatssap browser
    # Wait for registration
    # Ok message

    return abrir_chrome()

def setup():
    os.system('cls')
    print('Iniciando Programa!')
    print('-=-'*10)
    print('1 - Inserir Cliente')
    print('2 - Deletar Cliente')
    print('3 - Aumenta Divida')
    print('4 - Diminuir Divida')
    print('5 - Zerar Divida')
    print('6 - Mostrar Inf de um Cliente')
    print('7 - Mostrar Database')
    print('8 - Teste Selenium')
    print("-=-"*10)

    opcao = int(input('Escolha: '))
    if opcao == 1:
        inserir_cliente()
    elif opcao == 2:
        deletar_cliente()
    elif opcao == 3:
        adicionar_divida()
    elif opcao == 4:
        diminuir_divida()
    elif opcao == 5:
        zerar_divida()
    elif opcao == 6:
        mostrar_cliente()
    elif opcao == 7:
        mostrar_todos_clientes()
    elif opcao == 8:
        driver = abrir_chrome()
        esperar_login(driver)
        pass

def inserir_cliente():  # Opçao 1
    # Add client to the database
    # Add Name and Number
    
    # Verify the name
    name = input('nome a adicionar:')
    
    # Verify Number
    number = input(f'numero a adicionar a {name}:')
    
    cliente = Clientes(name, number)
    Clientes.inserir_cliente_db(cliente)
    
    print(f'Inserindo Cliente: {name} com numero {number} ao Banco de Dados')
    input('CONFIRMAR: ')
    
    setup()

def deletar_cliente(): # Opçao 2
    # Delete Cliente from the Database
    
    # Verify if the name actual exists in the Database
    name = input('Cliente a Deletar: ')
    print(f'Deletando Cliente: {name} do Banco de Dados')
    
    Clientes.deletar_cliente(name)
    
    input('Confirmar: ')
    setup()

def adicionar_divida(): # Opçao 3
    # Add a debt to the Client
    # Send a Message to the client

    # Verify if is the actual person u want to add debt
    name = input('Nome do Cliente: ')
    divida = int(input('Divida a aumentar: '))
    print(f'Adicionando divida de: {divida} ao Cliente: {name}')
    Clientes.aumentar_divida(name, divida)

    # Send a message to client warning about the new debt
    input('Confirmar: ')
    setup()

def diminuir_divida(): # Opçao 4
    # Remove debt from the client
    # Send a Message to the client

    # Verify if is the actual person u want to remove debt
    name = input('Nome do Cliente: ')
    dividapaga = int(input('Divida Paga: '))
    print(f'Diminuindo divida: {dividapaga} do Cliente: {name}')
    Clientes.diminuir_divida(name, dividapaga)

    input('Confirmar: ')
    setup()

def zerar_divida(): # Opçao 5
    # Remove all debt from the client
    # Send message to the client
    name = input('Nome do Cliente: ')
    print(f'Zerando divida do Cliente: {name}')
    Clientes.zerar_divida(name)

    input('Confirmar: ')
    setup()

def mostrar_cliente(): # Opçao 6
    # Show inf about one Client
    name = input('Nome do Cliente: ')
    print(f'Mostrando Informaçoes do Cliente: {name}')
    Clientes.mostrar_um_cliente(name)
    
    
    input('Confirmar: ')
    setup()

def mostrar_todos_clientes(): # Opçao 7
    # Show all the clients
    print('Mostrando dados do Banco de Dados')
    Clientes.mostrar_db()

    input('Confirmar: ')
    setup()

if __name__ == '__main__':
    setup()