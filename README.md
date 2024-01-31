# SWEET SAGE - SUGARCANE YIELD PREDICTION
<a target="blank"><img align="center" src="https://github.com/Nikki-ta/Nikita/blob/main/image2.jpeg"></a>

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


