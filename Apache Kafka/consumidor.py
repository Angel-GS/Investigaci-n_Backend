from confluent_kafka import Consumer, KafkaError
import time, random

# Configuración del consumidor Kafka
config = {
    'bootstrap.servers': 'localhost:29092',  # Cambiar si es necesario
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
}

# Crear el consumidor Kafka
consumer = Consumer(config)


def consume_messages(topic):
    """ Función para consumir mensajes """
    consumer.subscribe([topic])
    try:
        while True:
            msg = consumer.poll(timeout=1.0)  # Esperar mensajes por un segundo
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            print(f'Mensaje recibido: {msg.value().decode("utf-8")}')
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


if __name__ == '__main__':
    # Especificar el topic del que se consumirán los mensajes
    topic_name = 'test_topic'

    # Consumir los mensajes del topic especificado
    consume_messages(topic_name)
