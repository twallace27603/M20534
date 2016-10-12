#!/usr/bin/python3

import asyncore
import socket, sys, struct, os
import uuid
import datetime
from multiprocessing import Process, Pool

tcpPort = 8181

def wasteProcessor(endTime):
    lcv = 0
    now = datetime.datetime.now()
    while now < endTime:
        lcv = lcv + 1
        lcv = lcv % 100000
        now = datetime.datetime.now()

def getips():
    ips = []
    results = os.popen('ip addr | grep "inet " | grep -v "host"').read().strip().split("\n")
    for r in results:
        ips.append(r.split(" ")[1].split("/")[0])
    return ips
                       
def get_details():
    result = "IPv4 Addresses: "
    for ip in getips():
        result += ip + ";"
    result +=  "\n Computer Name: {}".format(socket.gethostname())
    return result

    

class TCPHandler(asyncore.dispatcher_with_send):
    def __init__(self,sock,addr):
        asyncore.dispatcher_with_send.__init__(self,sock)
        self.data = ""
        self.addr = addr[0]

    def handle_read(self):
        print("Receiving TCP data ...")
        data = self.recv(8192)
        message = "success"
        if data:
            data = data.decode()
            command = data[0]
            if command == '1':
                #Process echo
                message = get_details()
            else:
                #Process Ping
                message = "success"
            result = "Received {0} \n Processed {1}".format(command, message)
            self.sendall(result.encode())
        else:
            self.close()

class TCPServer(asyncore.dispatcher):
    def __init__(self):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', tcpPort))
        self.listen(5)
        print("TCP listening on port {}".format(tcpPort))

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print('Incoming connection from {}'.format(repr(addr)))
            handler = TCPHandler(sock, addr)



if __name__ == "__main__":
    
    tserver = TCPServer()

    asyncore.loop()
    print("Past loop")
