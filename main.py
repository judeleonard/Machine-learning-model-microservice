from fastapi import FastAPI, HTTPException
import uvicorn
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from schema import CustomerModel

app = FastAPI()

# Defining root endpoint
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this Bank Model Micro-service App!"}

# defining prediction endpoint
@app.post('/predict')
async def predict_customer(model_data: CustomerModel):
    clean_data = model_data.dict()
    data_input = [[clean_data['age'], clean_data['job'], clean_data['marital'], clean_data['education'], clean_data['default'],
                    clean_data['balance'], clean_data['housing'], clean_data['loan'], clean_data['day'], clean_data['duration'],
                    clean_data['campaign'], clean_data['pdays'], clean_data['previous'], clean_data['poutcome']]]
    dataframe = pd.DataFrame(data_input, index=[0])
    print('=======================')
    print(dataframe.shape)
    print("===================")
    # select column indexes for transforming and encoding the categorical variables received through data input
    cols = [1,2,3,4,6,7,13]
    dataframe[cols] = dataframe[cols].apply(LabelEncoder().fit_transform)
    dataframe.to_dict('records')
    loaded_model = pickle.load(open('./model/model3.pkl', 'rb'))
    #encoded_data_dict = dataframe.dict()
    prediction = loaded_model.predict(dataframe).tolist()
    probability = loaded_model.predict_proba(dataframe).max().tolist()
    prediction_label = ['Yes' if prediction== 1 else 'No' for value in prediction]
    if not prediction:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object =  {
        'prediction': prediction_label,
        'probability': probability
    }
    return response_object
# https://ml-model-ms.herokuapp.com/    

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8082)