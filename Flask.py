from flask import Flask, render_template


# Create a flask instance

app = Flask(__name__)


# Create a route decorator

@app.route('/')

#def index():
 #   return "<h1>Hello world!<h1>"


## FILTERS!!
#safe
#capitalize
#lower
#upper
#title
#trim
#striptags




def index():
	global first_name 
	first_name = "Amin"
	stuff = 'This is bold Text'
	favPizza = ['Pepperroni', 'Cheese', 'Mushroom', 41]
	return render_template('index.html', first_name = first_name, stuff = stuff, fav_pizza = favPizza)

@app.route('/user/<name>')
# localhost:5000/user/john

def user(name):
	return render_template('user.html', user_name = first_name)

##Create custom Error pages:

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


#Internal Sercer Error

@app.errorhandler(500)
def page_not_found2(e):
	return render_template('500.html'), 500
