def potten(base, expoe):
    return base ** expoe # base^expo


num = int(input("Digite o número: "))
expo = int(input("Digite o expoente: "))


print(num," elevado a",expo,"é igual a",potten(num, expo))
