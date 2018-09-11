import funken
import time

## serial port to connect to
port = "COM6"

## initialize the main PyFunken object
pyf = funken.PyFunken([port], [57600])

## register devices on the selected com port
pyf.ser_conn[port].register_devices()
time.sleep(1)

## set pin 13 as output
pyf.send_command("PM 13 1\n", port, 1)

while True:
	## turn led on pin 13 on
	pyf.send_command("DW 13 1\n", port, 1)
	time.sleep(1)
	## turn led on pin 13 off
	pyf.send_command("DW 13 0\n", port, 1)
	time.sleep(1)
