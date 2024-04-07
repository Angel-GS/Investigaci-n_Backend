from confluent_kafka import Producer
import time

# Configuración del productor Kafka
config = {
    'bootstrap.servers': 'localhost:29092',  # Cambiar si es necesario
}

# Crear el productor Kafka
producer = Producer(config)


def delivery_report(err, msg):
    """ Callback llamado una vez que el mensaje se envía o falla """
    if err is not None:
        print(f'Error al enviar el mensaje: {err}')
    else:
        print(f'Mensaje enviado: {msg.value()}')


def produce_messages(topic, messages):
    """ Función para producir mensajes """
    for index in range(0, 5):
        for message in messages:
            # Enviar el mensaje al topic
            producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
            producer.poll(0.5)  # Permitir que el productor maneje eventos
            time.sleep(1)  # Esperar un segundo entre los mensajes


if __name__ == '__main__':
    # Especificar el topic al que se enviarán los mensajes
    topic_name = 'test_topic'

    # Lista de mensajes a enviar
    messages_to_send = [
        'Hola Kafka!',
        'Este es un mensaje de prueba.',
        '¿Cómo estás?',
        '¡Adiós!'
    ]

    # Producir los mensajes en el topic especificado
    produce_messages(topic_name, messages_to_send)
