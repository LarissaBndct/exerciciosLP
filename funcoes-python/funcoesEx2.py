def CalculoImc(altura, peso):
    imc = peso / altura**2
    print("IMC: ", imc)

def Classificacao(imc):
    if imc < 22:
        print("Magro")
    elif imc > 27:
        print("Gordo")
    else:
        print("Ideal")

a = float(input("Insira a altura: "))
p = float(input("Insira o peso: "))

valor = CalculoImc(a, p)
Classificacao(valor)