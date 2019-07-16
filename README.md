![Funken logo](https://github.com/ar0551/PyFunken/blob/master/materials/FNK_LOGO_GITHUB.png)

# PyFunken
Python interface (GPL) to the [Funken](https://github.com/astefas/Funken) Serial Protocol Toolkit.

PyFunken is a Pyhton-based interface to the Funken Serial Protocol Toolkit. It offers classes to initiate communication with Funken-Enabled Arduino devices, send commands and handle responses.

Funken is a [Arduino](https://www.arduino.cc) [library](https://www.arduino.cc/en/Reference/Libraries) that enables [callbacks](https://en.wikipedia.org/wiki/Callback_(computer_programming)) on an arduino. It is part of a workflow that simplifies communication between your Arduino and any host, that is able to speak to it via serial messages.
For more info on Funken, see the [Funken Repository](https://github.com/astefas/Funken).

PyFunken is build on top of [PySerial](https://github.com/pyserial/pyserial).

## How to use PyFunken


### Initialize Communication with a Funken Device
```python
import funken
import time

## serial port to connect to
port = "COM6"

## initialize the main PyFunken object
pyf = funken.PyFunken([port], [57600])

## register devices on the selected com port
pyf.ser_conn[port].register_devices()
time.sleep(1)
```

### Send Commands to a Funken Device
```python
## set pin 13 as output
pyf.send_command("PM 13 1\n", port, 1)
while True:
	## turn led on pin 13 on
	pyf.send_command("DW 13 1\n", port, 1)
	time.sleep(1)
	## turn led on pin 13 off
	pyf.send_command("DW 13 0\n", port, 1)
	time.sleep(1)

```

