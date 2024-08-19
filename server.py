import socket

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor_socket.bind(('localhost', 12345))

# Colocando o servidor para escutar conexões
servidor_socket.listen(1)
print("Servidor esperando por conexões...")

# Aceitando a conexão do cliente
conexao, endereco = servidor_socket.accept()
print(f"Conexão estabelecida com {endereco}")
print("Bem-vindo ao Chat")
print("A primeira Mensagem e do cliente aguarde........")
while True:
# Recebendo a mensagem do cliente
    mensagem = conexao.recv(1024).decode()
    if mensagem:
        print(f"[{endereco[0]}]  Mensagem recebida:{mensagem}")
    else:
        pass
# Respondendo ao cliente
    mensagem=input("Digite sua mensagem:")
    if mensagem == '/sair':
        print("Você encerrou o Chat")
        mensagem = ("Conversa encerrada pelo servidor")
        conexao.send(mensagem.encode())
        conexao.close()
        servidor_socket.close()
        break
    print("Mensagem enviada ao cliente:")
    conexao.send(mensagem.encode())
