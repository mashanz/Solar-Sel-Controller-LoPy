# import pycom
import time
from fungsi import CheckStatus, http_get, request, updateData

MY_ID  = 'lopy1'
BASE   = 'http://192.168.1.110'
CHECK  = '/SolarCharger/api/status/check.php?id=' + MY_ID
INPUT  = '/SolarCharger/api/update/dataperaangkat.php'

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
            try:
                updateData(BASE, INPUT, parsing.id, 100, 200, 300, 400)
            except:
                print("\n\n")    
        except:
            # pycom.rgbled(0x0f0000)
            print("\n\n")