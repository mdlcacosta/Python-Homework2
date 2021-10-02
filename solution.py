from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = '127.0.0.1'
    port = 1025
        # Create socket called clientSocket and establish a TCP connection with mailserver and port

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((mailserver, port))
    serverSocket.listen(1)
    while True:
        clientSocket, addr = serverSocket.accept()
        # Fill in end



        recv = clientSocket.recv(1024).decode()
            #print(recv)
             #if recv[:3] != '220':
            #print('220 reply not received from server.')

         # Send HELO command and print server response.
        # heloCommand = 'HELO Alice\r\n'
        clientSocket.send(heloCommand.encode())
        recv1 = clientSocket.recv(1024).decode()
             #print(recv1)
             #if recv1[:3] != '250':
     #   print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
        mailfromCommand = 'MAIL FROM: <mja99226@nyu.edu>\r\n'
        clientSocket.send(mailfromCommand.encode())
        recv2 = clientSocket.recv(1024).decode()
        #print (recv2)
        # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
        rcptToCommand = 'RCPT TO: <mja9926@nyu.edu>\r\n'
        clientSocket.send(rcptToCommand.encode())
        recv3 = clientSocket.recv(1024).decode()
        #print(recv3)
        # Fill in end

    # Send DATA command and print server response.
    # Fill in start
        dataCommand = 'DATA\r\n'
        clientSocket.send(dataCommand.encode())
        recv4 = clientSocket.recv(1024).decode()
        #print(recv4)
        # Fill in end

    # Send message data.
    # Fill in start
        clientSocket.send(msg.encode())
        recv5 = clientSocket.recv(1024).decode()
        #print(recv5)
        # Fill in end

    # Message ends with a single period.
    # Fill in start
        clientSocket.send(endmsg.encode())
        recv6 = clientSocket.recv(1024).decode()
        # print(recv6)
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
        quitCommand = 'QUIT\r\n'
        clientSocket.send(quitCommand.encode())
        recv7 = clientSocket.recv(1024).decode()
        # print(recv7)
    # Fill in end

    serverSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
