# Chat Room

This is a simple chat room application implemented in Python using socket programming. It allows multiple clients to connect to a server and communicate with each other in a chat room environment.

## Features

- Connection establishment and password checking
- Multiple clients can join the chat room
- Chat functionality with message broadcasting
- Support for shortcuts like :) and :(
- Clients can leave the chat room by typing :Exit

## Getting Started

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/chat-room.git
   ```

2. Change into the project directory:

   ```shell
   cd chat-room
   ```

3. Start the server:

   ```shell
   python3 server.py -start -port <port> -passcode <passcode>
   ```

4. Join the chat room as a client:

   ```shell
   python3 client.py -join -host <hostname> -port <port> -username <username> -passcode <passcode>
   ```

## Usage

- Upon successful connection, clients can type messages that will be displayed to all participants in the chat room.
- Clients can use shortcuts like :) and :( to display specific text.
- To leave the chat room, type :Exit.

## Notes

- The passcode is limited to a maximum of 5 alphanumeric characters.
- The display name is limited to a maximum of 8 characters.
- Messages longer than 100 characters will be truncated.
- The server maintains a persistent TCP connection with clients until they type :Exit.
- Replace `<port>`, `<passcode>`, `<hostname>`, and `<username>` with the appropriate values based on your setup.


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This project serves as a learning exercise in socket programming and text parsing.
