from confluent_kafka import Consumer, KafkaError
from core.EmailProcessor import process_email # type: ignore

class KafkaConsumer:
    def __init__(self, config, topic):
        self.consumer = Consumer(config)
        self.topic = topic

    def consume_emails(self):
        self.consumer.subscribe([self.topic])
        
        try:
            while True:
                msg = self.consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        print(msg.error())
                        break
                process_email(msg.value())
        except KeyboardInterrupt:
            pass
        finally:
            self.consumer.close()