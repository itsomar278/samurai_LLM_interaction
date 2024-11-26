import threading
import time

from django.core.management import BaseCommand

from ...utils.rabbitmq_consumer import start_consumer


class Command(BaseCommand):
    help = 'Starts the RabbitMQ consumer to listen for text processing requests'

    def handle(self, *args, **kwargs):
        consumer_thread = threading.Thread(target=start_consumer)
        consumer_thread.daemon = True
        consumer_thread.start()

        # Keeps the command running
        while True:
            time.sleep(1)