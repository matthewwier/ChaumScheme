import getopt
import sys
import socket
import Utils


def client_function(server_host, server_port, server_public_key, message):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port))

    public_key = Utils.import_key(server_public_key)
    public_key_modulus = public_key.n
    rvalue = Utils.relatively_prime_to(public_key_modulus)
    blind_message = public_key.blind(message, rvalue)
    client.send(Utils.fill_text(str(blind_message)))
    signed_message = int(Utils.delete_equalities(client.recv(4096)))
    unblinded_value = public_key.unblind(signed_message, rvalue)
    print int(unblinded_value)


def main():
    try:
        opts = getopt.getopt(sys.argv[1:], 'o:p:K:M:')[0]
    except getopt.GetoptError:
        print '-o <server host> -p <server port> -K <server public key> -M <message>'
        sys.exit(2)

    for arg, val in opts:
        if arg == '-o':
            server_host = val
        if arg == '-p':
            server_port = int(val)
        if arg == '-K':
            server_public_key = val
        if arg == '-M':
            message = val

    client_function(server_host, server_port, server_public_key, message)


if __name__ == '__main__':
    main()
