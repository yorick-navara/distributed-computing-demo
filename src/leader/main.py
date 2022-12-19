import time
import pika


QUEUE_NAME = 'task_queue'
CONNECTION = 'demo-queue' # 'amqp://guest:guest@demo-queuee:5672/'  # 'localhost'

def do_work():
    print("Converting topology from State Estimation to PowerGridModel format...")
    time.sleep(2)
    print("Exporting topology to database...")
    print("Retrieving selections of topology from database...")
    return list(range(10))


def main():
    print("Starting leader...")
    print("Waiting...")
    time.sleep(30)
    print("Continuing leader...")
    
    print("Started leader.")
    selections = do_work()
    
    print(f'Selection in network: {selections}')
    for selection in selections:
        print(f'Defining message for selection {selection}')
        send_message(str(selection))
        time.sleep(1)
    print("Leader finished.")


def send_message(message):
    print(f'Sending message: {message}')
    connection = pika.BlockingConnection(pika.ConnectionParameters(CONNECTION))
    channel = connection.channel()
    
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    
    channel.basic_publish(exchange='', # default exchange
                      routing_key='hello',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
                      ))
    print(f'Message sent: {message}')
    
    connection.close()


if __name__ == '__main__':
    
    main()