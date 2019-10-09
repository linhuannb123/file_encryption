from Cryptodome.Cipher import AES
import base64


def AES_Encrypt(key, data):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    vi = '0102030405060708'
    pad = lambda s: s + (16 - len(s)%16) * b" "
    data = pad(data)
    
    # 字符串补位
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    encryptedbytes = cipher.encrypt(data)
    # 加密后得到的是bytes类型的数据
    encodestrs = base64.b64encode(encryptedbytes)
    # 使用Base64进行编码,返回byte字符串
    enctext = encodestrs.decode('utf8')
    # 对byte字符串按utf-8进行解码
    return enctext

def AES_Decrypt(key, data):
    vi = '0102030405060708'
    data = data.encode('utf8')
    encodebytes = base64.decodebytes(data)
    # 将加密数据转换位bytes类型数据
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    text_decrypted = cipher.decrypt(encodebytes).strip()

    return text_decrypted
  
  

def enc_file(key,file):  #加密
    with open(file,"rb") as r: #读取文件
        data = r.read()

    enctext = AES_Encrypt(key, data) #开始加密

    with open(file,"w") as w: #写入文件
        w.write(enctext)
    print("加密成功！")



def dec_file(key,file):  #解密  
    with open(file,"r") as r:
        enctext = r.read()     #读取文件

    text_decrypted = AES_Decrypt(key, enctext) #开始解密

    with open(file,"wb") as dec:  #写入文件
        dec.write(text_decrypted)
    print("解密成功")

# key = '0CoJUm6Qyw8W8jud'  #密钥
key = 'ashdeuhasdaaldaa'  #密钥
dec_file(key,"机场代号.txt")


