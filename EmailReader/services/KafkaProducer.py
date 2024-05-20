from confluent_kafka import Producer
import json
import time
from config.config import KAFKA_CONFIG 

class EmailProducer:
    def __init__(self):
        self.producer = Producer(KAFKA_CONFIG)

    def produce_email(self, topic, message):
        def delivery_report(err, msg):
            if err is not None:
                print(f'Error al enviar el mensaje: {err}')
            else:
                print(f'Mensaje enviado: {msg.value()}')

        message_json = json.dumps(message)
        self.producer.produce(topic, message_json, callback=delivery_report)
        self.producer.poll(0.5)
        time.sleep(1)
