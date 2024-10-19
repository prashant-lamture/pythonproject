import psycopg2
import Caller
import first

def __init__(self):
        # create connection with db
        self.connection = psycopg2.connect(
            dbname='pythonDB',
            user='postgres',
            password='12345',
            host='localhost',
            port=5432
        )
        self.cursor = self.connection.cursor()

def update(connection):
    cursor = connection.cursor()
    query = """
    UPDATE student SET address WHERE address'pune';
    """
    try:
        cursor.execute(query, ("Pune"))
        cursor.execute("SELECT * FROM student WHERE address=pune")
        records = cursor.fetchone()
        connection.commit()
    except Exception as err:
        print(err)
    cursor.close()
    connection.close()
