import sys

try:
    intvalor = int(input("digite um valor inteiro. "))
except ValueError:
    sys.exit("valor inválido. digite outro valor.")
except KeyboardInterrupt:
    sys.exit('\nPrograma interrompido pelo usuario.')
except Exception as erro:
    sys.exit('Erro inesperado: {erro}')
else:
    # imprimir o valor binário do numero interio
    print(f'\n{intvalor} em binário: {bin(intvalor)}\n')

    intQuantidade = intvalor.bit_length()

    binvalor = bin(intvalor)[2:]

    if