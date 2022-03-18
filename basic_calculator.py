import os
while True:
    
    operacao = input("Qual operação(+, -, *, /)? ou \"s\"para sair: ")
    if operacao == "s" or operacao == "s":
        break
        
    if operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/":
                
        x = int(input("Digite um número: "))
        
        y = int(input("Digite um número: "))
        
        if operacao == "+":
            result = x + y
        
        elif operacao == "-":
            result = x - y
        
        elif operacao == "*":
            result = x * y
        
        elif operacao == "/":
            result = x / y
        
        else:
            print("Operação não suportada")

        print(result)
        
        input("Presione Enter para limpar")

            