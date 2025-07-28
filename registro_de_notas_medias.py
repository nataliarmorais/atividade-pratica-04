# Registro de notas e cálculo da média
notas = []
while True:
    entrada =input ("Digite uma nota de 0 a 10 (ou 'fim para encerrar):")
    if entrada.lower() == 'fim':
       break
    try: 
       nota = float(entrada)
       if 0 <= nota <= 10:
           notas.append(nota)
       else:
           print("Nota fora do intervalo permitido.")
    except ValueError:
        print("Entrada inválida. Digite um numero ou 'fim'.")


if notas:
    media = sum (notas)/len(notas)
    print(f"A média das notas é: {media:.2f}")
    print(f"Notas registradas: {notas}")
else: 
    print("Nenhuma nota valida registrada.")