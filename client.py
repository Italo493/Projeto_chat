import socket
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
cliente_socket.connect(('localhost', 12345))
print("Bem-vindo ao Chat")
while True:
# Enviando uma mensagem ao servidor
    mensagem = input('Digite sua mensagem:')
    if mensagem == '/sair':
        print('Você encerrou a conversa')
        mensagem = ('O cliente saiu do chat')
        cliente_socket.send(mensagem.encode())
        cliente_socket.close()
        break
    print(f'Mensagem enviada ao servidor:{mensagem}')
    cliente_socket.send(mensagem.encode())
# Recebendo a resposta do servidor
    resposta = cliente_socket.recv(1024).decode()
    if resposta:
        servidor,_ = cliente_socket.getpeername()
        print(f"[{servidor}]  Resposta do servidor:{resposta}")
    else:
         pass