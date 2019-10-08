from flask import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'danni'

vorur = [[0,"Peysa",2500],[1,"Buxur",4500],[2,"Sokkar",1500]]

@app.route('/')
def index():
	return render_template("index.tpl", v=vorur) 

@app.route('/kaupa/<int:nr>')
def kaupa(nr):
	temp_karfa = []
	# er karfa tóm, ef satt þá ekki tóm?
	if 'karfa' in session:
		temp_karfa = session['karfa']
		temp_karfa.append(nr)
		session['karfa'] = temp_karfa
		return redirect("/karfa")
	else:
		temp_karfa.append(nr)
		session['karfa'] = temp_karfa
		return redirect("/karfa")

@app.route('/karfa')
def karfa():
	temp_karfa = []
	teljari = 0
	heildarverd = 0
	if 'karfa' in session:
		temp_karfa = session['karfa']
		for i in temp_karfa:
			heildarverd += vorur[i][2]
		return render_template('karfa.tpl',valdarvorur=temp_karfa, vorur=vorur, nr=teljari, hv=heildarverd)
	else:
		return render_template("karfa.tpl")

@app.route('/popKarfa')
def popkarfa():
    session.pop("karfa", None)
    return redirect("/")

@app.route("/info", methods=['GET','POST'])
def info():
	temp_karfa = []
	teljari = 0
	heildarverd = 0
	if 'karfa' in session:
		temp_karfa = session['karfa']
		for i in temp_karfa:
			heildarverd += vorur[i][2]

	if request.method == 'POST':
		nafn = request.form['name']
		netfang = request.form['email']
		simi = request.form['phone']
		print(nafn)
		print(netfang)
		print(simi)
		return render_template("Takk.tpl",n=nafn)
	else:
		session.pop("karfa", None)
		return render_template("info.tpl",valdarvorur=temp_karfa, vorur=vorur, hv=heildarverd)

if __name__ == "__main__":
	app.run(debug=True)