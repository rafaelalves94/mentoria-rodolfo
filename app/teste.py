class Conversor:
    valor_str = input("Digite qualquer coisa que desejar: ")
    valor_list = list(valor_str)

    @staticmethod
    def tamanho(valor_list):
        i = 0
        for valor in valor_list:
            i += 1
        return i

    @staticmethod
    def conversor_caracteres(valor_list):
        comprimento = Conversor.tamanho(valor_list)

        if comprimento > 0:
            # Corrigindo o índice para não ultrapassar o limite da lista
            if valor_list[comprimento - 1] == 'b':
                valor_list[comprimento - 1] = 'B'

        # Corrigindo para imprimir a lista completa após a conversão
        print('String após a conversão:', ''.join(valor_list))

    # Chamando os métodos estáticos
    tamanho_resultado = tamanho(valor_list)
    print('O comprimento da string é: ', tamanho_resultado)

    conversor_caracteres(valor_list)