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
        def __init__(self):
            #cursor.execute('DROP TABLE IF EXISTS products')

            create_script = """
                    CREATE TABLE IF NOT EXISTS products (
                        id          INT PRIMARY KEY,
                        product     varchar(100),
                        carat       int,
                        barcode     int
                    )
                    """
            cursor.execute(create_script)

        def adding_product(self):
            values_scripts = []
            for i in fields:
                value = str(input(f'Eklemek istediginiz urunun {i} yaziniz: '))
                values_scripts.append(value)
            insert_new_product = 'INSERT INTO products (id,product,carat,barcode) VALUES (%s,%s,%s,%s) '
            print(values_scripts)
            cursor.execute(insert_new_product, values_scripts)

        def read_all_products(self):
            products = []
            cursor.execute('SELECT * FROM PRODUCTS')
            for i in cursor.fetchall():
               products.append(i)
            print(products)
            return products
            
        def delete_product(self):
            value = input('Silmek istediginiz urunun isimini giriniz: ',)
            modified_value = str(f'{value}',)
            delete_product = "DELETE FROM products WHERE id = %s"
            print(modified_value)
            cursor.execute(delete_product, modified_value)

    database = Database()
    database.read_all_products()

    connect.commit()
except Exception as error:
    print(error)
