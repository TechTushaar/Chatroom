import socket
import threading
import sys 
import argparse


#TODO: Implement a client that connects to your server to chat with other clients here


def commandline():
    parser = argparse.ArgumentParser(description= "server command line parser")
    parser.add_argument('-join', "--join",nargs='?', const= "join",help= "Argument 1")
    parser.add_argument('-port', "--port",  type= int, required= True, help= "Argument 2")
    parser.add_argument('-passcode', "--passcode",  type= str, required= True, help= "Max 5 letters")
    parser.add_argument('-host', "--host",  type= str, required= True, help= "Argument 2")
    parser.add_argument('-username', "--username",  type= str, required= True, help= "Argument 2")
    
    #add optional arguments
    args = parser.parse_args()
    
    if not args.port or not args.passcode or not args.host or not args.username:
        raise Exception("Please see usage")
    else :
        port = int(args.port)  
        password = str(args.passcode) #limit to 5?  
        username = str(args.username)
        host = str(args.host)
    
    return host, port, password, username


def chat_client():
    
    host, port, password, username = commandline()
 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try :
        client.connect((host, port))
    except :
        print('Unable to connect')
        sys.exit()
     
    print(f'Connected to {host} on port {port}')
    sys.stdout.flush()
    
    client.send(f'{username} joined the chatroom'.encode())
    
    # how to listen and send messages at same time using threading?
    thread = threading.Thread(target=receive_messages(client))
    thread.start()
    
    while True:
        msg = input('')
        client.send(msg.encode())
    

def receive_messages(client):
    while True:
        msg = client.recv(1024).decode()
        if msg:
            print(msg)


if __name__ == "__main__":
	sys.exit(chat_client())