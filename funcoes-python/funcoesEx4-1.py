def ConverterF(f):
    c = (5/9) * (f - 32)
    return c


for fht in range(101):
    celcius = ConverterF(fht)
    print(f"A temperatura {fht:.2f} F° em C° é: {celcius:.2f}")
    #descobri que f antes da string tem a mesma funçao do $ no c# 