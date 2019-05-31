import socket
import time
#import unittest

class Client:

    def __init__(self, host, port, timeout=10):
        self.host = host
        self.port = port
        self.timeout = timeout

    def put(self, metric_name, metric_value, timestamp=str(int(time.time()))):
        sended_str = 'put {} {} {}\n'.format(metric_name, metric_value, timestamp)
        print(sended_str)
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            sock.sendall(sended_str.encode("utf8"))
            recv_data = sock.recv(1024)
            #print(recv_data)
            if not recv_data:
                raise ClientError()
            if recv_data.decode("utf-8") == "error\nwrong command\n\n":
                raise ClientError()
            if recv_data.decode("utf-8") == "ok\n\n":
                pass

    def get(self, metric_name):
        sended_str = 'get {}\n'.format(metric_name)
        with socket.create_connection((self.host, self.port)) as sock:
            sock.sendall(sended_str.encode("utf8"))
            recv_data = sock.recv(4096).decode("utf-8")
            print(recv_data)
            if not recv_data:
                raise ClientError()

        answer_dict = {}
        recv_data = recv_data.split('\n')
        recv_data = recv_data[1:-2]
        for i in recv_data:
            j = i.split(" ")
            dict_val = (int(j[2]), float(j[1]))
            if j[0] in answer_dict:
                answer_dict[j[0]].append(dict_val)
            else:
                answer_dict[j[0]] = [dict_val]

        if metric_name == '*':
            return answer_dict
        else:
            try:
                return {metric_name : answer_dict[metric_name]}
            except:
                return dict()

class ClientError(Exception):
    pass

client = Client('127.0.0.1', 8181)

#client.put('A', 500)
#client.put('B', 500)

#client.get('A')

#client.put('a')
