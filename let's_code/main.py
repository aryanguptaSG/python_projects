from flask import Flask , render_template,request
import subprocess


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit',methods=['GET','POST'])
def submit():
	if request.method=='POST':
		code = str(request.form.get('code'))
		fh = open("test.py",'w')
		fh.write(code)
		fh.close()
		# with open("ans.txt",'r') as f:
		# 	text = f.read()
		out = subprocess.run(["python3","test.py"],capture_output=True,text=True)
		print(out.stdout)
		# # print(text)
		return render_template('result.html',result=out.stdout.split("\n"))




app.run()