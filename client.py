# coding:UTF-8
# Python 3.10.6

import socket
import time

class Client:
    def __init__(self, ip, port, name, file):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.file = file
        self.ip = ip
        self.port = port
        self.name = name

    def upload(self):
        try:
            with open(self.file + self.name, "rb") as r:
                file_data = r.read()
        except BaseException as error:
            print(error)
        while True:
            try:
                self.sock.connect((self.ip, self.port))
                print("连接成功")
                data = f"upload:{self.name}"
                self.sock.send(data.encode())
                time.sleep(1)
                self.sock.send(file_data)
                print("发送成功")
                time.sleep(1)
                repose = self.sock.recv(65001).decode("utf8", "ignore")
                if repose == "OK":
                    print("上传成功")
                    break

            except WindowsError as error:
                print(error)
                break


if __name__ == "__main__":
    try:
        ip = input("IP:")
        port = int(input("端口:"))
        name = input("文件名称:")
        file = input("文件路径(请勿包含文件名称,末尾加上'\\'或'/'):")
        use = Client(ip, port, name, file)
        use.upload()
    except BaseException as error:
        print(error)
