from enum import Enum


class ProcessStatus(str,Enum):
    STARTED = 'STARTED'
    FINISHED = 'FINISHED'
    ERROR = 'ERROR'