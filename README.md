# Public_Portfolio

* Note: Sometimes Github won't render Juypter Notebooks for whatever reason. You may need to refresh a few times to see contents of any Juypter Notebooks.

## Future Hometown Finder Project:
With remote work more prevalent than ever, I decided to create a project to recommend places to live based on user specifications. The project is also for my parents because they wish to move somewhere with a lower cost of living when they retire. The project uses least-squares error to determine which towns/cities have the closest values to the desired user input. If you're looking to move somewhere new, I hope that this project is able to help you! Note that this project is only focused on the United States. 

* Created a web application that recommends towns/cities to live in based on criteria such as housing price, weather, crime rate, population density, and if there is a local hospital.
* Cleaned and merged data from five different sources in a Python Jupyter Notebook. 
* Created with Streamlit app framework and deployed with Heroku. 
* Interacted with Google Custom Search API to display images of homes in recommended towns.
* Link to application: https://future-hometown-finder.herokuapp.com/. Note that I have limited Google Custom Search API calls, so if you use the app only run it a few times (less than 10).


## Predicting Future Company Violation Fees:
The goal of this project is to determine which companies are taking their violations seriously and which ones are not. This could be useful for consumers in understanding which companies they might want to support. This could also be useful for the government in understanding which companies are likely to commit further violations. This was my first time working with time series data and I learned a lot about creating a time series model. At first, I wanted to use some type of LSTM neural network but I quickly discovered that the data did not fit with what I originally had in mind. This entire project stemmed from the dataset and I thought it would be a good opportunity to learn something new. Looking back, I think that the data was probably not suited for a time series model and the overall goal is probably a foolish one. Eventhough the project did not turn out as I had hoped, I'm still happy that I did it because I now know more about what's required for a time series project to be successful.

* Used Scikit-Learn's stacking ensembler to create a model that predicts total company penalties (USD) for the next year.
* Final RMSE on the test set was $210,003. 


## Metallic Asteroid Classification:
Asteroids are classified into three main categories (C, S, and M). We are interested in the M-type (metallic) asteroids. Manually classifying asteroids can be a slow and tedious process due to the number of observations we need to gather sufficient data. The goal of this project is to predict if asteroids are metallic using data that is faster and easier to gather. We can imagine a future where humans are mining asteroids for resources. A model such as this could be used to speed up the process of searching for metallic asteroids. This could also be used to help identify the most profitable asteroids in the early stages of asteroid mining.

* Used 10-fold cross-validation and Imblearn’s SMOTE oversampling to train and evaluate a classifier that attempts to identify asteroids with high metal content.
* Compared several machine learning  models and achieved ~70% ROC AUC score and ~23% Precision-Recall AUC.


## Craigslist Used Automobile Regression:
The goal is to predict the price of used vehicles on Craigslist so that we can determine what is a "fair" price. Since my knowledge of cars is very limited, I decided to work on this project so that I don't get scammed if I ever buy a used vehicle. While I could just use an existing website to find this information, I decided that doing this myself would be more fun.

* Used Scikit-Learn to create a multiple linear regression and a random forest regression to predict the price of used vehicles.
* Achieved an average accuracy of 78.28% relative to the actual listing prices and a mean absolute error of $1952.
