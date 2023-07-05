# coding:UTF-8
# Python 3.10.6

import socket
import datetime
import prettytable

class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("192.168.8.176", 5555))
        self.sock.listen(1)
        self.sock.setblocking(False)
        self.table = prettytable.PrettyTable()
        self.table.title = "连接"
        self.table.field_names = ["IP", "端口", "时间"]

    def file(self):
        while True:
            while True:
                try:
                    conn, addr = self.sock.accept()
                    ip, port = str(addr).split(",")
                    self.table.add_row([f"{ip[2:-1]}", f"{port[1:-1]}", datetime.datetime.now()])
                    print(self.table)
                    break
                except BlockingIOError:
                    pass

            while True:
                try:
                    data = conn.recv(65001).decode("utf8", "ignore").split(":")
                    if data[0] == "upload":
                        with open(data[1], "w+", encoding="UTF-8") as w:
                            file_data = conn.recv(65001).decode("utf8", "ignore")
                            w.write(file_data)
                            conn.send(b"OK")
                            break
                    else:
                        self.table.del_row(0)
                        conn.close()
                        break
                except BlockingIOError:
                    pass


if __name__ == "__main__":
    Server()
    Server().file()
