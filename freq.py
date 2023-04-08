import MySQLdb
import os

import datetime

def connect():
    return MySQLdb.connect(
      host=os.environ["HOST"],
      user=os.environ["USER"],
      passwd=os.environ["PASSWD"],
      db=os.environ["DB"],
      ssl_mode = "VERIFY_IDENTITY",
      ssl = {
        "ca": os.environ["CAPATH"]
      }
    )

connection=connect()
cursor=connection.cursor()
sql="SELECT COUNT(*) FROM freqdata"
cursor.execute(sql)
id=cursor.fetchone()[0]+1

sql="INSERT INTO usddata VALUES(%s, %s)"

time=datetime.datetime.now().strftime('%m%d%H%M')
cursor.execute(sql, (id, time))

connection.commit()
