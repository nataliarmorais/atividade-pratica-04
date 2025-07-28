# Classificador de pares e ímpares

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'sair' para encerrar): ")
    if entrada.lower() == "fim":
        break
    
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print("Esse número é par.")
            pares += 1
            print(f"{numero} é par.")
        else:
            print("Esse número é ímpar.")
            impares += 1
    except ValueError:
        print ("Entrada inválida. Por favor, digite um número inteiro ou 'fim' para encerrar.")
        
print(f"\nTotal de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
