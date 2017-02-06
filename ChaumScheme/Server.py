import getopt
import sys
import socket
import Utils


def server_function(server_port, server_private_key):
    server = socket.socket()
    server.bind(('localhost', server_port))
    server.listen(5)

    client, _ = server.accept()

    private_key = Utils.import_key(server_private_key)
    message_from_client = Utils.delete_equalities(client.recv(4096))
    blind_signature = private_key.sign(message_from_client, 18159)[0]
    client.send(Utils.fill_text(str(blind_signature)))
    client.close()


def main():
    try:
        opts = getopt.getopt(sys.argv[1:], 'p:S:')[0]
    except getopt.GetoptError:
        print '-p <server port> -S <server private key>'
        sys.exit(2)

    for arg, val in opts:
        if arg == '-p':
            server_port = int(val)
        if arg == '-S':
            server_private_key = val

    server_function(server_port, server_private_key)

if __name__ == '__main__':
    main()
