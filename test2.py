import pymysql

HOST = "pemotec.be"
PORT = 3306
USER = "most_pemotec"
PASSWORD = "z9H5%R^pjPxM&ePA"
DB = "pemotec_test"

try:
    connection = pymysql.Connect(host=HOST, port=PORT,
                               user=USER, passwd=PASSWORD, db=DB)

    dbhandler = connection.cursor()
    dbhandler.execute("SELECT * from most")
    result = dbhandler.fetchall()
    for item in result:
        print(item)

except Exception as e:
    print(e)

finally:
	connection.close()