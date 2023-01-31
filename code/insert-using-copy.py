import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=123jomblo")
cur = conn.cursor()

with open('D:/batch-processing-project-3/source/users_w_postal_code.csv','r') as f:
    next(f)
    cur.copy_from(f,'latihan_user',sep=',',columns=('email','name','phone','postcal_code'))

conn.commit()