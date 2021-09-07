# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
# import uos
# uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()


from machine import Pin
import neopixel
import utime
import network
from credenciales import ssid, password

# Configurar hardware
led = neopixel.NeoPixel(Pin(27), 1)
boton = Pin((39), Pin.IN)

# Conectando a la wifi
led[0] = (255, 0, 0)  # led encendido en rojo a la espera de que se conecte.
led.write()
print("\nConectando a {} ...".format(ssid), end='')
red = network.WLAN(network.STA_IF)
red.active(True)
red.connect(ssid, password)
while not red.isconnected():  # Espera hasta que este conectado
    utime.sleep_ms(100)
print("conectado!")
print(red.ifconfig())   # ver la ip que se nos ha asignado por DHCP
led[0] = (0, 255, 0)    #se enciende 0.1s en verde para mostrar que se ha conectado.
led.write()
utime.sleep_ms(150)
led[0] = (0,0,0)
led.write()