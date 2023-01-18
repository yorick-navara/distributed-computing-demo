from enum import Enum


class ProcessStatus(str,Enum):
    CREATED = 'CREATED'
    STARTED = 'STARTED'
    FINISHED = 'FINISHED'
    ERROR = 'ERROR'
