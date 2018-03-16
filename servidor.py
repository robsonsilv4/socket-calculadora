import socket

def soma(a, b):
    temp = a + b
    return str(temp)

def sub(a, b):
    temp = a - b
    return str(temp)

def mult(a, b):
    temp = a * b
    return str(temp)

def div(a, b):
	if b == 0:
		return 0
	else:
		temp = a / b
		temp = int(temp)
		return str(temp)

host = ''
porta = 12003

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, porta))
servidor.listen(1)

print('O servidor está esperando uma operação e dois números...')

while True:
	conn, addr = servidor.accept()

	msg = conn.recv(1024).decode()
	op, a, b = msg.split()
	a = int(a)
	b = int(b)

	resultado = 0
	if op == 'soma':
	    resultado = soma(a, b)
	elif op == 'subtração':
	   	resultado = sub(a, b)
	elif op == 'multiplicação':
	    resultado = mult(a, b)
	elif op == 'divisão':
	    resultado = div(a, b)
	else:
	    print('Operação não permitida')
	
	conn.send(resultado.encode())
	conn.close()