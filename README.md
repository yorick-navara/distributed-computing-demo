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
mysql> use local_db;

mysql> show tables;

mysql> select * from run_process

```

