rom flask import Flask , render_template , request
import pickle
import numpy as np
model= pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict' , methods=['POST'])
def predict():
    Tv_price = int(request.form.get('TV_price'))
    Radio_price =int( request.form.get('Radio_price'))
    Social_Media = int(request.form.get('Social_Media'))
    Influencer = int(request.form.get('Influencer'))

    #prediction
    result= model.predict(np.array([Tv_price,Radio_price,Social_Media,Influencer]).reshape(1,4))
    return render_template('index.html',result=result)

if __name__ == '__main__':
    app.run(debug=True)
