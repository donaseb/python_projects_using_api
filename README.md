# python_projects_using_api
This repository contains two Python projects that utilize API calls within Python scripts.
1***.project 1:***
 This project retrieves the current weather in Bangalore using the WeatherAPI.com through API calls in a Python script. The script runs daily at 8 AM as an AWS Lambda function, and the output is sent via email through SNS.
 steps to createthe project
 **************************
 1.Set Up the Weather API: 
   >signup to wheather api app
   >create an api key in the app
   > go to api documentation: we know that there is a base url for this app, Base URL: http://api.weatherapi.com/v1 then to it add the other details as it is said in the           documents
   >![image](https://github.com/user-attachments/assets/d231b2ce-4ae8-4ba6-bf59-e2cf5046c07e)
  >as shownin image the current wheather api url will be : http://api.weatherapi.com/v1//current.json
  >![image](https://github.com/user-attachments/assets/8a83ef04-f916-4f5f-a7e0-628640812440)
  >q=bangalore
  >A GET request is used to fetch information from the server, and since your task is to get weather data, GET is the most appropriate HTTP method.
  >then go to api explorer>clickon link to go to swager tool> authorize using your api key> click get current json>provide q=bangalore and exxecute>
  >![image](https://github.com/user-attachments/assets/bf04eda9-a975-4cca-ace0-cb1cf6c5ed51)
  >convert the script to python .
2.Set Up AWS Lambda Function.
  >


