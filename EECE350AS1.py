import socket
import struct,time
import sys

def dprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("129.6.15.27",37))

dprint("Listening to IP address: 129.6.15.27\n\n")
time_since_1970 = 2208988800

t = mysock.recv(4)
t = struct.unpack("!I",t)[0]
t = int(t-time_since_1970)
final_time_1 = time.ctime(t)
final_time_1_l = final_time_1.split()
final_time_1 = final_time_1_l[3]
mysock.close()

dprint("NIST Server Time in IP address 129.6.15.27 is " + str(final_time_1) +"\n\n")
time.sleep(1)
mysock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock2.connect(("129.6.15.30",37))

dprint("Listening to IP address: 132.163.97.1\n\n")

t2 = mysock2.recv(4)
t2 = struct.unpack("!I",t2)[0]
t2 = int(t2-time_since_1970)
final_time_2 = time.ctime(t2)
final_time_2_l = final_time_2.split()
final_time_2 = final_time_2_l[3]
mysock.close()


dprint("NIST Server Time in IP address 132.163.97.1 is " + str(final_time_2)+'\n\n')


dprint("The two IP addresses are "+ str(abs(t2-t))+ " seconds apart\n\n")
