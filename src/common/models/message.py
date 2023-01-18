from uuid import UUID
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List
import json


DATETIME_FORMAT = "%Y-%m-%d %H:%M"


@dataclass
class Message:
    run_id: UUID
    task_id: UUID
    selection: List[int]
    start_date: datetime
    end_date: datetime

    def _stringify(self, obj: any):
        if isinstance(obj,UUID):
            return str(obj)
        elif isinstance(obj,datetime):
            return obj.strftime(DATETIME_FORMAT)
        else:
            return obj

    def to_json(self):
        msg_dict = asdict(
            self,
            dict_factory=lambda data:dict((x[0], self._stringify(x[1])) for x in data)
        )
        return json.dumps(msg_dict)
    
    @staticmethod
    def from_json(json_str):
        msg_dict = json.loads(json_str)
        return Message(
            run_id=UUID(msg_dict['run_id']),
            task_id=UUID(msg_dict['task_id']),
            selection=msg_dict['selection'],
            start_date=datetime.strptime(msg_dict['start_date'], DATETIME_FORMAT),
            end_date=datetime.strptime(msg_dict['end_date'], DATETIME_FORMAT)
        )
