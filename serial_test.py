from sys import argv,exit
from serial import Serial,SerialException
if ((len(argv)<2) or (argv[1]=='?') or (argv[1]=='--help')): 
  print "---usage: python "+argv[0]+" port"
  exit()
stop = False
read = False
msg = ""
bd = [115200,9600,1200]
fr = ord('0')
to = ord('z') + 1
for i in range(fr,to):
	msg = msg + chr(i)
def clean(s):
  s.flushInput()
  s.flushOutput()
try:
  ser = Serial('/dev/'+argv[1], timeout=0.5)
  for i in range(3):
    ser.baudrate = bd[i]
    print "\nAt baudrate %s:\n Writing: %s" %(bd[i],msg)
    ser.write(msg)
    read = ser.read(to-fr)
    if (read != msg):
      print "\nError in loopback, check hardware connection, jumper terminals 2 & 3 and repeat the test\n"
      clean(ser)
      exit()
    else: print " Reading: %s" %read
  print "\nLoopBack Test Done Successfully\n" 
  clean(ser)
except SerialException:
  print argv[1],": port does not exist"
  exit()