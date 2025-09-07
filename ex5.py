ano_nascimento = int(input("\nDigite o ano de nascimento: "))
ano_atual = int(input("\nDigite o ano atual: "))

idade_anos = ano_atual - ano_nascimento

idade_meses = idade_anos * 12

idade_dias = idade_anos * 365

idade_semanas = idade_dias // 7

print("\n\n===== Idade da pessoa =====")
print(f"\nIdade em anos: {idade_anos} anos")
print(f"\nIdade em meses: {idade_meses} meses")
print(f"\nIdade em dias: {idade_dias} dias")
print(f"\nIdade em semanas: {idade_semanas} semanas\n")