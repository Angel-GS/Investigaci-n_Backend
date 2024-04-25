from confluent_kafka import Consumer, KafkaError
import emailManager


# Configuración del consumidor Kafka
config = {
    'bootstrap.servers': 'localhost:29092', 
    'group.id': 'email_consumers',
    'auto.offset.reset': 'earliest'
}

# Crear el consumidor Kafka
consumer = Consumer(config)

def consume_emails(topic):

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
            emailManager.processEmail(msg.value())
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


if __name__ == '__main__':
    # Especificar el topic del que se consumirán los mensajes
    topic_name = 'emails'

    # Consumir los mensajes del topic especificado
    consume_emails(topic_name)