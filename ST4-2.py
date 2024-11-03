
lista=[]
# adiciono masi um item a lista com append e introduzo o valor do input
for i in range(10):
    lista.append(int(input(str(i+1)+" valor:")))
print('*'*20)
lista.sort()
print("lista:", lista)