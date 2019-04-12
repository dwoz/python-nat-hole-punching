import logging
import socket
import sys
from util import *

logger = logging.getLogger()
addresses = []


def main(host='0.0.0.0', port=9999):
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((host, port))
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        logger.info("connection from: %s", addr)
        addresses.append(addr)
        if len(addresses) >= 2:
            logger.info("server - send client info to: %s", addresses[0])
            sock.sendto(addr_to_msg(addresses[1]), addresses[0])
            logger.info("server - send client info to: %s", addresses[1])
            sock.sendto(addr_to_msg(addresses[0]), addresses[1])
            addresses.pop(1)
            addresses.pop(0)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    main(*addr_from_args(sys.argv))
