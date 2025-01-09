import requests

def lambda_handler(event, context):
    # Define the URL and parameters
    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        'q': 'bangalore',
        'key': '7580f3b2ceee433bb9880636250401'
    }

    # Send the GET request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        print(data)
    else:
        print(f"Error: {response.status_code}")

    return {
        'statusCode': 200,
        'body': "Weather data fetched successfully!"
    }

