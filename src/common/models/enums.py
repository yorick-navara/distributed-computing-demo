from enum import Enum


class ProcessStatus(str,Enum):
    NOT_STARTED = 'NOT STARTED'
    STARTED = 'STARTED'
    FINISHED = 'FINISHED'
    ERROR = 'ERROR'