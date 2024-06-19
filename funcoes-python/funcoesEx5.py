def NovoSalario(salario):
    acrescimo = 0
    if salario <= 1500:
        acrescimo = salario * 0.15
    elif salario > 1500 and salario <= 3000:
        acrescimo = 0.1
    elif salario > 3000:
        acrescimo = salario * 0.05

    return salario + acrescimo

sal = float(input("Insira o salário: "))
novoSalario = NovoSalario(sal)
print(f"O novo salario é de: R${novoSalario:.2f}")