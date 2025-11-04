# programa que recebe o valor de alguns produtos soma e diz o total da compra
#recebe o valor total e diz o troco.

def realisar_venda():
    valor = 1
    contador =1
    total = 0.0

    while valor != 0:
        valor = float(input(f"Produto {contador}: R$ "))
        total += valor
        contador += 1
        
    print(f"Total = R${total:.2f}")
    dinheiro = float(input("Digite a quantidade de dinheiro a ser dado: "))
    print(f"Dinheiro ={dinheiro}")
    troco = dinheiro - total
    print(f"Troco ={troco: .2f}")


print("Lojas tabajara")
while True:
    controle = input("Quer fazer uma nova venda? digite s/n: ")
    if controle == 'n':
        break


    realisar_venda()

