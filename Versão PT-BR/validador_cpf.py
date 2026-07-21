cpf_digitado = ''
lista_cpf = []
while len(lista_cpf) < 11:
    try:
        cpf = input('Digite um CPF(Um número por vez): ')
        if len(cpf) == 1:
            int_cpf = int(cpf)
            lista_cpf.append(int_cpf)
            print(*lista_cpf)
        else:
            print('Apenas um número por vez é permitido')
        cpf_digitado += cpf
        cpf_validado = cpf_digitado[:9]
    except ValueError:
        print('Apenas números inteiros são permitidos')

contagem = 10
resultado = 0
for numero in cpf_validado:
    resultado += int(numero) * contagem
    contagem -= 1

resultado_final = (resultado * 10) % 11
primeiro_digito = 0 if resultado_final > 9 else resultado_final

cpf_validado = f'{cpf_digitado[:9]}{primeiro_digito}'
contagem2 = 11
resultado2 = 0
for numero2 in cpf_validado:
    resultado2 += int(numero2) * contagem2
    contagem2 -= 1

resultado_final2 = (resultado2 * 10) % 11
segundo_digito = 0 if resultado_final2 > 9 else resultado_final2
cpf_validado = f'{cpf_digitado[:9]}{primeiro_digito}{segundo_digito}'

if cpf_validado == cpf_digitado:
    print('Seu CPF é válido!')
else:
    print('Seu CPF não é válido!')