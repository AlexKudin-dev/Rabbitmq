import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')



channel.basic_publish(exchange='',
                      body="Hello World",
                      routing_key='hello')

print(" [x] Sent 'Hello World!'")
connection.close()


