import mysql.connector
import contextlib
from typing import Tuple, Dict


@contextlib.contextmanager
def _connect_to_db():
  cnx = mysql.connector.connect(
    user='root',
    password='pw',
    host='demo-db',
    database='local_db')
  yield cnx
  cnx.close()


def insert_data(insert_query:str, data:Dict):
  with _connect_to_db() as conn:
    cursor = conn.cursor()
    cursor.execute(insert_query, data)
    rowid = cursor.lastrowid
    conn.commit() # completes the transaction
    cursor.close()
    
    
def get_data(query:str, data:Tuple):
  with _connect_to_db() as conn:
    cursor = conn.cursor()
    cursor.execute(query, data)
    rowid = cursor.lastrowid
    results = []
    for (row) in cursor:
      print(row)
      results.append(row)
    cursor.close()
    return results
    

