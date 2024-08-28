v1,v2,v3 = input().split()
v1 = int(v1)
v2 = int(v2)
v3 = int(v3)

ordem = [v1,v2,v3]
desordem = [v1,v2,v3]

ordem.sort()
print(ordem[0])
print(ordem[1])
print(ordem[2])
print("")
print(desordem[0])
print(desordem[1])
print(desordem[2])

