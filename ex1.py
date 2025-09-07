salario_fixo = float(input("\nDigite o salário fixo do funcionário: R$ "))
vendas = float(input("\nDigite o valor total das vendas: R$ "))

comissao = vendas * 0.04

salario_final = salario_fixo + comissao

print("\n===== Resultado =====")
print(f"\nComissão: R$ {comissao:.2f}\n")
print(f"Salário final: R$ {salario_final:.2f}\n\n")
