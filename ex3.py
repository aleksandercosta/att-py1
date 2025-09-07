salario_minimo = float(input("Digite o valor do salário mínimo: R$ "))
salario_funcionario = float(input("Digite o valor do salário do funcionário: R$ "))

quantidade = salario_funcionario / salario_minimo

print("\n===== Resultado =====\n")
print(f"O funcionário ganha {quantidade:.2f} salários mínimos.\n")
