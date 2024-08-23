valor = float(input())

if not (0 <= valor <= 1000000.00):
    print("Valor invalido")
else:
    #valor * 100 pq se não essa bosta da erro e fica mais facil de lidar
    valor = int(round(valor * 100))
    
    #aqui tambem faz * 100
    notas = [10000, 5000, 2000, 1000, 500, 200]
    nomes_notas = ["R$ 100.00", "R$ 50.00", "R$ 20.00", "R$ 10.00", "R$ 5.00", "R$ 2.00"]
    
    #aqui tambem
    moedas = [100,50,25,10,5,1]
    nomes_moedas = ["R$ 1.00", "R$ 0.50", "R$ 0.25", "R$ 0.10", "R$ 0.05", "R$ 0.01"]

    print("NOTAS:")
    for i in range(len(notas)):
        quantidade = valor // notas[i]
        valor -= quantidade * notas[i] # valor - (quantidade * nota)
        print(f"{quantidade} nota(s) de {nomes_notas[i]}")
    
    print("MOEDAS:")
    for i in range(len(moedas)):
        quantidade_moedas = valor // moedas[i]
        valor -= quantidade_moedas * moedas[i]
        print(f"{quantidade_moedas} moeda(s) de {nomes_moedas[i]}")
