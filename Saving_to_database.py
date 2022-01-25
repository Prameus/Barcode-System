import psycopg2
import psycopg2.extras

fields = ['id', 'product', 'carat', 'barcode']

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
        products = []

        def __init__(self):
            #cursor.execute('DROP TABLE IF EXISTS products')

            create_script = """
                    CREATE TABLE IF NOT EXISTS products (
                        id          INT PRIMARY KEY,
                        product     TINYTEXT,
                        carat       int,
                        barcode     int
                    )
                    """
            cursor.execute(create_script)

        def adding_product(self, *kwargs):
            insert_new_product = 'INSERT INTO products (id,product,carat,barcode) VALUES (%s,%s,%s,%s) '
            cursor.execute(insert_new_product, kwargs)

        def read_all_products(self):

            cursor.execute('SELECT * FROM PRODUCTS')
            for record in cursor.fetchall():
                self.products.append(record)
            return self.products

        def clear_all(self):
            self.products.clear()

        def delete_product(self, selected):
            int_selected = int(selected)
            delete_product = (
                "DELETE FROM products WHERE id = %s")
            cursor.execute(delete_product, int_selected)
            # NEDEN SADECE 1 ITEM SILINIYOR??????

        def update_product(self, *kwargs):
            update_command = "UPDATE products SET (%s) = (%s) WHERE id = (%s);"
            cursor.execute(update_command, kwargs)
            # update syntax`inda hata yapiyorum ama nasil?

    database = Database()
    database.read_all_products()
    connect.commit()
except Exception as error:
    print(error)
