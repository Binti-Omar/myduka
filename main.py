from flask import Flask ,render_template,request,redirect,url_for
from database import display_products,display_sales,insert_product

# creating a Flask instance
app = Flask(__name__)


# decorator function -it determines the behavior of the view function
# @app.route('/') -is a connecter used to connect the url to the view function
@app.route('/')
# view function -it executes the return statement and it should have a unique name
def home():
    return render_template("index.html")

@app.route("/products")
def products():
    products = display_products()
    return render_template("products.html",products=products)

@app.route("/add_products",methods=['GET','POST'])
def add_products():
    product_name=request.form["product_name"]
    buying_price=request.form["buying_price"]
    selling_price=request.form["selling_price"]
    new_product=(product_name,buying_price,selling_price)
    insert_product(new_product)
    return redirect(url_for('products'))
    # return redirect(url_for('products'))the url is used to display all products with the new products and the products in the url is the product at the def function


@app.route("/sales")
def sales():
    sales = display_sales()
    return render_template("sales.html",sales=sales)

@app.route("/stock")
def stock():
    return render_template("stock.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")





app.run(debug=True)