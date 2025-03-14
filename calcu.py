executar = True
while executar:
    escolhas = '''
            [1] ou [+] para Somar
            [2] ou [+] para Subtrair
            [3] ou [+] para Dividir
            [4] ou [+] para Multiplicar
            [5] para sair' 
            '''
    print(escolhas)
    operador = input("Qual sua opção?: ")
    n1 = input("Qual o primeiro Valor? ")
    n2 = input("Qual o segundo Valor? ")
    n1 = input(n1)
    n2 = input(n2)

    texto_sair = '''
            [1] Não, desejo sair!
            [2] Sim, desejo realizar outro calculo
            '''

    #Soma
    if operador == "1" or operador == "+" or operador == "Somar":
        resultado = n1 + n2
        print("Resultado da soma: " + str(resultado)) 
        print(texto_sair)
        operador = input("Desejar realizar outro calculo? ")
        if operador == "1":
            executar = False      

    #Subtração
    if operador == "2" or operador == "-" or operador == "Subtrair":
        resultado = n1 - n2
        print("Resultado da subtração: " - str(resultado))
        print(texto_sair)
        operador = input("Desejar realizar outro calculo? ")
        if operador == "1":
            executar = False
    #Divisão
    if operador == "3" or operador == "*" or operador == "Multiplicação":
        resultado = n1 / n2
        print("Resultado da Dividir: " - str(resultado))
        print(texto_sair)
        operador = input("Desejar realizar outro calculo? ")
        if operador == "1":
            executar = False

    #Multiplicação
    if operador == "4" or operador == "/" or operador == "Dividir":
        resultado = n1 * n2
        print("Resultado da Multiplicar: " - str(resultado))
        print(texto_sair)
        operador = input("Desejar realizar outro calculo? ")
        if operador == "1":
            executar = False

    #Sair
    if operador =="5" or "sair":
        print("Obrigado!")
        executar = False