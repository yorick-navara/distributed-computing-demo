import sys
import os
import time
import pika

QUEUE_NAME = 'task_queue'
CONNECTION = 'demo-queue' #'amqp://guest:guest@demo-queue:5672/'  # 'localhost'

def do_work(body):
    print("Worker: Starting calculation of selection {body}...")
    print("Worker: Retrieving network for selection {body} from database...")
    time.sleep(1)
    print("Worker: Retrieving loads for selection {body}...")
    time.sleep(1)
    print("Worker: Performing load flow calculation for selection {body}...")
    print("Worker: Post processing results...")
    time.sleep(1)
    print("Worker: Exporting results to database...")
    print("Worker: Work finished.")


def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body)
    print("Worker: Received message: {body}")
    do_work(body)
    print("Worker: Acknowledging completion of message {body}...")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print("Worker: Finished handling message.")


def receive_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters(CONNECTION))
    channel = connection.channel()
    
    channel.queue_declare(queue=QUEUE_NAME, durable=True) # idempotent
    
    #channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)
    
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