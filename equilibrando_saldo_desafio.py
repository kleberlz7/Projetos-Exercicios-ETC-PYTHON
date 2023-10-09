# Saldo atual da conta
saldoAtual = in(input())
# Valor do deposito
valorDeposito = in(input())

# Valor da retirada
valorRetirada = in(input())

# Saldo final com casa decimal
novoSaldo = round(saldoAtual + valorDeposito - valorRetirada, 1)

# Saldo final
print(f"Saldo atualizado na conta: {novoSaldo:.1f}")