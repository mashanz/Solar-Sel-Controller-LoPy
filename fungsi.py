import socket
import ujson

# MODEL OBJECT
class CheckStatus:
    def __init__(self, inputdata):
        self.obj = inputdata
        self.id = self.parse('id')
        self.id_perangkat = self.parse('id_perangkat')

    def parse(self, data):
        try:
            return self.obj[data]
        except:
            return None 

# API HTTP GET
def http_get(url):
    _, _, host, path = url.split('/', 3)
    print("HOST : " + host)
    print("PATH : " + path)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    val = ""
    while True:
        data = s.recv(2048)
        if data:
            val = str(data, 'utf8')
        else:
            break
    s.close()
    return val

# FILTERING BODY
def request(URL):
    data = None
    dapet = http_get(URL)
    dapet1 = dapet.split('\r\n\r\n')
    fail = "{\"status\":\"Gagal Parsing Response\"}"
    try:
        data = ujson.loads(dapet1[1])
        print("STAT : Success Get JSON Data\n")
        print(dapet1[1])
    except:
        print("STAT : Failed Get JSON Data\n")
        print(dapet1[1])
        return ujson.loads(fail)
    return data
