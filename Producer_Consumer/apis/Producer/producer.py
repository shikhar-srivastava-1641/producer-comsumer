import pika
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response


class Producer:

    @staticmethod
    @api_view(['POST'])
    def produce(request):
        """Produce Data"""

        print("Starting")

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        print("con estb")
        try:
            req = request.data
            print(req)

            number_of_msg = req.get('no_of_msg')
            print(number_of_msg)

            channel = connection.channel()
            print("channel init")

            channel.queue_declare(queue='Producer_Consumer_Queue')
            print("qu dec")

            for i in range(number_of_msg):

                msg_to_publish = {
                    'id': i,
                    'success': True,
                    'data': 'Hello'
                }
                print(msg_to_publish)

                channel.basic_publish(
                    exchange='',
                    routing_key='Producer_Consumer_Queue',
                    body=json.dumps(msg_to_publish)
                )
                print("msg published")

            return Response({'status': True}, status=200)

        except Exception as e:
            print("Exception Occurred: ", str(e))
            return Response({'status': False}, status=500)

        finally:
            connection.close()
