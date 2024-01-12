salario = float(input("Digite o salário: "))
aumento = float(input("Digite o percentual de aumento: "))
novo_salario = salario + (salario / 100 * aumento)
print(f"O novo salário é: R${novo_salario:,.2f}")
