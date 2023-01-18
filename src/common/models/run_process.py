from dataclasses import dataclass
from common.models.enums import ProcessStatus
from uuid import UUID
from typing import Dict, List


@dataclass
class RunProcess:
    run_id: UUID
    task_id: UUID
    task_status: ProcessStatus
    worker_id: str = None
        
        
    def to_dict(self) -> Dict:
        self_dict = {
            'run_id': str(self.run_id),
            'task_id': str(self.task_id),
            'task_status': self.task_status.value
        }
        if self.worker_id is not None:
            self_dict['worker_id'] = self.worker_id

        return self_dict
