import mysql.connector
from mysql.connector import errorcode

def getConnection():
  error = ''
  cnx = ''
  try:
    cnx = mysql.connector.connect(host='dev.itcc.net.au', user='itccnet_venuuser',passwd='o&rWD#2].vhw',
                                  database='itccnet_venu')
  except mysql.connector.Error as err:
    error = err
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password",err)
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  return (cnx, error)

def runQuery(query):
  (conn, error) = getConnection()
  if error == '':
    cur = conn.cursor()
    cur.execute(query)
    res = cur.fetchall()
    cur.close()
    conn.close()
  else:
    res = error
  return str(res)