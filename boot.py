# boot.py -- run on boot-up
import pycom
import time
import machine
from network import WLAN

# CONFIG
SSID = 'PONDOK DR LT 1'
PSWD = 'bulanpuasa'

# SSID = 'Link Space'
# PSWD = ''

pycom.heartbeat(False)
wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
pycom.rgbled(0x007f00)
for net in nets:
    pycom.rgbled(0x707000)
    if net.ssid == SSID:
        print('Ditemukan Jaringan!')
        wlan.connect(net.ssid, auth=(net.sec, PSWD), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('Berhasil Tersambung!')
        pycom.rgbled(0x00007f)
        break
    else:
        pycom.rgbled(0x7f0000)
