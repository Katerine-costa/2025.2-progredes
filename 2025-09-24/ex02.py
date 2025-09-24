# Gerar a mascara  -------  # Deslocamento binario

intCIDR = 24

intMask = 0xffffffff

intMask = intMask >> (32 - intCIDR)   # deslocamento binario

intMask = intMask << (32 - intCIDR)   # deslocamento binario

print(intMask)

# Será impresso -> 4294967040 (4.294.967.040)

# ----------------------------------------------------------- #

# Forma simplificada #

# intMask = 0xffffffff >> (32 - intCIDR) << (32 - intCIDR)