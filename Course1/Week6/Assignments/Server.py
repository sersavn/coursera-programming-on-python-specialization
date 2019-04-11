import asyncio
import sys
import re

def run_server(host, port):
    async def wakeup():
        while True:
            await asyncio.sleep(0.5)

    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)
    asyncio.async(wakeup())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

class ClientServerProtocol(asyncio.Protocol):
    global storage
    storage = {}

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):

        def get():
            self.transport.write('ok\n'.encode())

            try:
                key = data_splitted[1]
                reply_str = []
                if key == '*':
                    for k,v in storage.items():
                        for val in v:
                            z = '{} {} {}'.format(k, str(val[0]),str(val[1]))
                            reply_str.append(z)
                else:
                    for val in storage[key]:
                        z = '{} {} {}'.format(key, str(val[0]), str(val[1]))
                        reply_str.append(z)
                reply_str = '\n'.join(reply_str)
                self.transport.write(reply_str + '\n\n'.encode())
            except KeyError:
                self.transport.write('\n\n'.encode())

        def put():
            try:
                timestamp_and_val = (float(data_splitted[2]), int(data_splitted[3]))
                if data_splitted[1] in storage:
                    if timestamp_and_val not in storage[data_splitted[1]]:
                        storage[data_splitted[1]].append(timestamp_and_val)
                else:
                    storage[data_splitted[1]] = [(timestamp_and_val)]
                self.transport.write('ok\n\n'.encode())
            except IndexError:
                self.transport.write('error\nwrong command\n\n'.encode())
            return storage

        try:
            data = data.decode()
            data_splitted = re.split(' |\n', data)[:-1] #getting rid of newline at the end
        except:
            self.transport.write('cant decode\n\n'.encode())

        if data_splitted[0] == 'put':
            put()
        elif data_splitted[0] == 'get':
            get()
        else:
            self.transport.write('error\n\n'.encode())
