"""
Desenvolva um programa Python que utilize um loop para imprimir os números de 1 a N (onde N é fornecido como argumento da linha de comando (Terminal) e, em seguida, 
imprima a soma desses números.
"""

numero = int(input("Digite um número: "))
i = 1
soma = 0

while numero >= i:
    print(i)
    soma+=i
    i+=1

print("A soma dos números de 1 a n é: ", soma)
