"""
Crie um programa Python que recebe uma string como argumento da linha de comando e realiza as seguintes operações:
Imprima o comprimento da string.
Converta todos os caracteres para maiúsculas. (Criar o método de converter caracteres minúsculos para maiúsculo)
Substitua todas as vogais por '*' na string e exiba o resultado.

"""
valor_str = input("Digite qualquer coisa que desejar: ")
valor_list = list(valor_str)
comprimento = 0
nova_string = ''

for valor in valor_list:
    
    if valor_list[comprimento] == 'a' or valor_list[comprimento] == 'e' or valor_list[comprimento] == 'i' or valor_list[comprimento] == 'o' or valor_list[comprimento] == 'u':
        valor_list[comprimento] = "*"
        nova_string += valor_list[comprimento]
    else:
        nova_string += valor_list[comprimento].upper()
        
    comprimento+=1

print('O comprimento da string é: ', comprimento)
print('A nova string é: ', nova_string)
