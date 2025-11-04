from collections import Counter
print("Pesquisa sobre SO")

lista_resposta = []

while True:
    resposta = int(input("Qual o melhor sistema operacional para servidores?\n"))
    if resposta == 0:
        break
    if resposta >6 or resposta < 0:
        continue
    lista_resposta.append(resposta)

valores = Counter(lista_resposta)

total = 0
for key in valores:
    total += valores[key]

mapa_nomes = {
    1:'windows',
    2:'unix',
    3:'linux',
    4:'netware',
    5:'mac os',
    6:'outro',
}

for nome in valores:
    porcentagem =(valores[nome]*100)/total
    print(f"{mapa_nomes[nome]}     {valores[nome]}  {porcentagem}%")
