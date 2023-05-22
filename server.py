import socket
import threading
import sys
import argparse


RECV_BUFFER = 1024
clients_socket_list = [] #contains server socket also
host = ''
server_port = 0
server_password = ''

def commandline():
    parser = argparse.ArgumentParser(description= "server command line parser")
    parser.add_argument('-start', "--start",nargs='?', const= "start",help= "Argument 1")
    parser.add_argument('-port', "--port",  type= int, required= True, help= "Argument 2")
    parser.add_argument('-passcode', "--passcode",  type= str, required= True, help= "Max 5 letters")
    
    #add optional arguments
    args = parser.parse_args()
    
    if args.port:
        port = int(args.port)
    else:
        raise Exception("Please see usage")
        
    if args.passcode:
        password = str(args.passcode) #limit to 5?
        #problem = not a classd var?
    else:
        raise Exception("Please see usage")
    
    return port, password

def chat_server():
    port, password = commandline()
    server_port = port
    server_password = password
    
    # create a socket object
	# AF_NET = address family ipv4
	# SOCK_STREM = connection oriented TCP protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#get local machine name
    HOST = socket.gethostname()
    print(HOST)
 
	#bind the socket to a host and a port
    server_socket.bind((HOST, port))
	
	#start listening for upto 10 connections
    server_socket.listen(10)
	
	#Required print statement
    print(f"Server started on port {port}. Accepting connections")
    sys.stdout.flush()
 
	#add server socket object to the list of readable connections
    clients_socket_list.append(server_socket)
    
    while True:
        conn, addr = server_socket.accept()

		#start a new thread to handle client
        thread = threading.Thread(target= handle_client, args= (conn, addr))
        thread.start()
	


def handle_client(conn, addr):
    
    # add check for username and password
    
    # send a welcome message to client
    # conn.send(f'Connected to {socket.gethostname()} on port {server_port}'.encode())
    
    clients_socket_list.append(conn) # store username as well? or does thread do it?
    
    #output on server - broadcasted on all clients and server 
    # need to broadcast this
    username = 'User'
    broadcast(conn, f'{username} joined the chatroom')
    
    while True:
        #might wanna add a try - except block here
        #recieve a message from the client
        msg = conn.recv(RECV_BUFFER)
        
        if msg:
            #recv a message, broadcast it
            broadcast(conn, f'{username}: ' + msg)
        else:
            #disconnected client
            clients_socket_list.remove(conn)
            conn.close()
            break
            

def broadcast(conn, message: str):
    for client in clients_socket_list:
        if client != conn:
            try:
                client.send(message.encode())
            except:
                #broken socket connection, removing from list ?? Maybe not req
                client.close()
                if client in clients_socket_list:
                    clients_socket_list.remove(client) 
            
	
	
if __name__ == "__main__":
    sys.exit(chat_server())

		
		