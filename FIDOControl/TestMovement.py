from FIDOControl import FIDOMove


fido = FIDOMove()

fido.setup()

fido.move('forward', None)
fido.move('backward', None)
fido.move('forward', 'left')
fido.move('forward', 'right')
fido.move('backward', 'left')
fido.move('backward', 'left')
fido.destroy()

