peso = float(input("\nDigite o peso da pessoa (kg): "))

engordar = peso * 0.15
emagrecer = peso * 0.20

peso_engordar = peso + engordar

peso_emagrecer = peso - emagrecer

print("\n===== Resultados =====")
print(f"\nSe engordar 15%: {peso_engordar:.2f} kg\n")
print(f"\nSe emagrecer 20%: {peso_emagrecer:.2f} kg\n\n")
