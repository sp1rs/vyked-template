import json
from vyked import HTTPApplicationService, TCPApplicationService, get, post, Bus, delete, api, put
from again.decorate import silence_coroutine
from aiohttp.web import Response


class ComboHTTPService(HTTPApplicationService):

    def __init__(self, host, port):
        self._manager = ComboManager()
        super(ComboHTTPService, self).__init__('{{cookiecutter.service_name}}', 1, host, port)



class CombosTCPService(TCPApplicationService):

    def __init__(self, host, port):
        self._manager = ComboManager()
        super(CombosTCPService, self).__init__('{{cookiecutter.service_name}}', 1, host, port)


if __name__ == '__main__':
    bus = Bus()
    tcp_service = CombosTCPService('{{cookiecutter.tcp_address}}', {{cookiecutter.tcp_port}})
    http_service = ComboHTTPService('{{cookiecutter.http_address}}', {{cookiecutter.http_port}})
    bus.serve_tcp(tcp_service)
    bus.serve_http(http_service)
    bus.start('127.0.0.1', 4500, '127.0.0.1', 6379)
