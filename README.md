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
  >go to awsconsole
  > create function> Select Author from Scratch.>give fun name weather_app> sleelct python as runtime>Role: For now, you can choose Create a new role with basic Lambda permissions. This will create a role that allows Lambda to log to CloudWatch logs.>clickcreate fun
>Now that your Lambda function is created, you'll be taken to the function editor. Copy the Python code for fetching weather data and paste it into the editor:
>Click on Deploy to save your changes.
3.Set up CloudWatch Events to Trigger Lambda Every Day at 8 am
  >Go to CloudWatch:
  > Create a Rule in CloudWatch Events:
  >In CloudWatch, on the left-hand sidebar, go to Rules under the Events section.
  >Click on the Create rule button.
4.Set Rule to Trigger at 12:05 PM Every Day:
  >Select Event Source: Choose Schedule.
  >select the schedule pattern as
>![image](https://github.com/user-attachments/assets/a3f7a3d0-5e8d-46ed-b9c7-1c341eec0d1d)
>in the image the cron job is set at 12.30 pm every day but tom ameke it 8am every day
>cron(0 8 * * ? *)
>select instead of UST as Local time zone
>![image](https://github.com/user-attachments/assets/d5780e1f-ebcd-45a4-b66b-12359cc1b025)
>selct the target as lambda function also selct the function
>Configure Input (Optional):give as default additional settinsalso default
5 create iam role to allowcloud watch to access and Add Permissions to Allow CloudWatch to Trigger Lambda
>





