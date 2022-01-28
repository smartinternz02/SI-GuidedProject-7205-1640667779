import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import inputScript

app = Flask(__name__)
model = pickle.load(open('Phising_website.pkl','rb'))

@app.route('/')
def abcd():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return render_template('final.html')

ans = ""   #@akshit
bns = ""   #@ojas
@app.route('/y_predict', methods=['POST'])
def y_predict():
    url = request.form['URL']
    checkprediction = inputScript.main(url)
    prediction = model.predict(checkprediction)
    print(prediction)
    output=prediction[0]
    if(output==1):
        pred="You are safe!!  This is a legitimate Website."
        return render_template('final.html',bns=pred)
    
    else:
        pred="You are on the wrong site. Be cautious!"        
        return render_template('final.html',ans=pred)


@app.route('/predict_api', methods=['POST'])
def predict_api():
    
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output=prediction[0]
    return jsonify(output)        
 
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
    