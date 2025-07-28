# Verificador de força de senha
import re
while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower()=="sair":
        print("Encerrando o programa...")
        break
    if len(senha) < 8:
        print ("Senha fraca : menos de 8 caracteres")
        continue
    if not re.search(r"\d", senha):
        print("Senha fraca : deve conter pelo menos um número")
        continue
    print("Senha forte! Segurança aprovada.")
    break
    