import secrets

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_characters = "!@#$%^&*()-_=+[]{}/;:,.<>?"
password_list = []
x = 1
all_characters = upper_case + lower_case + numbers + special_characters
random_generator = secrets.SystemRandom()

while True:
    try:
        number_characters = int(input("Digite o número de caracteres que deseja na senha: "))
        if number_characters <= 0:
            print(f"Por favor, insira um número maior que 0.")
            continue
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")
        continue

    password = "".join(random_generator.choices(all_characters, k=number_characters))
    password_list.append(f'Senha {x}: {password}')
    print(f'Essa é a senha gerada: {password}')
    x += 1

    while True:
        another_password = input("Deseja gerar outra senha? (s/n): ").strip().lower()
        if another_password == 's':
            break
        elif another_password == 'n':
            print('Encerrando o programa...')
            password_list_formatted = '\n'.join(password_list)
            print('==============Obrigado===============')
            print('Aqui estão as senhas geradas:')
            print(password_list_formatted)
            print('=====================================')
            exit()
        else:
            print("Entrada inválida! Por favor, digite 's' para sim ou 'n' para não.")
            