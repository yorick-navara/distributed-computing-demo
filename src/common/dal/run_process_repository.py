from dataclasses import asdict
from uuid import UUID

from common.dal.connect_db import insert_data, get_data
from common.models.run_process import RunProcess


class RunProcessRepository:

  @staticmethod
  def insert_run_process(run_process: RunProcess) -> None:
    insert_query = (
      "INSERT INTO run_process "
      "(run_id, task_id, task_status) "
      "VALUES (%(run_id)s, %(task_id)s, %(task_status)s)"
    )
    
    insert_data(insert_query, run_process.to_dict())

  @staticmethod
  def update_run_process(run_process: RunProcess) -> None:
    update_query = (
      "UPDATE run_process "
      "SET task_status = %(task_status)s"
      "WHERE run_id = %(run_id)s AND task_id = %(task_id)s)"
    )
    
    insert_data(update_query, run_process.to_dict())

  @staticmethod
  def get_run_process(run_id: UUID, task_id:UUID) -> RunProcess:
    query = (
      "SELECT run_id, task_id, task_status FROM run_process"
      "WHERE run_id = %s AND task_id = %s"
    )
    
    return get_data(query, (str(run_id), str(task_id)))
  