 
from flask import Flask ,request
import pickle
import pandas as pd
import numpy as np
app=Flask(__name__)

@app.route('/',methods=['POST'])


def perdict():
    clf = pickle.load(open('./model.pkl', 'rb'))
    data=request.get_json(force=True)
    data=pd.DataFrame(data)
    out=clf.predict(np.asarray(data['ct']).reshape(1, -1))
    result={'Trend':int(out[0])}
    return result 


if __name__== '__main__':
    app.run(port=5000,debug=False)
