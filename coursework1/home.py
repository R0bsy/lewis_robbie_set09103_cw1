from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('home.html')

@app.route('/champions')
def champion_page():
	return render_template('champions.html')

@app.route('/champions/cassiopeia')
def cassiopeia_page():
	return render_template('cassiopeia.html')

@app.route('/champions/syndra')
def syndra_page():
	return render_template('syndra.html')

@app.route('/champions/zed')
def zed_page():
	return render_template('zed.html')
	
@app.route('/tournaments')
def tournaments_page():
	return render_template('tournaments.html')	

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
