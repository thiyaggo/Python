# faca 5 perguntas pra saber a condição do indivídou.
analise =0
perguntas = [
    "Telefonou para vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vitima? ",
    "Já trabalhou cam a vítima? "
]

for pergunta in perguntas:
    resposta = input(pergunta)
    resposta = 1 if resposta == 's' else 0
    analise += resposta

if analise == 2:
    print("Clasificação suspeita: ")
elif analise == 3 or analise == 4:
    print("Clasificação cúmplice: ")
elif analise == 5:
    print("Clasificação assassino: ")    
else: print("Clasificação inocentes: ")