# Distributed computing prototype with Python and RabbitMQ

Tutorial on RabbitMQ and Python: 
- https://www.rabbitmq.com/tutorials/tutorial-one-python.html
- https://www.rabbitmq.com/tutorials/tutorial-two-python.html


```
docker run -p 5672:5672 rabbitmq
```

```
python3 src/leader/main.py
```

To run the complete stack in Docker compose, run:

```
docker compose up --force-recreate --build
```

Then connect to the DB with:

```
docker exec -t -i demo-db sh
mysql --host=127.0.0.1 --port=3306 -u root -p
```

Type in the password.

And type the following:

```
mysql> use local_db; select * from run_process;

```

Manage the queue:

```
docker exec -t -i demo-queue sh
rabbitmq-plugins enable rabbitmq_management
```

Now you can browse to http://localhost:15672/ for the dashboard.

Or continue in the command line with rabbitmqctl:

```
rabbitmqctl list_queues
```

