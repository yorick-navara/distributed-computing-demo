import sys
import os
import time
import pika

from common.message import Message


QUEUE_NAME = 'task_queue'
CONNECTION = 'demo-queue' #'amqp://guest:guest@demo-queue:5672/'  # 'localhost'


def do_work(message: Message):
    for selection in message.selections:
        print("Worker: Starting calculation of selection {selection}...")
        print("Worker: Retrieving data for selection {selection} from database...")
        time.sleep(1)
        print("Worker: Retrieving loads for selection {selection}...")
        time.sleep(1)
        print("Worker: Performing calculation for selection {selection}...")
        print("Worker: Post processing results...")
        time.sleep(1)
        print("Worker: Exporting results to database...")
    print("Worker: Work finished.")


def handle_incoming_message(ch, method, properties, body:str):
    #print(" [x] Received %r" % body)
    print("Worker: Received message: {body}")
    # deserialize message:
    message = Message.from_json(body)
    
    print('Received message:')
    print(f'run_id: {message.run_id}')
    print(f'task_id: {message.task_id}')
    print(f'selections: {message.selections}')
    print(f'start_date {message.start_date}')
    print(f'end_date {message.end_date}')
    
    
    do_work(message)
    print("Worker: Acknowledging completion of message {body}...")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print("Worker: Finished handling message.")


def receive_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters(CONNECTION))
    channel = connection.channel()
    
    channel.queue_declare(queue=QUEUE_NAME, durable=True) # idempotent
    
    #channel.basic_qos(prefetch_count=1)
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