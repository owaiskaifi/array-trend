 
 

from flask import Flask ,request,render_template 
from joblib import load
import numpy as np


app=Flask(__name__)
clf =   load( './model.pkl'  )
 
def get_status(y_pred_cycle ):    
   
    ct_status= ['NO_COUNT','INCREASE','DECREASE','STABLE','VARIANCE'] #  ['0','1','2','3','4']      
    
    ctt=ct_status[y_pred_cycle]
    
    return  ctt
  
@app.route('/')
def home():
    return render_template( 'index.html')
 
@app.route('/predict', methods=['POST'])
def predict():

    try:

    
        data=request.get_json(force=True)   
        val_arr_ct=  np.asarray(data['arr']) 

        nor=max(val_arr_ct)
        
        if nor!=0:
            val_arr_ct= val_arr_ct / nor*2 
            
            out=clf.predict( val_arr_ct.reshape( 1,-1))  
            
        else:
            out=np.array([0])

          
        out= get_status(int(out))
        result={'STATUS': out  }
        return result 
    except:
        result={"ERROR":'Wrong input format'}
        return     result

if __name__== '__main__':
    app.run(  )
