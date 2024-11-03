lista=[10,8,7,6,5,4,3,2,1,0,12,3] #coloquei 2 num 3 para mostrar que ele pega o todos o numeros da array
print(lista)

num = int(input("numero pra procurar:"))
print("o numero", num, "foi encontrado")
for i in range(len(lista)):
    if (num == lista[i]):
        print("posicao",i+1)


