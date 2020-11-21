from __future__ import absolute_import, unicode_literals
from celery.task import task, periodic_task
from datetime import timedelta
import pika
from Producer_Consumer.apis.Consumer.consumer import Consumer


@task
def add(x, y):
    return x + y


@periodic_task(run_every=timedelta(hours=1))
def mul():
    x = 1
    y = 2
    print("Multiplying {} and {}".format(x, y))
    return x * y


@periodic_task(run_every=timedelta(minutes=1))
def run_listener():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))

    channel = connection.channel()
    channel.queue_declare(queue='Producer_Consumer_Queue')

    channel.basic_consume(queue='Producer_Consumer_Queue',
                          auto_ack=True,
                          on_message_callback=Consumer.consume)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
