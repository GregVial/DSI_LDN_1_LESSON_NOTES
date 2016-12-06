import flask

app = flask.Flask(__name__)

## Model
import  numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("titanic_app/data/titanic.csv")
include = ['Pclass','Sex','Age','Fare','SibSp','Survived']

df['Sex'] = df['Sex'].apply(lambda x: 0 if x == 'male' else 1)
df = df[include].dropna()

X = df[include[:-1]]
y = df[include[-1]]

PREDICTOR = RandomForestClassifier().fit(X,y)

## Routes
@app.route('/page')
def page():
	with open("page.html",'r') as viz_file:
		return viz_file.read()

@app.route('/result',methods=["GET","POST"])
def result():
	if flask.request.method == "POST":
		inputs = flask.request.form
        	pclass = inputs['pclass'][0]
        	sex = inputs['sex'][0]
        	age = inputs['age'][0]
        	fare = inputs['fare'][0]
        	sibsp = inputs['sibsp'][0]


	        item = [pclass,sex,age,fare,sibsp]
      		score = PREDICTOR.predict_proba(item)
        	results = {'survival chances': score[0,1], 'death chances': score[0,0]}
        	return flask.jsonify(results)


@app.route('/predict',methods=["GET"])
def predict():
	pclass = flask.request.args['pclass']
        sex = flask.request.args['sex']
        age = flask.request.args['age']
        fare = flask.request.args['fare']
        sibsp = flask.request.args['sibsp']

	item = [pclass,sex,age,fare,sibsp]
	score = PREDICTOR.predict_proba(item)
	results = {'survival chances': score[0,1], 'death chances': score[0,0]}
	return flask.jsonify(results)



if __name__ == '__main__':
	HOST = "127.0.0.1"
	PORT = 4000
	app.run(HOST,PORT,debug=True)

