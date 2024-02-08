<!-- [![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=13655493&assignment_repo_type=AssignmentRepo) -->

<!-- ![](./Deployment/IKN_LOGO.JPG) -->
# About IKN PROPERTY

<p align="center">
    <img src="./Deployment/IKN_LOGO2.png">
</p>
Leveraging the most recent price data, this application serves as a price estimation tool designed to assist developers and homeowners in estimating and determining the value of their residential properties in IKN (Ibu Kota Nusantara). This application will be an invaluable tool for potential homebuyers, investors, and stakeholders seeking insights into property values in this emerging capital city.

# Project's Background
The Indonesian government's decision to relocate the national capital to the Kalimantan area, with the new capital named IKN (Ibu Kota Nusantara), a new era of development and growth is anticipated in the region. The establishment of a new capital city brings about changes in infrastructure, economic activities, and the real estate market. The objective is to create a predictive model application that can estimate house prices in the IKN area. 

# About Dataset
The dataset used to build the house price prediction model for the IKN area is obtained through web scraping from [rumah123.com](https://www.rumah123.com/). This dataset aims to capture a comprehensive view of the real estate market in Balikpapan. 


# Conclusion 
1. EDA Conclusion :
The analysis of the dataset reveals several key trends in the Balikpapan real estate market. Most houses feature land and building areas below 500 square meters, and larger areas correlate with higher prices. Balikpapan city commands the highest average house prices (IDR 2.4 billion) due to its central location, while the East Balikpapan area, farther from the city center, shows the lowest prices (IDR 1.3 billion). Ownership Certificate is the most common certificate type in home sales, constituting 86% of transactions. The majority of houses for sale are situated in the South Balikpapan area. Furniture condition data is often missing, and a strong correlation exists between Building Area, Land Area, Bedrooms, and house prices, indicating their impact on property values. 

2. Model Conclusion :
The model used for this detection is XGBRegressor Regression Model which Hyperparameter have been tuned. And the model achieved 88% R² Train Score and 83% R² Test Score.

# Recommendation 
1. Given the strong correlation between house features (Luas Bangunan, Luas Tanah, Kamar Tidur) and prices, real estate developers or sellers may consider focusing on properties with larger and well-designed living spaces. Emphasizing these features in marketing materials could attract potential buyers seeking spacious and comfortable homes.
                
2. For properties in the East Balikpapan area, where prices are comparatively lower, there may be an opportunity for real estate investors to explore strategic development projects or renovations to enhance the appeal of the area. Highlighting any upcoming infrastructure developments or amenities could also contribute to increased property values over time.
                 
3.  Additionally, since Sertifikat Hak Milik is the most common certificate type, real estate professionals should streamline processes related to this type of certificate to facilitate smoother transactions. Providing clear information and guidance on certificate-related matters can build trust and simplify the buying process for potential customers.

# Try IKN PROPERTY here


# Meet our team
 - Masayu Anandita Prameswari | [LinkedIn](https://www.linkedin.com/in/masayuanandita-/) | [Github](https://github.com/masayuanandita)
 - Gilbert Kurniawan Hariyanto | [LinkedIn](https://www.linkedin.com/in/gilbert-kurniawan-h/) | [Github](https://github.com/gilbertk27)
 - Ade William Tabrani | [LinkedIn](https://www.linkedin.com/in/ade-william-tabrani/) | [Github](https://github.com/AdeWT/)
 - Mardhya Malik Nurbani | [LinkedIn](https://www.linkedin.com/in/mnurbani/) | [Github](https://github.com/mnurbani97)

