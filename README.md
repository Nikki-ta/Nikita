# SWEET SAGE - SUGARCANE YIELD PREDICTION
<a target="blank"><img align="center" src="https://github.com/Nikki-ta/Nikita/blob/main/image2.jpeg" height="600" width="1000"></a>

## About
In this project, we utilized NDVI data and weather data to forecast sugarcane yield in the sugarcane belt districts of Uttar Pradesh. Employing Multiple Linear Regression (MLR), LSTM (Long short-term memory) and Random Forest (RF) models, we computed yield predictions based on Sentinel-2 satellite imagery from Google Earth Engine and weather data from the ERA-5 Land dataset by ECMWF (2015-2023). The investigation involved analyzing expected versus actual yields, comparing model performances, and visualizing NDVI time series data annually.

## Problem Statement
Traditional methods of sugarcane yield prediction are time-consuming and often lack accuracy. In the context of extensive research conducted in the field of sugarcane yield prediction, we aim to improve the precision and efficiency of this process. Our approach integrates different machine learning algorithms like MLR, LSTM and RF in combination with meteorological and NDVI data obtained from remote sensing technology. The primary objective is to develop a predictive model that can accurately estimate yields of Sugarcane fields of the respective Area of Interest. By doing so, we aim to provide sugarcane farmers with a valuable tool for optimizing resource management, enhancing crop productivity, and contributing to sustainable agriculture practices.

## Tools and technologies used
* Jupyter Notebook
* Python Programming Language
* Normalized Difference Vegetation Index (NDVI)
* Meteorological Data

## Software required
* ### Scikit-Learn and TensorFlow Libraries:
Scikit-Learn is used for implementing machine learning algorithms, while TensorFlow facilitates the development and training of deep learning models, including LSTM.
* ### Pandas and NumPy Libraries:
Pandas is employed for data manipulation and analysis, and NumPy is used for numerical operations, enhancing the efficiency of data handling.
* ### Matplotlib and Seaborn Libraries:
Matplotlib and Seaborn are utilized for data visualization, providing insightful graphs and plots to interpret the results effectively.

## Machine learning models used are:
* LSTM (Long Short-Term Memory): LSTM is a type of recurrent neural network (RNN) suitable for sequence prediction tasks. In this project, LSTM is applied for time-series analysis of NDVI and meteorological data.
* Random Forest (RF): RF is an ensemble learning method used for classification and regression. In the project, RF is employed for predictive modeling, offering robust and accurate results.
* Multiple Linear Regression (MLR): MLR is a statistical method used for modeling the relationship between multiple independent variables and a dependent variable. In this project, MLR aids in understanding the correlation between various factors affecting sugarcane farming.

## Dataset
To create our dataset, we collected NDVI and meteorological data using GEE API of our area of interest over a period of 8 years starting from 1.1.2015 to 1.1.2023 and integrated both the csv files on the basis of time series parameters. We extracted NDVI for these dates and created a collection of images. However, these images cannot be directly used to train our LSTM model and thus data pre-processing was required. 

<a target="blank"><center><img src="https://github.com/Nikki-ta/Sweet-Sage/blob/main/Images/aoi%20ndvi.jpeg" height="300" width="50%"></center></a>

## Data Preprocessing
Duplicates were removed from the data and only one reading per day was kept in the dataset. Finally, interpolation was done to ensure that readings for all days were available. After the preprocessing the data was then converted to a time series data and then supervised data which is a favorable format for  training and testing the LSTM model. 
<a target="blank"><center><img src="https://github.com/Nikki-ta/Sweet-Sage/blob/main/Images/graph.png" height="300" width="50%"></center></a>




## Getting Started
To get started with this project:

  1. Clone this repository to your local machine.
  2. Ensure you have Jupyter Notebook and VS Code installed and running.
  3. Install the required dependencies.
  4. Open and run the Jupyter Notebook "Final_Minor_Project(SweetSage)_checkpoint.ipynb" to train and evaluate the model.
  5. Authorize and authenticate by entering the required key to use the google earth engine API.
  6. Run all the cells and save the most accurate model(MLR here) using .sav extension.
  7. Download the entire project from here and then import it in VS Code.
  8. Run apps.py file which integrates our model with flask.
  9. Model is finally deployed and you'll see a webpage with the some entries.
  10. Fill those entries and you'll see another webpage with the predicted yield.   


