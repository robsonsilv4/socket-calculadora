import socket

host = 'localhost'
porta = 12003

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.connect((host, porta))

mensagem = str(input('Digite a operação e os números: '))
servidor.send(mensagem.encode())

resultado = servidor.recv(1024).decode()
print('Resultado da operação: ', resultado)

servidor.close()