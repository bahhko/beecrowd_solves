cod, quantidade = input().split()
cod = int(cod)
quantidade = int(quantidade)

resultado = 0

if cod == 1:
   resultado = quantidade * 4.00
elif cod == 2:
   resultado = quantidade * 4.50
elif cod == 3:
   resultado = quantidade * 5.00
elif cod == 4:
   resultado = quantidade * 2.00
elif cod == 5:
   resultado = quantidade * 1.50
   
print(f"Total: R$ {resultado:.2f}")
