from machine import Pin

motion = False

def handle_interrupt(pin):
  global motion
  motion = True
  global interrupt_pin
  interrupt_pin = pin 

pir1 = Pin(35, Pin.IN)
pir2 = Pin(34, Pin.IN)

pir1.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)
pir2.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

num = 0

while True:

  if motion:
    
    num = num + 1
    if num <= 50:
      state = machine.disable_irq()
      print(num)
      #utime.sleep_ms(1000)
      motion = False
      machine.enable_irq(state)  
    else:
      break