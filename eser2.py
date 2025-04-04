#ESER 2

stringhe = []

lunghezza_precedente = 0

while True:
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