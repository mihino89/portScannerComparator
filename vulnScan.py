#!/usr/bin/python

import socket 
import os
import sys


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)

        return banner
    except:
        return


def checkVulns(banner, filename):
    f = open(filename, "r")
    for line in f.readlines():
        if line.strip("\n") in banner:
            print '[*] Server is vulnerable: ' + banner.strip("\n")

def main():
    #checking with sys library if i have correct arguments in input
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        #kontrola ci subor neexistuje pomocou lib os
        if not os.path.isfile(filename):
            print '[*] File doesnt exist!'
        if not os.access(filename, os.R_OK):
            print '[*] Access denied to the file'
            exit(0)
    else:
        print '[*] Usage: ' + str(sys.argv[0]) + ' <vuln fileName>'
        exit(0)

    portList = [21, 22, 25, 80, 110, 443, 445]
    
    #will change value of each ip in local network (max is <1,255>)) 
    for x in range(243,245):
        ip = "192.168.0." + str(x)
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print '[*] ' + ip + '/' + str(port) + ' : ' + banner
                checkVulns(banner, filename)

main()
