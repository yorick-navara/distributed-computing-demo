import time
import pika
from uuid import uuid4
from datetime import datetime

from common.models.message import Message
from common.models.enums import ProcessStatus
from common.models.run_process import RunProcess
from common.dal.run_process_repository import RunProcessRepository


QUEUE_NAME = 'task_queue'
CONNECTION = 'demo-queue' # 'amqp://guest:guest@demo-queuee:5672/'  # 'localhost'

def do_work():
    print("Doing preliminary work...")
    time.sleep(2)
    print("Exporting result of preliminary work to database...")
    print("Retrieving selections of work from database...")
    return [[0],[1],[2,3],[4],[5],[6],[7],[8,9,10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20],[21],[22],[23],[24],[25,26],[27],[28],[29],[30]]


def main():
    print("Starting leader...")
    print("Waiting...")
    time.sleep(60)
    print("Continuing leader...")
    
    print("Started leader.")
    selections = do_work()
    
    run_id = uuid4()
    start_date = datetime.strptime('2022-11-01 00:00', '%Y-%m-%d %H:%M')
    end_date = datetime.strptime('2022-12-01 00:00', '%Y-%m-%d %H:%M')
    
    print(f'Selection of work: {selections}')
    for selection in selections:
        print(f'Defining message for selection {selection}')
        task_id = uuid4()
        
        run_process = RunProcess(
            run_id=run_id,
            task_id=task_id,
            task_status=ProcessStatus.CREATED
        )
        RunProcessRepository.insert_run_process(run_process)
        
        msg = Message(
            run_id=run_id,
            task_id=task_id,
            selection=selection,
            start_date=start_date,
            end_date=end_date)
        send_message(msg)

    print("Leader finished.")


def send_message(message: Message):
    print(f'Sending message: {message}')
    connection = pika.BlockingConnection(pika.ConnectionParameters(CONNECTION))
    channel = connection.channel()
    
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    
    channel.basic_publish(exchange='', # default exchange
                      routing_key=QUEUE_NAME,
                      body=message.to_json(),
                      properties=pika.BasicProperties(
                         delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
                      ))
    print(f'Message sent: {message}')
    time.sleep(5)
    connection.close()


if __name__ == '__main__':
    main()
