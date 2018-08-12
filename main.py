import pycom
import time
from fungsi import CheckStatus, http_get, request

BASE   = 'http://192.168.1.110'
CHECK  = '/SolarCharger/api/status/check.php?id=lopy1'
INPUT  = '/SolarCharger/api/update/dataperaangkat.php?'

# MAIN PROGRAM
if __name__=="__main__":
    while 1:
        time.sleep(1)
        pycom.rgbled(0x000f00)
        parsing = CheckStatus(request(BASE + CHECK))
        try:
            print("ID adalah    : " + parsing.id)
            print("ID Perangkat : " + parsing.id_perangkat)
            # lakukan update data
            pycom.rgbled(0x00000f)
        except:
            0xRRGGBB
            pycom.rgbled(0x0f0000)
            print("\n\n")

# while 1:
#     time.sleep(1)
#     pycom.rgbled(0x000000)
#     try:
#         pycom.rgbled(0x00ff00)
#         pycom.rgbled(0x0000ff)
#     except:
#         pycom.rgbled(0xff0000)
#         print("Gagal Koneksi Server")
