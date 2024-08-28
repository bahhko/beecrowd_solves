A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)

if (A + B > C) and (A + C > B) and (B + C > A):
   P = A + B + C
   print(f"Perimetro = {P:.1f}")
else:
   Area = ((A + B)*C)/2
   print(f"Area = {Area:.1f}")
   
