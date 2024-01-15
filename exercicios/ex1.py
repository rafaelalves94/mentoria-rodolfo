
# Crie um programa Python que recebe um array de números como argumento da linha de comando (CLI) (Terminal) e realiza as seguintes operações:

# Calcule e imprima a soma de todos os elementos do array:
numeros = list(input("Digite os números que deseja:"))
soma = 0
max_valor = 0
n = 0

for num in numeros:
    soma += int(num)
    if str(max_valor) <= numeros[n]:
        max_valor = numeros[n]
    n+=1

print(f'A soma dos valores digitados é: {soma}')
    
# Encontre o valor máximo no array e o exiba:
print(f'O maior valor dessa lista é: {max_valor}')

# Inverta a ordem dos elementos no array e mostre o resultado:
i = 0
lista_invertida =[]
for num in numeros:
    i-= 1
    lista_invertida += numeros[i]

print('Lista invertida: ', lista_invertida)