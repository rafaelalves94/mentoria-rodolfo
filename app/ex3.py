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

def conversor_caracteres(valor_list):
    match valor_list[comprimento]:
        case 'b':
            valor_list[comprimento] = 'B'
        case 'c':
            valor_list[comprimento] = 'C'
        case 'd':
            valor_list[comprimento] = 'D'
        case 'f':
            valor_list[comprimento] = 'F'
        case 'g':
            valor_list[comprimento] = 'G'
        case 'h':
            valor_list[comprimento] = 'H'
        case 'j':
            valor_list[comprimento] = 'J'
        case 'k':
            valor_list[comprimento] = 'K'
        case 'l':
            valor_list[comprimento] = 'L'
        case 'm':
            valor_list[comprimento] = 'M'
        case 'n':
            valor_list[comprimento] = 'N'
        case 'p':
            valor_list[comprimento] = 'P'
        case 'q':
            valor_list[comprimento] = 'Q'
        case 'r':
            valor_list[comprimento] = 'R'
        case 's':
            valor_list[comprimento] = 'S'
        case 't':
            valor_list[comprimento] = 'T'
        case 'v':
            valor_list[comprimento] = 'V'
        case 'x':
            valor_list[comprimento] = 'X'
        case 'y':
            valor_list[comprimento] = 'Y'
        case 'z':
            valor_list[comprimento] = 'Z'
        case 'ç':
            valor_list[comprimento] = 'Ç'
        case 'ñ':
            valor_list[comprimento] = 'Ñ'
    return valor_list[comprimento]       

for valor in valor_list:
    
    if valor_list[comprimento] == 'a' or valor_list[comprimento] == 'e' or valor_list[comprimento] == 'i' or valor_list[comprimento] == 'o' or valor_list[comprimento] == 'u'  or valor_list[comprimento] == 'ã'  or valor_list[comprimento] == 'õ'  or valor_list[comprimento] == 'í'  or valor_list[comprimento] == 'ì'  or valor_list[comprimento] == 'á'  or valor_list[comprimento] == 'à'  or valor_list[comprimento] == 'é'  or valor_list[comprimento] == 'è'  or valor_list[comprimento] == 'ú'  or valor_list[comprimento] == 'ù'  or valor_list[comprimento] == 'â'  or valor_list[comprimento] == 'ô':
        valor_list[comprimento] = "*"
        nova_string += valor_list[comprimento]
    else:
        nova_string += conversor_caracteres(valor_list)
    comprimento+=1

print('O comprimento da string é: ', comprimento)
print('A nova string é: ', nova_string)
