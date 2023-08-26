import socket
import threading

# Function to receive question from server
def receive_question(connection):
    question = connection.recv(1024).decode()
    return question

# Function to send answer to server
def send_answer(connection, answer):
    connection.send(answer.encode())

# Function to receive score from server
def receive_score(connection):
    score = connection.recv(1024).decode()
    return int(score)

# Function to set nickname for the game
def set_nickname(connection):
    nickname = input("Enter your nickname: ")
    connection.send(nickname.encode())

# Main function
def main():
    # Connect to the server
    host = 'localhost'  # Replace with the server IP address
    port = 12345  # Replace with the server port
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set nickname for the game
    set_nickname(connection)

    # Play the quiz game
    while True:
        question = receive_question(connection)
        print("Question:", question)
        answer = input("Your answer: ")
        send_answer(connection, answer)
        score = receive_score(connection)
        print("Your score:", score)

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != 'y':
            break

    # Close the connection
    connection.close()

if __name__ == '__main__':
    main()
