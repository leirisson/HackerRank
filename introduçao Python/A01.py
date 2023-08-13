numero = int(input("digite um valor: ").strip())

if numero % 2 != 0:
    print("impa")
elif numero >=2 and numero <=5:
    if numero % 2 ==0: 
        print(f'numero par')
elif numero >= 6 and numero <=20:
    if numero % 2 == 0:
        print("numero par")
elif numero > 20:
    if numero % 2 == 0:
        print('numero par')
