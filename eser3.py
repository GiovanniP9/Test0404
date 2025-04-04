#ESER 3

utenti = {} # dizionario per memorizzare gli utenti

def salva_utente():
    """Salva un utente nel dizionario."""
    username = input("Inserisci il nome utente: ")
    if username in utenti:
        print("Nome utente già esistente. Riprova.")
        return
    
    password = input("Inserisci la password: ")
    nome_cognome = input("Inserisci il tuo nome e cognome: ")
    email = input("Inserisci la tua email: ")
    
    # Salva i dati dell'utente nel dizionario
    utenti[username] = {
        "password": password,
        "nome_cognome": nome_cognome,
        "email": email }
    print("Utente salvato con successo!")
    
def login():
    """Effettua il login di un utente."""
    username = input("Inserisci il nome utente: ")
    password = input("Inserisci la password: ")
    
    # Controlla se l'utente esiste e se la password è corretta
    if username in utenti and utenti[username]["password"] == password:
        print(f"Benvenuto {utenti[username]['nome_cognome']}!")
    else:
        print("Nome utente o password errati.")
        return None

# modifica i dati dell'utente
# permette di modificare nome e cognome o email
def modifica_dati(username):
    print("cosa vuoi modificare?")
    print("1. Nome e cognome")
    print("2. Email")
    
    scelta = input("Inserisci la tua scelta (1 o 2): ")
    
    if scelta == "1":
        nuovo_nome_cognome = input("Inserisci il nuovo nome e cognome: ")
        utenti[username]["nome_cognome"] = nuovo_nome_cognome
        print("Nome e cognome modificati con successo!")
    elif scelta == "2":
        nuova_email = input("Inserisci la nuova email: ")
        utenti[username]["email"] = nuova_email
        print("Email modificata con successo!")
    else:
        print("Scelta non valida.")
        return None

## Menu principale
# permette di salvare un utente, effettuare il login e modificare i dati
def menu():
    while True:
        print("Menu:")
        print("1. Salva utente")
        print("2. Login")
        print("3. Modifica dati")
        print("4. Esci")
        
        scelta = input("Inserisci la tua scelta (1-4): ")
        
        if scelta == "1":
            salva_utente()
        elif scelta == "2":
            username = login()
            if username:
                print(f"Accesso effettuato con successo! Benvenuto {utenti[username]['nome_cognome']}")
        elif scelta == "3":
            username = input("Inserisci il nome utente: ")
            if username in utenti:
                modifica_dati(username)
            else:
                print("Utente non trovato.")
        elif scelta == "4":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida.")

menu()