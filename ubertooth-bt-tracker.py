#!/usr/bin/python3

import subprocess
import re
import os, sys
import time, threading
import datetime
from gps3 import agps3

# Print Banner
print('')
print('              kNXK0OOOkkOOO0KXNk                 ')
print('           dNX0OOkkkkkkkkkkkkkkkkOO0XNd          ')  
print('        ;N0OkkkkkkkkkkdokkkkkkkkkkkkkkO0N:       ') 
print('      ,XOkkkkkkkkkkkkkx  okkkkkkkkkkkkkkkOX;     ')  
print('     OOkkkkkkkkkkkkkkkx    ckkkkkkkkkkkkkkkO0    ')  
print('    XOkkkkkkkkkkkkkkkkx      :kkkkkkkkkkkkkkOX   ')  
print('   0kkkkkkkkkkkkkkkkkkx        ;kkkkkkkkkkkkkkK  ')  
print('  dOkkkkkkkkkkkkkkkkkkx          ,kkkkkkkkkkkkkd ')  
print(' .Okkkkkkkkkkkkkkkkkkkx    .o       kkkkkkkkkkkO' ) 
print(' xkkkkkkkkkd  ;kkkkkkkx    .OKd      .kkkkkkkkkkx') 
print(' Okkkkkkko      ,kkkkkx    .kkOKx      .kkkkkkkkO')
print(';kkkkkkkkOXo       kkkx    .kkkk       NOkkkkkkkk')
print('okkkkkkkkkkOKx      .kx    .kx       N0kkkkkkkkkk')
print('xkkkkkkkkkkkkOKk                  .N0kkkkkkkkkkkk')
print('kkkkkkkkkkkkkkkOKO              .N0kkkkkkkkkkkkkk')
print('     u b e r t o o t h         o n e             ')
print('kkkkkkkkkkkkkkkkkkkOKx      .XOkkkkkkkkkkkkkkkkkk')
print('kkkkkkkkkkkkkkkkkkkc           kkkkkkkkkkkkkkkkkk')
print('kkkkkkkkkkkkkkkkk:               kkkkkkkkkkkkkkkk')
print('dkkkkkkkkkkkkkk;           .       xkkkkkkkkkkkkk')
print('lkkkkkkkkkkkk,      lXx    .0N.      dkkkkkkkkkkk')
print(',kkkkkkkkkk       dKOkx    .kk0N.      dkkkkkkkkk')
print(' kkkkkkkkk      xKOkkkx    .kkkk;      cOkkkkkkkk') 
print(' lkkkkkkkk0N  kKOkkkkkx    .kk       lXOkkkkkkkkl') 
print(' .kkkkkkkkkk0KOkkkkkkkx    ..      dKOkkkkkkkkkk.') 
print('  :kkkkkkkkkkkkkkkkkkkx          xKOkkkkkkkkkkkc ') 
print('      b l u e t o o t h           t r a c k e r  ') 
print('    xkkkkkkkkkkkkkkkkkx      0KOkkkkkkkkkkkkkd   ') 
print('     lkkkkkkkkkkkkkkkkx    KKOkkkkkkkkkkkkkkl    ') 
print('      .kkkkkkkkkkkkkkkx  N0Okkkkkkkkkkkkkkk.     ') 
print('         kkkkkkkkkkkkkxN0kkkkkkkkkkkkkkkk.       ') 
print('           .kkkkkkkkkkOkkkkkkkkkkkkkkk.          ') 
print('                 dkkkkkkkkkkkkkkd                ')
print('')

gpsd_socket = agps3.GPSDSocket()
data_stream = agps3.DataStream()
gpsd_socket.connect()
gpsd_socket.watch()

def trackBT():
    print("Start bluetooth discovering")
    basename = "mylogfile"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([basename, suffix])
    myfile = open(filename,"w")

    while 1:
        try:
            print("new scan")
            p = subprocess.Popen(["ubertooth-scan", "-U 0 -b hci0 -x -t 40"],shell=True,stdout=subprocess.PIPE)
            out = p.stdout.read()
            for line in out.decode().split("\n"):
                print(line)
                try:
                    regObj = re.search(r'(\sLAP\=(.*?)\s)(.*)(\ss\=(.*?)\s)', line)
                    lap = regObj.group(2)
                    s = regObj.group(5)
                    s_num = re.sub(r'(?i)\-+','',s)
                    n = int(s_num)
                    if lap is not None and n < 65:
                        print("found a close BT device")
                        print('MAC = ', lap)
                        print('Signal =', s)
                        print('signal num =', s_num)
                        for new_data in gpsd_socket:
                            if new_data:
                                data_stream.unpack(new_data)
                                if data_stream.lon != 'n/a' and  data_stream.lat != 'n/a':
                                    longitude = data_stream.lon
                                    latitude = data_stream.lat
                                    print('Longitudine = ', data_stream.lon)
                                    print('Latitude = ', data_stream.lat)
                                    break
                        t = input("Enter track note:")
                        print("log data into file")
                        myfile.write("MAC: " + str(lap))
                        myfile.write(" Signal " + str(s))
                        myfile.write(" LONG: " + str(longitude))
                        myfile.write(" LAT: " + str(latitude))
                        myfile.write(" Note: " + str(t))
                        myfile.write("\n\n")
                except AttributeError:
                    print('')

        except KeyboardInterrupt:
            myfile.close()
            os.system("ubertooth-util -r")
            sys.exit("quit scan")

trackBT()
