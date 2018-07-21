import socket
import ujson

# [ Server ke Lora (panel surya) ]
# 1. Id perangkat

# [ Lora (panel surya) ke server ]
# 1. Tegangan panel surya
# 2  Arus panel surya
# 3. Tegangan baterai
# 4. Arus baterai

URL = 'www.micropython.org'
PATH = '/'
# URL = 'openlibrary.telkomuniversity.ac.id'
# PATH = '/room/index.php/Rfidbooked?rfid=040D3782253980&roomid=15'
# s.settimeout(5000)

def contoh():
    # init data
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = socket.socket()
    s.connect(socket.getaddrinfo(URL, 80)[0][-1])
    s.sendall("GET " + PATH + " HTTP/1.0\r\nHost: " + URL + "\r\n\r\n")

    #Parsing to string
    raw = s.recv(4096)
    parse = str(raw,"UTF-8")

    # s.close
    return parse

def getJson():
    # parse body to json
    json = "{\"rc\":\"00\",\"status\":\"success\",\"data\":{\"suhu\":\"5\",\"humid\":\"10\",\"volt\":\"220\",\"amp\":\"2\"}}"
    obj = ujson.loads(json)
    return obj


def initID(id):
    print("ID"+ id)

def sendParam():
    print("Send")

def getParam():
    print("Get")
