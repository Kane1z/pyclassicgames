maior= 0
menor = None
lista=[None]*10 #defino o tamanho da litsa
for i in range(len(lista)):
    lista[i] = int(input(str(i+1)+" valor:"))
    if(i == 0 ):
        menor = lista[i] #primtio numro caso comese o porgrama
    elif(lista[i] < menor):
        menor = lista[i] #verifica qual o menor numero com o primeiiro ja adicionado
    elif(lista[i] > maior):
        maior = lista[i]#apos passar para o segundo num ele vai agora comprar com o primiro
#output do projeto ;)
print('*'*20)
print("pares:",end = " ")
for i in range(len(lista)):  #compara se o numero é par vendo se o resto é 0
    if(lista[i] % 2 == 0):
        print(lista[i],end = " " )
print("\nmenor:",menor)
print("maior:",maior)
print("diferenca:",maior - menor)