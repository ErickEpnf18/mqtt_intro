import random
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

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        # print(f"Msg received`{msg.payload.decode()}`from`{msg.topic}` topic")
        print(f"Msg payload: `{msg.payload.decode()}`from`{msg.topic}` topic")
    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()



