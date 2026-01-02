from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def home(): 
	return "<center><h1>Hello, Flask! <H2>AUTOMATED</H2> CI CD Pipiline With Dymamic Change!! IP Changed!!</h1>"

@app.route("/about") 
def about(): 
	return "This is a simple Flask starter project! Testing!"
    
@app.route("/contact") 
def contact(): 
	return "<CENTER><h1>FLASK DEMO FOR AUTOMATED CI/CD</H1>"

@app.route("/testform", methods=["GET"])
def testform():
    if request.method=='GET':
        return render_template('myform.html')
	
@app.route("/addtest") 
def addtest(): 
	a = request.args.get("a")
	b = request.args.get("b")

	result = int(a) + int(b)

	return "<h1>" + str(result) + "</h1>"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False   # 🔴 VERY IMPORTANT
    )