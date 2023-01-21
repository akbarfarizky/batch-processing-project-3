import psycopg2

# connect to postgres
try:
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=123jomblo")
    print("Koneksi database berhasil")
except:
    print("Koneksi database gagal")

# menggunakan curso
cur = conn.cursor()
cur.execute("select * from public.siswa")

# menampilkan hasil
one = cur.fetchone()
all = cur.fetchall()
conn.commit()

# menampilkan secara list
for i in all:
    print(i)