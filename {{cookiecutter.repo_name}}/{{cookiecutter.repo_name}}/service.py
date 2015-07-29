import json
from vyked import HTTPApplicationService, TCPApplicationService, get, post, Bus, delete, api, put
from again.decorate import silence_coroutine
from aiohttp.web import Response

from .manager import {{cookiecutter.manager_class_name}}
from .exceptions import {{cookiecutter.exceptions_class_name}}

class {{cookiecutter.service_class_name}}HTTPService(HTTPApplicationService):

    def __init__(self, host, port):
        super(ComboHTTPService, self).__init__('{{cookiecutter.service_name}}', 1, host, port)



class {{cookiecutter.service_class_name}}TCPService(TCPApplicationService):

    def __init__(self, host, port):
        super(CombosTCPService, self).__init__('{{cookiecutter.service_name}}', 1, host, port)


if __name__ == '__main__':
    bus = Bus()
    tcp_service = {{cookiecutter.service_class_name}}TCPService('{{cookiecutter.tcp_address}}', {{cookiecutter.tcp_port}})
    http_service = {{cookiecutter.service_class_name}}HTTPService('{{cookiecutter.http_address}}', {{cookiecutter.http_port}})
    bus.serve_tcp(tcp_service)
    bus.serve_http(http_service)
    bus.start('127.0.0.1', 4500, '127.0.0.1', 6379)
