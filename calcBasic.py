while True:

    def adi(num1, num2):
        resul = num1 + num2
        print(str(num1) + ' + ' + str(num2) + ' = ' + str(resul))

    def sub(num1, num2):
        resul = num1 - num2
        print(str(num1) + ' - ' + str(num2) + ' = ' + str(resul))

    def mult(num1, num2):
        resul = num1 * num2
        print(str(num1) + ' * ' + str(num2) + ' = ' + str(resul))

    def div(num1, num2):
        resul = num1 / num2
        print(str(num1) + ' / ' + str(num2) + ' = ' + str(resul))

    print('(1) + Adição')
    print('(2) - Subtração')
    print('(3) * Multiplicação')
    print('(4) / Divisão')
    print('(0) Sair!')

    op = int(input('Escolha uma opção: '))

    if op == 1:
        print('Adição')
        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('Informe o segundo número: '))
        adi(num1, num2)
    elif op == 2:
        print('Subtração')
        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('Informe o segundo número: '))
        sub(num1, num2)
    elif op == 3:
        print('Multiplicação')
        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('Informe o segundo número: '))
        mult(num1, num2)
    elif op == 4:
        print('Divisão')
        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('Informe o segundo número: '))
        div(num1, num2)
    elif (op >= 5):
        print('Opção inválida!!!')
        break
    if not (op == 1 or op == 2 or op == 3 or op == 4):
        print('Calculadora finalizada')
        break
