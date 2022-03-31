from machine import Pin, ADC
import utime
from math import log
sensor_temp = machine.ADC(27)
pote_temp = machine.ADC(28)
conversion_factor = 3.3 / (65535)
L1 = Pin(9, Pin.OUT)
L2 = Pin(10, Pin.OUT)
Pir = Pin(2, Pin.IN)
B1 = Pin(17, Pin.OUT)
B = 3950
R = 10000
T0 = 298

while True:
  Reads = sensor_temp.read_u16() * conversion_factor
  Rn = ((Reads*R)/(3.3-Reads))
  Tk = ((T0*B)/(T0*log(Rn/R)+B))
  Readp = pote_temp.read_u16() * conversion_factor
  Tp = (Readp*35)/3.3
  Tc = Tk - 273
  if (Tp < Tc):
    L1.on()
    L2.off()
  if (Tp > Tc):
    L1.off()
    L2.on()
  if (Pir.value()==1):
    B1.on()
    utime.sleep(5)
    B1.off()
  utime.sleep(0.1)