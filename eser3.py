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

def modifica_dati():
    """Modifica i dati di un utente."""
    print("cosa vuoi modificare?")
    print("1. Nome e cognome")
    print("2. Email")
    
    