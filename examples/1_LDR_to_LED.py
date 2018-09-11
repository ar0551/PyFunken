import funken
import time

## remap function
def remap(x, oMin, oMax, nMin, nMax):
	return (((x - oMin) * (nMax - nMin)) / (oMax - oMin)) + nMin


## serial port to connect to
port = "COM6"

## initialize the main PyFunken object
pyf = funken.PyFunken([port], [57600])
pyf.verbose = 0

## register devices on the selected com port
pyf.ser_conn[port].register_devices()
time.sleep(1)

## set pin 9 as output
pyf.send_command("PM 9 1\n", port, 1)

while True:
	## analog read on pin A0
	ldr_response = pyf.get_response("AR 0\n", "AR", port, 1)
	if ldr_response is not None:
		## parse and remap output
		ldr_value = int(ldr_response.split(" ")[1])
		led_value = 255 - int(remap(ldr_value, 100, 900, 0, 255))
		
		## analog write on pin 9
		pyf.send_command("AW 9 " + str(led_value) + "\n", port, 1)
		
		## console log
		print("ldr: %s led: %s"%(str(ldr_value), str(led_value)))
	time.sleep(0.01)