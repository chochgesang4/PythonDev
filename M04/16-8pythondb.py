import sqlite3
import sqlalchemy

con = sqlite3.connect("books.db")
cursor = con.cursor()
#start database initialization
try:
    #try block will prevent duplicate entries if the database has already been made and inserted into
    cursor.execute("CREATE TABLE Book (title,author,year)")
    cursor.execute("INSERT INTO Book VALUES(\"The Weirdstone of Brisingamen\",\"Alan Garner\",1960)")
    cursor.execute("INSERT INTO Book VALUES(\"Perdido Street Station\",\"China Miéville\",2000)")
    cursor.execute("INSERT INTO Book VALUES(\"Thud!\",\"Terry Pratchett\",2005)")
    cursor.execute("INSERT INTO Book VALUES(\"The Spellman Files\",\"Lisa Lutz\",2007)")
    cursor.execute("INSERT INTO Book VALUES(\"Small Gods\",\"Terry Pratchett\",1992)")   
    con.commit()
except Exception as exception:
    print(str(exception))




#stop database initialization
engine = sqlalchemy.create_engine("sqlite+pysqlite:///books.db")
with engine.connect() as conn:
    result = conn.execute(sqlalchemy.text("SELECT * FROM Book ORDER BY title ASC"))
    for row in result:
        print(f"title: {row.title}")
