# Public_Data_Science_Portfolio

## Future Hometown Finder Project:
Created a web application that recommends towns/cities to live in based on criteria such as housing price, weather, crime rate, population density, and if there is a local hospital.
Cleaned and merged data from five different sources in a Python Jupyter Notebook. 
Created with Streamlit app framework and deployed with Heroku. 
Interacted with Google Custom Search API to display images of homes in recommended towns.
Link to application: https://future-hometown-finder.herokuapp.com/. Note that I have limited Google Custom Search API calls, so if you use the app only run it a few times (less than 10).


## Predicting Future Company Violation Fees:
Used Scikit-Learn's stacking ensembler to create a model that predicts total company penalties (USD) for the next year. The goal of this project is to determine which companies are taking their violations seriously and which ones are not. This could be useful for consumers in understanding which companies they might want to support. This could also be useful for the government in understanding which companies are likely to commit further violations. The final RMSE on the test set was $210,003. This was my first time working with time series data and I learned a lot about creating a time series model. At first, I wanted to use some type of LSTM neural network but I quickly discovered that the data did not fit with what I originally had in mind. This entire project stemmed from the dataset and I thought it would be a good opportunity to learn something new. Looking back, I think that the data was probably not suited for a time series model and the overall goal is probably a foolish one. Eventhough the project did not turn out as I had hoped, I'm still happy that I did it because I now know more about what's required for a time series project to be successful.


## Metallic Asteroid Classification:
Used 10-fold cross-validation and Imblearn’s SMOTE oversampling to train and evaluate a classifier that attempts to identify asteroids with high metal content.
Compared several machine learning  models and achieved ~70% ROC AUC score and ~23% Precision-Recall AUC.


## Craigslist Used Automobile Regression:
Used Scikit-Learn to create a multiple linear regression and a random forest regression to predict the price of used vehicles.
Achieved an average accuracy of 78.28% relative to the actual listing prices and a mean absolute error of $1952.
