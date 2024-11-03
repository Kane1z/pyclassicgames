print("*coloque a idade da pessoa 999 para encerrar o programa")
valor = int(input("insira o numero de pessoas: "))
maisNovo = 0
nomeNovo = ""
for i in range(1,valor+1):
    print(i,"*"*50)
    nome = input("nome da pessoa:" )
    idade = int(input("insira a idade: "))
    cartaocid = input("Insira o Cartao de cidadao:") #pq isto esta aqui se nao vou utilizar
    if (i == 1):
        maisNovo = idade
        nomeNovo = nome
    elif(idade <= maisNovo):
        maisNovo = idade
        nomeNovo = nome
    elif(idade == 999):
        break
print("*"*53)
print("mais novo e", nomeNovo, "que tem", maisNovo)