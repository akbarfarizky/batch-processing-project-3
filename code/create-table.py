import psycopg2

# connect to postgres

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=123jomblo")
cur = conn.cursor()

# create table

try:
    cur.execute("""
                CREATE TABLE IF NOT EXISTS latihan_user(
                    id serial PRIMARY KEY,
                    email text,
                    name text,
                    phone text,
                    postcal_code text
                )
    """)
    print("Create Table Success")
except:
    print("Create Table Failed")

# menambahkan data
cur.execute("INSERT INTO latihan_user VALUES (%s, %s, %s, %s, %s)", (1, 'ahmadi@yuhu.id', 'ahmadi', '089089089', '40133'))
conn.commit()


