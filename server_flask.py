import numpy as np 
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

filename = '/home/ajmalrasi/Documents/ML_Deployments_exp/sentimental-analysis-nlp/pipe_clf_checkpoint.joblib'
model = joblib.load(open(filename, 'rb'))
model_clf = model['pipeline_clf']

@app.route('/api', methods=['POST'])
def predict():
    
    data = request.get_json(force=True)
    predictoin =  model_clf.predict(data['x'])
    output_text = "Text;" + str(data["x"])
    output = "Class:" + str(predictoin)
    
    return jsonify(output_text, output)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
    