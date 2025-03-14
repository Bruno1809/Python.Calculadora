executar = True
while executar:
    escolhas = '''
            [1] ou [+] para Somar
            [2] ou [-] para Subtrair
            [3] ou [/] para Dividir
            [4] ou [*] para Multiplicar
            [5] para sair
            '''
    print(escolhas)
    operador = input("Qual sua opção?: ")

    # Entrada dos números com conversão para float
    try:
        n1 = float(input("Qual o primeiro Valor? "))
        n2 = float(input("Qual o segundo Valor? "))
    except ValueError:
        print("Por favor, insira valores numéricos válidos!")
        continue

    texto_sair = '''
            [1] Não, desejo sair!
            [2] Sim, desejo realizar outro cálculo
            '''

    # Soma
    if operador == "1" or operador == "+" or operador.lower() == "somar":
        resultado = n1 + n2
        print("Resultado da soma: " + str(resultado)) 
        print(texto_sair)
        operador = input("Deseja realizar outro cálculo? ")
        if operador == "1":
            executar = False      

    # Subtração
    elif operador == "2" or operador == "-" or operador.lower() == "subtrair":
        resultado = n1 - n2
        print("Resultado da subtração: " + str(resultado))
        print(texto_sair)
        operador = input("Deseja realizar outro cálculo? ")
        if operador == "1":
            executar = False

    # Divisão
    elif operador == "3" or operador == "/" or operador.lower() == "dividir":
        if n2 == 0:
            print("Não é possível dividir por zero!")
        else:
            resultado = n1 / n2
            print("Resultado da divisão: " + str(resultado))
        print(texto_sair)
        operador = input("Deseja realizar outro cálculo? ")
        if operador == "1":
            executar = False

    # Multiplicação
    elif operador == "4" or operador == "*" or operador.lower() == "multiplicar":
        resultado = n1 * n2
        print("Resultado da multiplicação: " + str(resultado))
        print(texto_sair)
        operador = input("Deseja realizar outro cálculo? ")
        if operador == "1":
            executar = False

    # Sair
    elif operador == "5" or operador.lower() == "sair":
        executar = False