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

#crea_database()
#crea_tabella()
inserimento()