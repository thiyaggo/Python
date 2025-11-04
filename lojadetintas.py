'''
progama que pede a quantidade de tintas e calcula o 
valor a ser pago e quantas latas de tintas vai ser usada.
'''
CUSTO_POR_LATA = 80
quantidade_metros = int(input("Digite a quantidade de metros quadrados: "))

litros, resto = divmod(quantidade_metros,3)

if resto > 0:
    litros += 1

latas, diferenca = divmod(litros,18)
if diferenca > 0:
    latas += 1

custo = latas * CUSTO_POR_LATA

print("A quantidade de latas a serem compradas é: ",latas)
print("O valor a ser gasto é: ", custo)