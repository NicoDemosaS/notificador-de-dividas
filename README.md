# Notificador de Dividas

## Descrição
O **Notificador de Dividas** é um software que utiliza SQLite e Selenium para gerenciar registros de dívidas, nomes e números de telefone de clientes. Ele permite o envio automático de mensagens para informar os clientes sobre suas dívidas.

## Como Utilizar

1. **Instalação:**
   - Baixe e instale as dependências listadas em `requirements.txt`:
     ```sh
     pip install -r requirements.txt
     ```

2. **Configuração:**
   - Execute o script `setup.py` para configurar o ambiente:
     ```sh
     python setup.py
     ```

3. **Uso:**
   - Escolha a opção 8 no terminal e siga as instruções para entrar no WhatsApp Web.
   - Adicione clientes com a opção 1 no terminal, fornecendo o nome e número de telefone.
   - Edite as dívidas usando as opções 3, 4 e 5 no terminal.
   - Ao editar uma dívida, a mensagem será enviada automaticamente com a ajuda do Selenium.

   **Nota:** Certifique-se de estar usando o Google Chrome.

## Melhorias Futuras

- Melhorar/criar a Interface Gráfica para uma melhor experiência do usuário.
- Criar uma aplicação web.
- Hospedar o serviço de envio de mensagens do Selenium.

