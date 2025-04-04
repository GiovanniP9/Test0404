#ESER 2

stringhe = [] # lista per memorizzare le stringhe

lunghezza_precedente = 0 # lunghezza della stringa precedente

while True:# ciclo infinito per l'inserimento delle stringhe
    #input dell'utente
    dato = input("inserisci una stringa (o 'fine' per terminare): ")
    if dato.lower() == "fine":
        break
    elif len(dato) > lunghezza_precedente:
        lunghezza_precedente = len(dato)
        stringhe.append(dato)
    else:
        print("La stringa deve essere più lunga della precedente.")

print("Lista delle stringhe:", ", ".join(stringhe))
print("Lunghezza della stringa più lunga:", lunghezza_precedente)
print("Numero di stringhe inserite:", len(stringhe))