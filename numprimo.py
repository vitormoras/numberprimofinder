#verificação de números primos
#num primos tem somente 2 divisores

numero = int(input("Digite um número: "))
divisores = []
for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)

if len(divisores) == 2:
        print(f" {numero} É um numero primo")
else:
        print(f'{numero} não é primo!')
 