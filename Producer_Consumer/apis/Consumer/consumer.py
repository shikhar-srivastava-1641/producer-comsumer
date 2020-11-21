
class Consumer:

    @staticmethod
    def consume(ch, method, properties, body):
        """Consume rabbitmq msg"""

        print(" [x] Received ch %r" % ch)
        print(" [x] Received method %r" % method)
        print(" [x] Received prop %r" % properties)
        print(" [x] Received body %r" % body)
