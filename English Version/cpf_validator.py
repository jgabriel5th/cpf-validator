import sys

typed_cpf = ''
cpf_list = []
while len(cpf_list) < 11:
    try:
        cpf = input('Type a CPF(One number at a time): ')
        if len(cpf) == 1:
            int_cpf = int(cpf)
            cpf_list.append(int_cpf)
            print(*cpf_list)
            typed_cpf += cpf
            validated_cpf = typed_cpf[:9]
        else:
            print('Only one number at a time is permitted')
    except ValueError:
        print('Only integer numbers are allowed')

repeated_cpf = typed_cpf == typed_cpf[0] * len(typed_cpf)
if repeated_cpf:
    print('You typed repeated numbers.')
    sys.exit()
    
countdown = 10
result = 0
for number in validated_cpf:
    result += int(number) * countdown
    countdown -= 1

final_result = (result * 10) % 11
first_digit = 0 if final_result > 9 else final_result


validated_cpf = f'{typed_cpf[:9]}{first_digit}'
countdown2 = 11
result2 = 0
for number2 in validated_cpf:
    result2 += int(number2) * countdown2
    countdown2 -= 1

final_result2 = (result2 * 10) % 11
second_digit = 0 if final_result2 > 9 else final_result2
validated_cpf = f'{typed_cpf[:9]}{first_digit}{second_digit}'

if validated_cpf == typed_cpf:
    print('Your CPF is valid!')
else:
    print('Your CPF is not valid')