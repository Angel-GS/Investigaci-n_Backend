KAFKA_CONFIG = {
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'email_consumers',
    'auto.offset.reset': 'earliest'
}

SMTP_CONFIG = {
    'server': 'smtp.gmail.com',
    'port': 587,
    'login_email': 'paratektechnologies@gmail.com',
    'login_password': 'syoujglncixqqfbg'
}

URGENT_MAILBOX = 'raulmirandavargas82@gmail.com'