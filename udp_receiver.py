import socket
import sys
import logging
log_level = logging.INFO
log = logging.getLogger()
log_handler = logging.StreamHandler(sys.stdout)
log_handler.setLevel(log_level)
log.setLevel(log_level)
log_format = '%(name)s - %(levelname)s - %(message)s'
log_formatter = logging.Formatter(log_format)
log_handler.setFormatter(log_formatter)
log.handlers = []
log.addHandler(log_handler)


UDP_IP = "127.0.0.1"
UDP_PORT = 5005
log.info("Starting UDP Receiver on {} , Port: {}".format(UDP_IP, UDP_PORT))

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
cntr = 0
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    cntr += 1
    msg = data.decode('UTF-8')
    log.info('#'*40)
    log.info("  INDEX: {}".format(cntr))
    log.info('#'*40)
    log.info("Message received from:{}".format(addr))
    log.info("  Message Content:{}: ".format(data))
