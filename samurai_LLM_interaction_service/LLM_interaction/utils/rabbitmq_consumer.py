import pika
from .rabbitmq_channel import RabbitMQChannel
from ..services.process_text_processing_request import process_text_processing_request

def start_consumer():
    channel = RabbitMQChannel.create_channel()

    channel.queue_declare(queue='ready_for_vectorization', passive=False)

    channel.basic_consume(queue='ready_for_vectorization', on_message_callback=process_text_processing_request)

    try:
        print("Starting consumer... Press Ctrl+C to stop.")
        channel.start_consuming()
    except KeyboardInterrupt:
        print("\nConsumer stopped by user.")
        channel.stop_consuming()
    finally:
        RabbitMQChannel.close_channel()
        print("Connection closed.")
