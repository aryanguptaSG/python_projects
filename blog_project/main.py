from flask import Flask , render_template,request
import json
import subprocess
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

with open('config.json','r') as c:
	params = json.load(c)["params"]


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/blog_project'
db = SQLAlchemy(app)

class contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email= db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(120), nullable=False)





@app.route('/')
def home():
    return render_template('index.html', params=params)

@app.route('/executepy')
def executepy():
	out = subprocess.run(["python3","1.py"],capture_output=True)
	print(str(out.stdout.decode()))
	return str(out.stdout.decode())


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/contact' ,methods=['GET',"POST"])
def contact():
	if(request.method=="POST"):
		name=request.form.get('name')
		email=request.form.get('email')
		phone=request.form.get('phone')
		message=request.form.get('message')
		entry = contact(name=name,email=email,phone=phone,message=message)
		db.session.add(entry)
		db.session.commit()
	return render_template('contact.html')



app.run()




