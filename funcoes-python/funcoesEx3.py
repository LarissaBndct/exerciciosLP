def MaiorValor(v1,v2,v3):
    if v1 > v2 and v1 > v3:
        return v1
    elif v2 > v1 and v2 > v3:
        return v2
    elif v3 > v1 and v3 > v2:
        return v3
    
def MenorValor(v1,v2,v3):
    if v1 < v2 and v1 < v3:
        return v1
    elif v2 < v1 and v2 < v3:
        return v2
    elif v3 < v1 and v3 < v2:
        return v3
    
def MediaValor(v1,v2,v3):
    media = (v1 + v2 + v3)/3
    return media

valor1 = float(input("insira o primeiro valor: "))
valor2 = float(input("insira o segundo valor: "))
valor3 = float(input("insira o terceiro valor: "))

maiorValor = MaiorValor(valor1, valor2, valor3)
menorValor = MenorValor(valor1, valor2, valor3)
mediaValor = MediaValor(valor1, valor2, valor3)

resultado = ""
if(valor1 == valor2 == valor3):
    resultado = "Todos os valores são iguais"
else:
    resultado = "o maior valor é: ", maiorValor, ", o menor valor é: ", menorValor, " e a média dos tres valores é: ", mediaValor

print(resultado)
