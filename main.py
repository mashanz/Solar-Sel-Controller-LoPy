import time
from fungsi import contoh, getJson

while 1:
    time.sleep(1)
    pycom.rgbled(0x000000)
    try:
        pycom.rgbled(0x00ff00)
        print(contoh())
        pycom.rgbled(0x0000ff)
        obj = getJson()
        print(obj["data"])
        print("Tegangan = " + obj["data"]["volt"])
        print("Arus = " + obj["data"]["amp"])
        print("Kelembapan = " + obj["data"]["humid"])
        print("Suhu = " + obj["data"]["suhu"])
    except:
        pycom.rgbled(0xff0000)
        print("Gagal Koneksi Server")
