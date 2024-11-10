def potten(base, expoe):
    return base ** expoe

# Entrada do usuário
num = int(input("Digite o número: "))
expo = int(input("Digite o expoente: "))

# Cálculo da potência
print(num," elevado a",expo,"é igual a",potten(num, expo))
