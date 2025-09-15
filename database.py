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
    cur.execute(f"insert into products(name,buying_price,selling_price)values{product_values}")
    conn.commit()

product1= ('sugar',100,120)
product2= ('salt',50,70)
# insert_product(product1)
# insert_product(product2)

# inserting a sale
def insert_sale(sale_values):
    cur.execute(f"insert into sales(pid,quantity)values{sale_values}")
    conn.commit()

sale1 = (1,2)
sale2 = (2,3)
# insert_sale(sale1)
# insert_sale(sale2)

# display  stocks
def display_stock():
    cur.execute('select* from stock')
    stock=cur.fetchall()
    return stock

stock=display_stock()
# print(stock)

# inserting stock
def insert_stock(stock_values):
    cur.execute(f'insert into stock(pid,stock_quantity)values{stock_values}')
    conn.commit()

stock1=(5,200)
stock2=(16,10)
# insert_stock(stock1)
# insert_stock(stock2)

def available_stock(pid):
    cur.execute(f"select sum(stock_quantity) from stock where pid ={pid}")
    total_stock= cur.fetchone()[0] or 0

    cur.execute(f"select sum(quantity) from sales where pid ={pid}")
    total_sales = cur.fetchone()[0] or 0

    return total_stock - total_sales

