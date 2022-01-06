import psycopg2
import psycopg2.extras


hostname = "localhost"
database = "lira_gold"
username = "postgres"
pwd = "transformers6"
port_id = 5432

connect = None
cursor = None
try:
    connect = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )

    cursor = connect.cursor(cursor_factory=psycopg2.extras.DictCursor)

    class Database:
        def __init__(self):
            cursor.execute('DROP TABLE IF EXISTS products')

            create_script = """
                    CREATE TABLE IF NOT EXISTS products (
                        id  INT PRIMARY KEY,
                        product    varchar(100),
                        carat   int,
                        item    int
                    )
                    """
            cursor.execute(create_script)
            connect.commit()

        def adding_product(self):
            value = input()

        def delete_product(self):
            value = input('Silmek istediginiz urunun isimini giriniz: ')
            delete_product = "DELETE FROM products WHERE = %s"

            cursor.execute(delete_product, value)
            connect.commit()

    database = Database()
    database.delete_product()

except Exception as error:
    print(error)

finally:
    if connect is not None:
        connect.close()
    if cursor is not None:
        cursor.close()
