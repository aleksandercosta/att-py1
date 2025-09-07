salario = 1200.00
c1 = 200.00
c2 = 120.00
multa = 0.02

c1_atrasada = c1 + (c1 * multa)
c2_atrasada = c2 + (c2 * multa)

saldo_restante = salario - (c1_atrasada + c2_atrasada)

print(f"\n\nSaldo restante do salário: R$ {saldo_restante:.2f}\n\n")