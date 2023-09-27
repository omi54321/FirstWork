# Step 1 - Import the required libraries
from flask import Flask,render_template


# Step 2 - Create an object of Flask class
app = Flask(__name__)

l=['Meher','Omkar']

# Step 4 - Define all the required route
@app.route('/')
def home():
    return render_template('home.html',l=l)

# Step 3 - Run the application
if __name__ == "__main__":
    app.run(debug=True)