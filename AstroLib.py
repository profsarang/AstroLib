#Import sqlite3 for database connection and operation.
import sqlite3 as sq
 
# Import pandas module into this program as pd
import pandas as pd

def connectDatabase():
  # Create a Database connection object
  connection = sq.connect('./planets.db')
  return connection
def getPlanets(connection,date):
  # Create a cursor object.
  curs = connection.cursor()
  #Querying the Database.
  curs.execute("SELECT * FROM Planets WHERE Date=?", (date,))
  #Fetching Records from the databse.
  rows=curs.fetchall()
  #printing the Records.
  for row in rows:
    print("Sun: "+str(row[1]))
    print("Moon: "+str(row[2]))
    print("Mercury: "+str(row[3]))
    print("Venus "+str(row[4]))
    print("Mars "+str(row[5]))
    print("Jupiter "+str(row[6]))
    print("Saturn "+str(row[7]))
    print("Uranus "+str(row[8]))
    print("Neptune"+str(row[9]))
    print("Pluto "+str(row[10]))
    print("Mean Node "+str(row[11]))
    print("")
  # Close connection to SQLite database
  connection.close()
if __name__ == "__main__":
  db_connection=connectDatabase()
  date=input("Enter Date(IN YYYYMMDD Format):")  #Testing:Enter Date 20000102
  getPlanets(db_connection,date)
