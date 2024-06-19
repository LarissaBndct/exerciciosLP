def ConverterF(f):
    c = (5/9) * (f - 32)
    return c

fht = float(input("insira a temperatura em F°: "))

celcius = ConverterF(fht)

print("A temperatura em C° é: ", celcius)