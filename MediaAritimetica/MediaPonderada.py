# Media Ponderada, soma(dados * peso) / soma(peso)
peso = [1, 2, 3, 4]
notas = [8, 7, 9, 9]

notaXpeso = [notas[i] * peso[i] for i in range(0, len((notas)))]
media_pond = sum(notaXpeso) / sum(peso)
print(media_pond)