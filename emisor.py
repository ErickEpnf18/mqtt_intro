import random 
import time
from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
topic = "/home/rooms/room1"

#generate id client
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'usuario'
# password = 'passwd'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connetion successful with MQTT Broker")
        else:
            print("Connection failure, return code {}".format(rc))

    client = mqtt_client.Client(client_id)
    # Client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 1
    while(True):
        time.sleep(2)
        # msg = f"My message from emisor: {msg_count}"
        # msg = input('Please enter your msg[{}]: '.format(msg_count))
        msg = random.randrange(50, 100)
        result = client.publish(topic, msg)
        # result : [0, 1]
        status = result[0]
        if status == 0:
            print("Sent: humidity {} & the topic{}".format(msg, topic))
        else:
            print("Not sent! the topic{}".format(msg, topic))
        msg_count +=1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
if __name__ == '__main__':
    run()



