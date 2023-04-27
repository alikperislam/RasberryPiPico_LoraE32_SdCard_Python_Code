import machine
import sdcard
import uos
from machine import UART
from machine import Pin
import _thread
import utime
# sd card -----------------------------------
cs = machine.Pin(13, machine.Pin.OUT)
spi = machine.SoftSPI(
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(10),
                  mosi=machine.Pin(11),
                  miso=machine.Pin(12))
sd = sdcard.SDCard(spi, cs)
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")
# sd card -----------------------------------

sayi = 0

def lora_tx():
    while True:
        lora = UART(0,9600)
        lora.write("Lora data : {}\r\n".format(sayi))
        print("Lora writing...")
        utime.sleep(0.3)       
_thread.start_new_thread(lora_tx,()) #multithreading - core1


with open("/sd/test03.txt", "w") as file: #multithreading - core2
    while True:
        file.write("Sd card data : {}\r\n".format(sayi))
        print("Sd card writing...")
        utime.sleep(0.3)