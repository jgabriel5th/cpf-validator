cpf_list = []
while len(cpf_list) < 9:
    try:
        cpf = input('Type the first 9 digits of a CPF(One number at a time): ')
        if len(cpf) == 1:
            int_cpf = int(cpf)
            cpf_list.append(int_cpf)
            print(*cpf_list)
        else:
            print('Only one number at a time is permitted')
    except ValueError:
        print('Only integer numbers are allowed')
countdown = 10
results = []

for number in cpf_list:
    result = number * countdown
    results.append(result)
    countdown -= 1

number2 = 0
for number1 in results:
    number2 += number1
    sum_result = number2

calculation_result = (sum_result * 10) % 11
first_digit = 0 if calculation_result > 9 else calculation_result
print(f'The first digit of the CPF is: {first_digit}')
cpf_list.append(first_digit)

countdown1 = 11
results1 = []

for number in cpf_list:
    result1 = number * countdown1
    results1.append(result1)
    countdown1 -= 1

number3 = 0
for number4 in results1:
    number3 += number4
    sum_result2 = number3

calculation_result1 = (sum_result2 * 10) % 11
second_digit = 0 if calculation_result1 > 9 else calculation_result1
print(f'The second digit of the CPF is: {second_digit}')
cpf_list.append(second_digit)
print("Here's your validated CPF:", *cpf_list)
