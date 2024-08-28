'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''

hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

minuto_duracao = minuto_final - minuto_inicial
if minuto_duracao < 0:
    minuto_duracao += 60
    hora_final -= 1

hora_duracao = hora_final - hora_inicial
if hora_duracao < 0:
    hora_duracao += 24

if hora_duracao == 0 and minuto_duracao == 0:
    hora_duracao = 24

print(f"O JOGO DUROU {hora_duracao} HORA(S) E {minuto_duracao} MINUTO(S)")