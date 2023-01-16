from dataclasses import dataclass
from common.models.enums import ProcessStatus
from uuid import UUID
from typing import Dict


@dataclass
class RunProcess:
    run_id: UUID
    task_id: UUID
    # task_definition: str
    task_status: ProcessStatus
    
    # def __init__(
    #     self,
    #     run_id: UUID,
    #     task_id: UUID,
    #     task_status: ProcessStatus
    # ) -> None:
    #     self.run_id = str(run_id)
    #     self.task_id = str(task_id)
    #     self.task_status = str(task_status)
        
        
    def to_dict(self) -> Dict:
        return {
            'run_id': str(self.run_id),
            'task_id': str(self.task_id),
            'task_status': str(self.task_status)
        }
        # msg_dict = asdict(
        #     self,
        #     dict_factory=lambda data:dict((x[0], self._stringify(x[1])) for x in data)
        # )
        # return json.dumps(msg_dict)
        # return dict(
        #     (key, value)
        #     for (key, value) in self.__dict__.items()
        #     if key not in _excluded_keys
        #     )
