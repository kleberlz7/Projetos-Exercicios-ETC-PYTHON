valor = float(input())
valor2 =float(valor)
valor_formatado = f"{valor:.2f}"

if valor > 0 :
    print("Deposito realizado com sucesso! \nSaldo atual:R$", valor_formatado)
   

elif  valor < 0:
    print("Valor invalido! Digite um valor maior que zero.")

elif valor == 0:
    print("Encerrando o programa...")

