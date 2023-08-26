import socket
import threading

questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au"}
]


def handle_client(client_socket):
    client_socket.send(bytes("Welcome to the Quiz Game! Answer the questions.", "utf-8"))
    for question in questions:
        client_socket.send(bytes(question["question"] + "\n", "utf-8"))

        client_answer = client_socket.recv(1024).decode().strip()

        
        if client_answer.lower() == question["answer"].lower():
            client_socket.send(bytes("Correct!\n", "utf-8"))
        else:
            client_socket.send(bytes("Incorrect!\n", "utf-8"))

    client_socket.close()
def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   
    host = "localhost"
    port = 1234

    
    server_socket.bind((host, port))

    
    server_socket.listen(5)
    print("Server started on {}:{}".format(host, port))

    while True:
        
        client_socket, address = server_socket.accept()
        print("New client connected: {}".format(address))

       
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()
