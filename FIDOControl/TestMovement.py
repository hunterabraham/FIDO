from FIDOControl import FIDOMove
import time

fido = FIDOMove()

fido.setup()


fido.move(100, 'no', 1)
time.sleep(2.5)
fido.move(-100, 'no', 1)
time.sleep(2.5)
fido.move(100, 'left', 0.6)
time.sleep(5)
print('1')

fido.move(100, 'right', 0.6)
time.sleep(5)
fido.move(0, 'left', 1)
time.sleep(5)
fido.destroy()

