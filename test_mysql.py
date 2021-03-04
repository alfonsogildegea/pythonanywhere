import mysql.connector
import datetime

import json 


# Configuración
with open(r'C:\TRABAJO\Python\Pythonanywhere\repo_pythonanywhere\pythonanywhere\config.json') as json_file: 
    config = json.load(json_file) 

#config = {
#  'user': 'alggea',
#  'password': 'sito28',
#  'host': '127.0.0.1',
#  'database': 'prueba_db',
#  'raise_on_warnings': True
#}

print(config)

cnx = mysql.connector.connect(**config)

print(cnx)


#query = ("SELECT id, nombre, email FROM tbl_prueba "
#         "WHERE hire_date BETWEEN %s AND %s")
#hire_start = datetime.date(1999, 1, 1)
#hire_end = datetime.date(1999, 12, 31)
#cursor.execute(query, (hire_start, hire_end))

cursor = cnx.cursor()

query = ("SELECT id, nombre, email FROM tbl_prueba")
cursor.execute(query)

for (id, nombre, email) in cursor:
  print(id, nombre, email)

cursor.close()


cnx.close()