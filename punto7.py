print("¡Bienvenido al programa de declaración de renta")
renta = int(input("Por favor ingrese el valor de su renta anual: "))
if renta > 0 and renta <= 1000000:
    print("Su impositivo es de 5%")
elif renta > 1000000 and renta <= 2000000:
    print ("Su impositivo es de 15%")
elif renta > 2000000 and renta <= 3500000:
    print("Su impositivo es de 20%")
elif renta > 3500000 and renta <= 6000000:
    print("Su impositivo es de 30%")
else:
    print("Su impositivo es de: 45%")
