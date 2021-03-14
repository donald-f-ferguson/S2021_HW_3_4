import pymysql

conn = pymysql.connect(
    host="localhost",
    user="dbuser",
    password="dbuserdbuser",
    cursorclass=pymysql.cursors.DictCursor
)

cur = conn.cursor()
res = cur.execute("select * from lahmansbaseballdb.people limit 1")
res = cur.fetchall()

cols = res[0].keys()


print(cols)


def update_col_by_name(t, n):
    s = "update " + t + " set " + n + "=NULL where " + n + "=''"
    print(s)

for k in cols:
    update_col_by_name("people", k)

