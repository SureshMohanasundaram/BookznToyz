from application import app
from flask import render_template,request

productsData = [{
	"Product ID": "1111",
	"Product Name": "PHP 111",
	"Description": "Intro to PHP",
	"Price": "3",
	"Age Group": "3-5"
}, {
	"Product ID": "2222",
	"Product Name": "Java 1",
	"Description": "Intro to Java Programming",
	"Price": "4",
	"Age Group": "5-7"
}, {
	"Product ID": "3333",
	"Product Name": "Adv PHP 201",
	"Description": "Advanced PHP Programming",
	"Price": "3",
	"Age Group": "6-8"
}, {
	"Product ID": "4444",
	"Product Name": "Angular 1",
	"Description": "Intro to Angular",
	"Price": "3",
	"Age Group": "7-10"
}, {
	"Product ID": "5555",
	"Product Name": "Java 2",
	"Description": "Advanced Java Programming",
	"Price": "4",
	"Age Group": "9-12"
}]

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)

@app.route("/products")
def products():
    # print(productsData);
    return render_template("products.html", productsData=productsData, products=True)


@app.route("/register")
def register():
    return render_template("register.html", register=True)

@app.route("/requested",methods=["GET","POST"])
def requested():
    id=request.form.get('Product ID')
    name = request.form.get('Product Name')
    price = request.form.get('Price')
    return render_template("requested.html", requested=True, data={"id":id,"name":name,"price":price})