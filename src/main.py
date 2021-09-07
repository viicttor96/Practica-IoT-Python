from random import randint
from machine import unique_id, Pin
import utime
import neopixel
from umqtt.simple import MQTTClient
from ubinascii import hexlify
import json

def mqtt_cb(topic, msg):
    print(msg)

id_client = hexlify(unique_id())
client = MQTTClient(id_client, "broker.hivemq.com")
client.set_callback(mqtt_cb)
client.connect()
client.subscribe(b"JuegoIOT")
np = neopixel.NeoPixel(Pin(27), 1)
button = Pin(39, Pin.IN)

while True:
    client.check_msg()
    random_time = randint(0, 20)
    utime.sleep(random_time)
    np[0] = (255, 0, 128)
    np.write()
    starting_time = utime.ticks_ms()
    while button.value():
        continue
    else:
        elapsed_time = utime.ticks_diff(utime.ticks_ms(), starting_time)
        print(elapsed_time)
        score = {"score": elapsed_time}
        publication_json = json.dumps(score)
        client.publish(b"JuegoIOT", publication_json)
    np[0] = (0, 0, 0)
    np.write()
