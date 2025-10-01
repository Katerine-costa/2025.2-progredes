# Operações bit a bit (bitwise) com strings em Python
strTexto_1 = 'P'
strTexto_2 = 'd'

print(f'Texto 1................: {strTexto_1} -> ASCII = {ord(strTexto_1):>3}')
print(f'Texto 2................: {strTexto_2} -> ASCII = {ord(strTexto_2):>3}')

# Operação AND bit a bit (&)
andResultado = ord(strTexto_1) & ord(strTexto_2)
print(f'strTexto_1 & strTexto_2: ACSII = {andResultado:>3} -> {chr(andResultado)}')

# Operação bit a bit

andResultado = ord(strTexto_1) & ord(strTexto_2)
orResultado  = ord(strTexto_1) | ord(strTexto_2)
xorResultado = ord(strTexto_1) ^ ord(strTexto_2)

# print(f'strTexto_1 & strTexto_2: ACSII = {andResultado:>3} -> {chr(andResultado)}')
print(f'strTexto_1 | strTexto_2: ACSII = {orResultado:>3} -> {chr(orResultado)}')
print(f'strTexto_1 ^ strTexto_2: ACSII = {xorResultado:>3} -> {chr(xorResultado)}')