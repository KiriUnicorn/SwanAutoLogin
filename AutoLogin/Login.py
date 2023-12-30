import requests
import time
import subprocess
from time import sleep

# 常量
target_host = "192.168.240.3"
WIFI_NAME = "SWXY-WIFI"


# 寻找 SSID 字段
def Check_Wifi():
    result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
    output = result.stdout
    sleep(1)
    ssid_index = output.find("SSID")
    if ssid_index != -1:
        ssid_start = output.find(":", ssid_index) + 2  # 找到冒号后面的位置
        ssid_end = output.find("\n", ssid_start)  # 找到换行符的位置
        ssid = output[ssid_start:ssid_end].strip()  # 获取SSID并去除首尾空格
        if ssid == WIFI_NAME:
            print("匹配")
            return True
        else:
            print("wifi不匹配", ssid)
            return False

def is_ping_successful(host):
    try:
        # 执行ping命令，timeout设置超时时间（单位为秒）
        subprocess.run(["ping", "-c", "1", host], check=True, timeout=5)
        print(f"Ping to {host} successful.")
        return True
    except subprocess.CalledProcessError:
        print(f"Ping to {host} failed.")
        return False
    except subprocess.TimeoutExpired:
        print(f"Ping to {host} timed out.")
        return False


# 例子：检查是否能够ping通谷歌的公共DNS服务器
def ping_host(host):
    try:
        subprocess.check_output(["ping", "-c", "1", host])
        print('true')
        return True
    except subprocess.CalledProcessError:
        print('false')
        return False


while True:
    if Check_Wifi() and is_ping_successful(target_host) and ping_host(target_host):
        print("ok")
        # print(f"Ping to {target_host} successful")
        url = "http://192.168.240.3/drcom/login"
        # 生成当前毫秒时间戳
        timestamp = int(time.time() * 1000)
        phone = '19313183825'
        pasword = '090010'
        params = {
                'callback': f'dr{timestamp}',
                'DDDDD': phone,
                'upass': pasword,
                '0MKKey': '123456',
                'R1': '0',
                'R3': '0',
                'R6': '0',
                'para': '00',
                'v6ip': '',
                '_': str(timestamp)
            }
        response = requests.get(url, params=params)

        break
    else:
        pass






