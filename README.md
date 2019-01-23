# Hypothyroid prediction, a simple flask app. 

I built this flask app on a small machine learning project I did in the past. Based on previous work, I could get decent prediction with numeric testing data with Baysian approach. Neural network model with numeric data gave similar levels of performance. Although predictions would be better using all data, I just wanted a simple version of the app with less input.

Hypothyroid diseases (underactive thyroid) is a condition in which the body doesn't produce enough of important thyroid hormones. The condition may lead to various symptoms at late ages. More information about the disease is available at https://www.mayoclinic.org/diseases-conditions/hypothyroidism/symptoms-causes/syc-20350284 .

The data was from: http://archive.ics.uci.edu/ml/datasets/thyroid+disease. I used "allhypo.data" for the analysis. "allhypo.names" contains the column names of the data. The data contains several categorical data and several thyroid hormone measurements.


There are 4 classes hypothyroids:
{0: 'No hypothyroid disease', 1: 'Primary hypothyroid', 2: 'Compensated hypothyroid', 3: 'Secondary hypothyroid'}.

'Secondary hypothyroid' are very rare in this dataset, only 2 instances in the training set, 0 instance in the test set.  

I made a short video that input 2 cases of data (from test set) into the app.  The first one displayed "No hypothyroid disease". The second case displayed 'Compensated hypothyroid'.  Video link: https://youtu.be/kqXe0S70iug

The project is still in progress. I will add more html page stylings with css/bootstraps and authentication for the database access in near future.  
