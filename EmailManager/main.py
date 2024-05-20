from services.KafkaConsumer import KafkaConsumer
from config.config import KAFKA_CONFIG

if __name__ == '__main__':
    topic_name = 'emails'
    consumer = KafkaConsumer(KAFKA_CONFIG, topic_name)
    consumer.consume_emails()