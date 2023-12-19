import json
import pickle
import numpy as np
import pandas as pd



transformer = pickle.load(open("models/transformer.pkl","rb"))
pipes = pickle.load(open("models/pipes.pkl","rb"))

with open('feature_names.json', 'r') as file:
    column_names_json = file.read()

# Convert JSON to list (column names)
column_names = json.loads(column_names_json)


def get_prediction(model,input):

    try:
        for m in pipes:
            if m['Model'] == model:
                pipe = m['Pipe']

                input_data =(np.array([input],dtype=object)).reshape((1,-1))
                datafr = pd.DataFrame(input_data,columns=column_names)
                data = transformer.transform(datafr)
                pred = int(pipe.predict(data)[0])
                
                return pred
    
    except Exception as e:
        print(e) 
        
        