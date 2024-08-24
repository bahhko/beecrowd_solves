entrada = input().split() #le e separa

A, B, C, D = map(int, entrada) #converte e atribui

CD = C + D
AB = A + B
par = A % 2

if B > C and D > A and CD > AB and C >= 0 and D >= 0 and par == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")