import sys
import os
import time
import subprocess
import pika


from common.models.message import Message
from common.models.run_process import RunProcess
from common.models.enums import ProcessStatus
from common.dal.run_process_repository import RunProcessRepository


QUEUE_NAME = 'task_queue'
CONNECTION = 'demo-queue' #'amqp://guest:guest@demo-queue:5672/'  # 'localhost'


def do_work(message: Message):
    for selection in message.selection:
        print("Worker: Starting calculation of selection {selection}...")
        print("Worker: Retrieving data for selection {selection} from database...")
        time.sleep(5)
        print("Worker: Retrieving loads for selection {selection}...")
        time.sleep(10)
        print("Worker: Performing calculation for selection {selection}...")
        print("Worker: Post processing results...")
        time.sleep(10)
        print("Worker: Exporting results to database...")
    print("Worker: Work finished.")


def handle_incoming_message(ch, method, properties, body:str):
    print(f"Worker: Received message: {body}")

    message = Message.from_json(body)
    
    print('Received message:')
    print(f'run_id: {message.run_id}')
    print(f'task_id: {message.task_id}')
    print(f'selections: {message.selection}')
    print(f'start_date {message.start_date}')
    print(f'end_date {message.end_date}')

    run_process = RunProcess(
        run_id=message.run_id,
        task_id=message.task_id,
        task_status=ProcessStatus.STARTED,
        worker_id=os.environ['HOSTNAME']
    )

    RunProcessRepository.update_run_process(run_process)

    print("Worker: Acknowledging delivery of message {body}...")
    ch.basic_ack(delivery_tag = method.delivery_tag)

    do_work(message)

    run_process.task_status = ProcessStatus.FINISHED
    RunProcessRepository.update_run_process(run_process)

    print("Worker: Finished handling message.")


def receive_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters(CONNECTION))
    channel = connection.channel()
    
    channel.queue_declare(queue=QUEUE_NAME, durable=True) # idempotent
    
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=handle_incoming_message)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def main():
    print("Starting worker...")
    
    print("Waiting...")
    time.sleep(30)
    print("Continuing worker...")
    try:
        receive_messages()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


if __name__  == '__main__':
    main()