from flask import Flask, request
import datetime
import threading
import socket
import hmac
import hashlib
from Crypto.Cipher import AES
from Crypto.Util import Counter
import time
from pwn import unpack

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    pass



@app.route('/xpeng')
def xpeng():
    try:
        HardwareID = request.args.get('id').encode()
        current_time = int(time.time()) // 10000
        # current_time = 407230 # 小鹏的垃圾判定，只判定暗码有没有过期，但是不判定生成时间是否超过当前时间
        # 计算 aes_iv 和 aes_key
        hmac_obj = hmac.new(b'\x03U\x0f\xf7\xf7\x02`\x01Q\xd5hn\xb8\xe4y6', HardwareID, hashlib.sha512)
        hmac_hash = hmac_obj.digest()
        aes_iv = hmac_hash[32:48]
        aes_key = hmac_hash[0:32]
        a0 = ((current_time >> 12) & 0xFF)  # 获取最高的8位作为 a0
        a1 = ((current_time >> 4) & 0xFF)  # 获取接下来的8位作为 a1
        a2 = ((current_time & 0xF) << 4) | (0x03 & 0xF)
        aes_out = bytes([a0, a1, a2])
        # aes_out=b'(\xf9#'
        decryptcateIdType = aes_out[2] & 0xF
        cipher = AES.new(aes_key, AES.MODE_CTR,
                         counter=Counter.new(128, initial_value=int.from_bytes(aes_iv, byteorder='big')))
        aes_in = cipher.encrypt(aes_out)
        aes_in = unpack(aes_in, 24)
        # print(aes_in)
        int2 = ((aes_in >> 16) & 0xFF) | (((aes_in >> 8) & 0xFF) << 8) | ((aes_in & 0xFF) << 16)
        # print(int2)
        print(f'*#{str(decryptcateIdType).zfill(2)}*{str(int2).zfill(8)}#*')
        return f'*#{str(decryptcateIdType).zfill(2)}*{str(int2).zfill(8)}#*'
    except:
        return 'FUCK YOU'


def th1():
    app.run(host='0.0.0.0', port=5000)


def th2():
    app.run(host='::', port=5000)


if __name__ == '__main__':
    t1 = threading.Thread(target=th1)
    t1.start()
    t1.join()


