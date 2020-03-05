import mysql.connector
from mysql.connector import errorcode
import datetime
import json

class DateTimeEncoder(json.JSONEncoder):
  def default(self, o):
    if isinstance(o, datetime.datetime):
      return o.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(o, datetime.date):
      return o.strftime("%Y-%m-%d")
    if isinstance(o, datetime.timedelta):
      return str(o.seconds//3600).zfill(2)+':'+str(o.seconds%3600//60).zfill(2)
    return json.JSONEncoder.default(self, o)

def getConnection():
  error = ''
  cnx = ''
  try:
    cnx = mysql.connector.connect(host='localhost', user='root',passwd='',
                                  database='itcc_venu') #dev.itcc.net.au
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
    conn.commit()
    cur.close()
    conn.close()
  else:
    res = error
  return json.dumps(res, cls=DateTimeEncoder)

def runUpdate(query):
  (conn, error) = getConnection()
  if error == '':
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
    return "Success"
  else:
    res = error
  return json.dumps(res, cls=DateTimeEncoder)

def runInsert(query):
  (conn, error) = getConnection()
  res = ''
  if error == '':
    cur = conn.cursor()
    id = cur.lastrowid
    cur_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {'id':id,'last_updated':cur_date}
    print(cur_date)
    cur.execute(query,data)
    conn.commit()
    cur.close()
    conn.close()
  else:
    res = error
  return str(res)
