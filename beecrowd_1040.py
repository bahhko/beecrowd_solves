n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (2 + 3 + 4 + 1)
print(f"Media: {media:.1f}")

if media >= 7.0:
   print("Aluno aprovado.")
elif media < 5.0:
   print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
   print("Aluno em exame.")
   n5 = float(input())
   print(f"Nota do exame: {n5:.1f}")
   
   media_nova = (media + n5) / 2
   
   if media_nova >= 5.0:
      print("Aluno aprovado.")
   else:
      print("Aluno reprovado.")
   print(f"Media final: {media_nova:.1f}")
