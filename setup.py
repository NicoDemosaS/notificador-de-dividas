import os
from sqlfunction import SqlLite
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
    print('8 - Logar Chrome')
    # print('9 - Enviar Mensagem Teste')
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
        global driver
        driver = abrir_chrome()
        esperar_login(driver)
        setup()
    #elif opcao == 9:
    #    nome = 'Gab'
    #    numero = '45999232799'
    #    divida = 500
    #    mensagem = f'{nome} voce tem uma dividade de {divida}'

        #mandar_mensagem(driver, numero, mensagem)
        
        #setup()

def inserir_cliente():  # Opçao 1
    # Add client to the database
    # Add Name and Number
    
    # Verify the name
    name = input('nome a adicionar:')
    
    # Verify Number
    number = input(f'numero a adicionar a {name}:')
    
    # Create a new client
    cliente = SqlLite(name, number)
    SqlLite.inserir_cliente_db(cliente)
    
    # Terminal Message
    print(f'Inserindo Cliente: {name} com numero {number} ao Banco de Dados')
    input('CONFIRMAR: ')
    
    setup()

def deletar_cliente(): # Opçao 2
    # Delete Cliente from the Database
    
    # Verify if the name actual exists in the Database
    name = input('Cliente a Deletar: ')
    print(f'Deletando Cliente: {name} do Banco de Dados')
    
    SqlLite.deletar_cliente(name)
    
    input('Confirmar: ')
    setup()

def adicionar_divida(): # Opçao 3
    # Add a debt to the Client
    # Send a Message to the client

    # Verify if is the actual person u want to add debt
    name = input('Nome do Cliente: ')
    divida = int(input('Divida a aumentar: '))
    print(f'Adicionando divida de: {divida} ao Cliente: {name}')
    SqlLite.aumentar_divida(name, divida)



    # Send message about new debt
    numero = SqlLite.mostrar_inf(name, "numero")
    nova_divida = SqlLite.mostrar_inf(name, "divida")
    mensagem = f'{name} foi adicionado R${divida} a sua conta, sua nova divida é de R${nova_divida}'
    
    mandar_mensagem(driver, numero, mensagem)

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
    SqlLite.diminuir_divida(name, dividapaga)

    #Send message about the debt
    numero = SqlLite.mostrar_inf(name, "numero")
    nova_divida = SqlLite.mostrar_inf(name, "divida")
    mensagem = f'{name} voce pagou R${dividapaga} sua nova divida é de {nova_divida}'
    mandar_mensagem(driver, numero, mensagem)

    input('Confirmar: ')
    setup()

def zerar_divida(): # Opçao 5
    # Remove all debt from the client
    # Send message to the client
    name = input('Nome do Cliente: ')
    print(f'Zerando divida do Cliente: {name}')
    SqlLite.zerar_divida(name)

    # Send message about the debt
    numero = SqlLite.mostrar_inf(name, "numero")
    nova_divida = SqlLite.mostrar_inf(name, "divida")
    mensagem = f'{name} voce pagou toda sua divida, sua nova divida é de {nova_divida}'
    mandar_mensagem(driver, numero, mensagem)

    input('Confirmar: ')
    setup()

def mostrar_cliente(): # Opçao 6
    # Show inf about one Client
    name = input('Nome do Cliente: ')
    print(f'Mostrando Informaçoes do Cliente: {name}')
    SqlLite.mostrar_um_cliente(name)
    
    
    input('Confirmar: ')
    setup()

def mostrar_todos_clientes(): # Opçao 7
    # Show all DB the clients
    print('Mostrando dados do Banco de Dados')
    SqlLite.mostrar_db()

    input('Confirmar: ')
    setup()

if __name__ == '__main__':
    setup()