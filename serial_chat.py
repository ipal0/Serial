import threading
from sys import argv,exit
from serial import Serial,SerialException
if ((len(argv)<3) or (argv[1]=='?') or (argv[1]=='--help')): 
  print "---usage: python "+argv[0]+" port baud"
  exit()
stop = False
msg = ""
def Write():
  global stop,msg,read
  while not stop:
    msg = raw_input()
    ser.write(msg)
    if (msg == "quit"):
      stop = True
      break
def Read():
  global stop,msg,read
  while not stop:
    i = ser.read(50)
    if i != "":  print "Received = %s" %i
try:
  ser = Serial('/dev/'+argv[1], argv[2], timeout=0.5)
except SerialException:
  print argv[1],": port does not exist"
  exit()
print "---To Quit the program type 'quit'"
threading.Thread(target = Write).start()
threading.Thread(target = Read).start()