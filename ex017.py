import math
co = float(input('comprimento do cateto oposto;'))
ca = float(input('comprimento do cateto adjacente'))
hi = int(math.hypot(co, ca))
print('A hipotenusa vai medir {}'.format(hi))
