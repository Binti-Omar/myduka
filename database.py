import psycopg2

conn = psycopg2.connect(host = "localhost",port ="5432",user = "postgres",password="C0717824020",dbname="myduka_db")

cur = conn.cursor()

# displaying products
def display_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

products = display_products()
# print(products)

# displaying sales
def display_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

sales = display_sales()
# print(sales)

# inserting a product
def insert_product(product_values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values(product_values)")
    conn.commit()

product1= ('sugar',100,120)
product2= ('salt',50,70)
# insert_product(product1)
# insert_product(product2)

# inserting a sale
def insert_sale(sale_values):
    cur.execute("insert into sales(pid,quantity)values(sale_values)")
    conn.commit()

sale1 = (1,2)
sale2 = (2,3)
# insert_sale(sale1)
# insert_sale(sale2)