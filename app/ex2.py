"""
Desenvolva um programa Python que utilize um loop para imprimir os números de 1 a N 
(onde N é fornecido como argumento da linha de comando (Terminal) e, em seguida, 
imprima a soma desses números.
"""

class Loop_numeros:

    numero = int(input("Digite um número: "))

    def soma_numeros(numero):
        i = 1
        soma = 0

        while numero >= i:
            print(i)
            soma+=i
            i+=1
        return soma
        
    print("A soma dos números de 1 a n é: ", soma_numeros(numero))
