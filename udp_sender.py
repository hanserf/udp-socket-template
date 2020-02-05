import socket
import sys
import logging
import time
# Create Logger / Log Handler
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
MESSAGE = "Hello, World! "

log.info("UDP target IP: {}".format(UDP_IP))
log.info("UDP target port: {}".format(UDP_PORT))
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
cntr = 0
while True:
    cntr += 1 
    msg = (MESSAGE + str(cntr)).encode('UTF-8')
    sock.sendto(msg, (UDP_IP, UDP_PORT))
    log.info("message: {}".format(msg.decode('UTF-8')))
    time.sleep(1)