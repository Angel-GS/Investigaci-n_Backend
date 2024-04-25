from confluent_kafka import Producer
import time

# Configuración del productor Kafka
config = {
    'bootstrap.servers': 'localhost:29092',
}

# Crear el productor Kafka
producer = Producer(config)


def delivery_report(err, msg):
    if err is not None:
        print(f'Error al enviar el mensaje: {err}')
    else:
        print(f'Mensaje enviado: {msg.value()}')


def produce_emails(topic, message):
    # Enviar el mensaje al topic
    producer.produce(topic, message, callback=delivery_report)
    producer.poll(0.5)  # Permitir que el productor maneje eventos
    time.sleep(1)  # Esperar un segundo entre los mensajes
