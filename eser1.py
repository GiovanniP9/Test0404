#ESER 1
print("dammi numero ripetizioni ciclo")
X = int(input())
i = 0

interi = []
decimali = []
stringhe = []
    
for _ in range(X):# ciclo for che si ripete X volte
    #input dell'utente
    dato = input("inserisci un numero intero, decimale o stringa: ")
    if dato.isdigit():#controlla se è un intero
        interi.append(int(dato))
    elif dato.replace('.', '', 1).isdigit(): #controlla se è un decimale
        decimali.append(float(dato))
    else: # se non è ne intero ne decimale è una stringa
        stringhe.append(dato)
    
scelta = input("Vuoi stampare una lista specifica o tutte? (interi, decimali, stringhe, tutte): ").lower()
    
if scelta == "interi":
        print("Lista degli interi:", interi)
elif scelta == "decimali":
        print("Lista dei decimali:", decimali)
elif scelta == "stringhe":
        print("Lista degli altri:", stringhe)
elif scelta == "tutte":
        print("Lista degli interi:", interi)
        print("Lista dei decimali:", decimali)
        print("Lista degli altri:", stringhe)
else:
        print("Scelta non valida.")