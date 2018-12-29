a-flask-api-for-serving-scikit-learn-models.rst

* 참고
https://towardsdatascience.com/a-flask-api-for-serving-scikit-learn-models-c8bcdaa41daa



> 원본
|from flask import Flask, jsonify
|from sklearn.externals import joblib
|import pandas as pd
|
|app = Flask(__name__)
|clf = joblib.load('model.pkl') # 이렇게 하면 메모리에 한번 올리고 여러 쓰레드가 같이 사용할수 있을 것 같다. 
|@app.route('/predict', methods=['POST'])
|def predict():
|     json_ = request.json
|     query_df = pd.DataFrame(json_)
|     query = pd.get_dummies(query_df)
|     prediction = clf.predict(query)
|     return jsonify({'prediction': list(prediction)})
|if __name__ == '__main__':
|     # clf = joblib.load('model.pkl')
|     app.run(port=8080)
  
     
  
