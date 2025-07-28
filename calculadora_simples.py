# Calculadora Simples com tratamento de erros

while True:
    try:
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))
        operacao = input("Escolha a operação (+, -, *, /):")
        
        if operacao == '+':
           resultado = num1 + num2
        elif operacao == '-':
           resultado = num1 - num2
        elif operacao == '*':
           resultado = num1 * num2
        elif operacao == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Operação inválida. Tente novamente.")
                continue

        print(f"Resultado:, {resultado:2f}")
        break
    except ValueError:
        print("Entrada inválida. Por favor, use apenas números reais.")
        