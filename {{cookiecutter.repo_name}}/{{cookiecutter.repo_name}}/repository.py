from vyked.sql import PostgresStore
from vyked.utils.log import log

from .exceptions import {{cookiecutter.exceptions_class_name}}

class {{cookiecutter.repository_class_name}}(PostgresStore):

    def __init__(self):
        pass
