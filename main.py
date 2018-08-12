# import pycom
import time
# import crypto
from fungsi import CheckStatus, http_get, request

MY_ID  = 'lopy1'
BASE   = 'http://localhost'
CHECK  = '/SolarCharger/api/status/check.php?id=' + MY_ID
INPUT  = '/SolarCharger/api/update/dataperangkat.php'

# MAIN PROGRAM
if __name__=="__main__":
    while 1:
        time.sleep(1)
        # pycom.rgbled(0x000f00)
        parsing = CheckStatus(request(BASE + CHECK))
        try:
            print("ID adalah    : " + parsing.id)
            print("ID Perangkat : " + parsing.id_perangkat)
            # lakukan update data
            # pycom.rgbled(0x00000f)
            print("\n\n")
            # time.sleep(1)
            # try:
            #     updateData(BASE, INPUT, parsing.id_perangkat, RandomRange(0.1,2.4), RandomRange(0.0,13.0), RandomRange(0.0,2.9), RandomRange(0.0,12.9))
            # except:
            #     print("GAGAL UPDATE\n\n")
        except:
            # pycom.rgbled(0x0f0000)
            print("\n\n")
