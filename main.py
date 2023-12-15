import mysql.connector


def crea_database():
    #configurazione per la connessione al database
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password=""
    )

    #cursore che ci permette di eseguire i comandi su mysql
    mycursor = mydb.cursor()

    #sintassi per creare il database
    mycursor.execute("CREATE DATABASE animali")


def crea_tabella():
    #configurazione per la connessione al database
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="animali"
    )

    #cursore che ci permette di eseguire i comandi su mysql
    mycursor = mydb.cursor()

    #sintassi per creare la tabella
    mycursor.execute("CREATE TABLE mammiferi (id CHAR(4), nome VARCHAR(25), razza VARCHAR(25), peso int, eta int)")


def inserimento():
    #configurazione per la connessione al database
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="animali"
    )
    #cursore che ci permette di eseguire i comandi su mysql
    mycursor = mydb.cursor()

    #sintassi per inserire una tupla
    sql = "INSERT INTO mammiferi (id, nome, razza, peso, eta) VALUES (%s, %s, %s, %s, %s)"
    
    val = [
      ('1234', 'Giuseppe', 'Ratto', 2, 5),
      ('4567', 'Fabio', 'Anatra', 4, 7),
      ('7890', 'Furia', 'Cavallo', 500, 12),
      ('4321', 'Baffo', 'Gatto', 3, 8),
      ('7654', 'Sandy', 'Cane', 9, 2)
    ]

    #esegue il comando
    mycursor.executemany(sql, val)

    #applica le modifiche apportate al database, le salva
    mydb.commit()

    #restituisce il numero di righe modificate
    print(mycursor.rowcount, "record inserted.")


def stampa():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="animali"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM mammiferi")

    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)


def aggiungi_5_animali():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="animali"
    )
    
    mycursor = mydb.cursor()

    for i in range(5):
      id=input("inserisci id: ")
      nome=input("inserisci nome: ")
      razza=input("inserisci razza: ")
      peso=input("inserisci peso: ")
      eta=input("inserisci età: ")

      sql = "INSERT INTO mammiferi (id, nome, razza, peso, eta) VALUES (%s, %s, %s, %s, %s)"
    
      val = (id, nome, razza, peso, eta)

      mycursor.execute(sql, val)

      mydb.commit()

      print(mycursor.rowcount, "record inserted.")  


def peso_maggiore_2_kg():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="animali"
    )

    mycursor = mydb.cursor()

    mycursor.execute("""SELECT nome 
                        FROM mammiferi
                        WHERE peso > 2""")

    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)


def aggiungi_animali():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="animali"
    )
    
    mycursor = mydb.cursor()

    scelta=0

    while scelta==0:
      id=input("inserisci id: ")
      nome=input("inserisci nome: ")
      razza=input("inserisci razza: ")
      peso=input("inserisci peso: ")
      eta=input("inserisci età: ")

      sql = "INSERT INTO mammiferi (id, nome, razza, peso, eta) VALUES (%s, %s, %s, %s, %s)"
    
      val = (id, nome, razza, peso, eta)

      mycursor.execute(sql, val)

      mydb.commit()

      print(mycursor.rowcount, "record inserted.")  

      scelta=int(input("vuoi continuare ad inserire? si=0, no=1: "))


def menu():
    scelta = 0
    while scelta != 8:
        print("\nMenu:")
        print("1. Crea database")
        print("2. Crea tabella")
        print("3. Inserisci animali predefiniti")
        print("4. Aggiungi animali")
        print("5. Visualizza tutti gli animali")
        print("6. Visualizza animali con peso maggiore di 2kg")
        print("7. Inserisci 5 animali")
        print("8. Esci")

        scelta = int(input("Seleziona un'opzione: "))

        if scelta == 1:
            crea_database()
        elif scelta == 2:
            crea_tabella()
        elif scelta == 3:
            inserimento()
        elif scelta == 4:
            aggiungi_animali()
        elif scelta == 5:
            stampa()
        elif scelta == 6:
            peso_maggiore_2_kg()
        elif scelta == 7:
            aggiungi_5_animali()
        elif scelta == 8:
            print("Arrivederci!")
        else:
            print("Opzione non valida. Seleziona un numero da 1 a 8.")

# Esegui il menu
menu()
