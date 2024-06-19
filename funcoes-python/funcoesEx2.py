def CalculoImc(altura, peso):
    imc = peso / altura**2
    print("IMC: ", imc)

a = float(input("Insira a altura: "))
p = float(input("Insira o peso: "))

CalculoImc(a, p)