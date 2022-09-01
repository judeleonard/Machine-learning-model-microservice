# Machine-learning-model-microservice
Machine l earning model deployed as a microservice through FastAPI and Docker. Access the prediction endpoint anywhere by sending a request over https protocol.  

## Background of the Model
The data used for developing this model was downloaded from UCI machine learning repository website.The dataset contains bank customer's information
and the goal is to use this data to train a machine learning model that will help them to profile potential clients who are most likely to open a term deposite with the bank, in this way they can channel their marketing resources towards these customers to hasten this process. However, I was not entirely focused on developing a robust model but rather testing out this API, although the performance is not so bad for a less trained model with 88% accuracy. You can find the notebook I used for the training [here](https://colab.research.google.com/drive/1wEksu_DEc6o1HYjh76eJthicxXcG9tWC#scrollTo=M8V-0-ksPHmL)

## How the API works
The API predict endpoint recieves a json object that contains a customer's information then outputs a prediction label either Yes or No. Where yes means the customer is most likely to open a term deposit with the bank and No for the opposite, alongside the probability for each of this prediction.
