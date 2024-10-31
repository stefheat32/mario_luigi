from flask import Flask, render_template, request, redirect, flash, session, url_for
from dotenv import load_dotenv
from datetime import timedelta
from services.json_ops import read_from_json, save_order
from services.accont_handling import validate_and_login_user, validate_and_register_user
import os

load_dotenv()
app = Flask(__name__)

app.secret_key = os.getenv('FLASK_SECRET_KEY')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

@app.before_request
def make_session_permanent():
   session.permanent = True

#routing the 'index' page
@app.route('/', methods=['GET'])
def get_home():
	return render_template("homepage.html")

@app.route('/login', methods = ["GET"])
def get_login():
	return render_template("login.html")

@app.route('/login', methods = ["POST"])
def post_login():
	email = request.form["email"]
	password = request.form["password"]

	willRedirect, flashMessage, flashMessageType, redirectURL, account = validate_and_login_user(email, password)

	flash(flashMessage, flashMessageType)
	if willRedirect:
		session['email'] = email
		session['username'] = account['name']
		return redirect(redirectURL)
	else:
		return redirect(redirectURL)

@app.route('/logout', methods=['GET'])
def get_logout():
	session.clear()
	return redirect(url_for('get_home'))

#routing the 'register' page
@app.route('/register', methods=['GET'])
def get_register():
	return render_template('register.html')

@app.route('/register', methods=['POST'])
def post_register():
	email = request.form["email"]
	firstName = request.form["name"]
	lastName = request.form["lastName"]
	password = request.form["password"]
	phone = request.form["phone"]

	willRedirect, flashMessage, flashMessageType = validate_and_register_user(email, firstName, lastName, password, phone)

	flash(flashMessage, flashMessageType)
	if willRedirect:        
		return redirect('/login')
	else:
		return redirect('/register')

@app.route("/owner_page", methods=['GET'])
def get_owner_page():
	return "Owner page"

#routing the 'about us' page
@app.route('/about_us', methods=['GET'])
def get_about_us():
	return render_template("about_us.html")

#routing the 'menu' page
@app.route('/menu', methods=['GET'])
def get_menu():
	menuItems = read_from_json("Python/data/menu.json")
	return render_template("menu.html", menuItems=menuItems["menu"])

#routing the 'order' page
@app.route('/order', methods=['GET'])
def get_order():
	return render_template("order.html")

@app.route('/order', methods=['POST'])
def post_order():
	try:
		orderedPizzas = request.get_json()
		if not orderedPizzas:
			print("Empty order recieved")

		order_id = save_order(orderedPizzas)
		if order_id is None:
			print("Failed to save order")
	
	except Exception as e:
		print(f"An error occured: {e}")

	return redirect("/complete_order")

#routing the 'complete order' page
@app.route('/complete_order', methods=['GET'])
def get_complete_order():
	return "Order completed"

#routing the 'shopping cart' page
@app.route('/shopping_cart', methods=['GET'])
def get_shopping_cart():
	return render_template("shopping_cart.html")

# VISUALIZING QUEUE
@app.route('/queue', methods=['GET'])
def get_queue():
	queue = read_from_json("Python/data/orders.json")
	return render_template("queue.html")

@app.route('/api/queue', methods=['GET'])
def get_queue_api():
   queue = read_from_json("Python/data/orders.json")
   return {"queue": queue}

if __name__ == '__main__':
	app.run(debug=True, port=5001)