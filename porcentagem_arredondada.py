inicial = float(input())
juros = float(input())
periodo= int(input())
valorFinal = inicial * (1+juros)**periodo 
valorFinalArredondado = round(valorFinal, 2)
valorFormatado = "R$ {:.2f}".format(valorFinalArredondado)

print("Valor final do investimento: " + valorFormatado)
