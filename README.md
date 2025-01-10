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
  >convert the script to python and then to lambda function
>ISSUE: when i tried to execute the code in awslambda the problemwas request module cant be installed in lambda so the code is then stored inside an aws ec2 and virtual env is created inside it all the modules like pip,boto3,request is installed and then the whole is converted as a zip file and uploaded into lamda function2
2:set up the lamda zip file
>.launch ec2 ,set up a virtual environment and install all the modules
>sudo apt update
sudo apt install python3-venv

Create and activate the virtual environment:

python3 -m venv my_lambda_env
source my_lambda_env/bin/activate
nstall Dependencies (requests and boto3)
pip install requests boto3
then make it a zip file
3: upload the zip file from ec2 to laambda function
>execute the code
>Status: Succeeded
Test Event Name: (unsaved) test event

Response:
{
  "statusCode": 500,
  "body": "Error storing data in S3: An error occurred (AccessDenied) when calling the PutObject operation: User: arn:aws:sts::329599663668:assumed-role/my_lambda-role-75aqozt7/my_lambda is not authorized to perform: s3:PutObject on resource: \"arn:aws:s3:::weatherappdona/weather_data.json\" because no identity-based policy allows the s3:PutObject action"
}

Function Logs:
START RequestId: 86c3ddfd-8c0f-43a9-ba2d-ce4b1a2469d7 Version: $LATEST
END RequestId: 86c3ddfd-8c0f-43a9-ba2d-ce4b1a2469d7
REPORT RequestId: 86c3ddfd-8c0f-43a9-ba2d-ce4b1a2469d7	Duration: 3853.38 ms	Billed Duration: 3854 ms	Memory Size: 128 MB	Max Memory Used: 84 MB	Init Duration: 941.72 ms

Request ID: 86c3ddfd-8c0f-43a9-ba2d-ce4b1a2469d7
ERROR OCCURED
>to execute the code create role for getting s3 full acces
>when lambda fun is created a role is automatically created so search the role relatd to your lambda fun
>in permission >attach policies>s3 full acces>attch
>![image](https://github.com/user-attachments/assets/19e8012f-551a-48f5-88c9-e217e32ad0f4)
>suucessfully executed and output is stored in s3
>![image](https://github.com/user-attachments/assets/95b4bfaf-4b75-4873-a4c2-2f002a36ceee)



>





