
# Crie um programa Python que recebe um array de números como argumento da linha de comando (CLI) (Terminal) e realiza as seguintes operações:

class Array_numeros:

    numeros = list(input("Digite os números que deseja:"))

    # Calcule e imprima a soma de todos os elementos do array:
    def soma_valores(numeros):

        soma = 0

        for num in numeros:
            soma += int(num)    
    
        return soma

    print('A soma dos valores digitados é:', type(soma_valores(numeros)))
    
    # Encontre o valor máximo no array e o exiba:
    def maior_valor(numeros):

        max_valor = 0
        n = 0

        for num in numeros:
            if str(max_valor) <= numeros[n]:
                max_valor = numeros[n]
                n+=1
        return max_valor

    print('O maior valor dessa lista é: ', maior_valor(numeros))

    # Inverta a ordem dos elementos no array e mostre o resultado:
    def lista_invertida(numeros):
        i = 0
        lista_invertida =[]
        for num in numeros:
            i-= 1
            lista_invertida += numeros[i]
        return lista_invertida

    print('Lista invertida: ', lista_invertida(numeros))