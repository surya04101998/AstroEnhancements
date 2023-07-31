import requests
import urllib.parse
import json as JSON

def make_api_call_with_query_params(base_url, params, headers):
    # Encode the query parameters
    # encoded_string = urllib.parse.quote(params["datetime"])
    params_updated=params
    # params_updated["datetime"]=encoded_string
    # Create the complete URL with encoded parameters
    complete_url = base_url+"/planet-position"

    try:
        # Make the API call
        response = requests.get(complete_url,verify=False,headers=headers,params=params_updated)
        print(complete_url)
        print(headers)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.json()  # Assuming the response is in JSON format
        else:
            print(f"Request failed with status code: {response.json()}")
            return None
    except requests.RequestException as e:
        print(f"Error occurred during API call: {e}")
        print(complete_url)
        print(headers)
        return None


# Example usage
def generate_auth_token():
    url = "https://api.prokerala.com/token"
    json = {
        "grant_type": "client_credentials",
        "client_id": "03524bd0-47ab-4741-bb18-fb83317793db",
        "client_secret": "K1dUI2hK8A96maoHlLOniPFqEk93RUw0l4LMGasM"
    }
    response = requests.post(url, json,verify=False)
    auth_response=JSON.loads(response.text)
    accessoken = "Bearer " + auth_response['access_token']
    return {"Authorization": accessoken}


if __name__ == "__main__":
    base_url = "https://api.prokerala.com/v2/astrology"  # Replace with the actual API endpoint
    query_params = {
        "ayanamsa": "1",
        "coordinates": "11.6643,78.1460",
        "datetime": "1998-10-04T17:04:21+05:30",
    }
    headers = generate_auth_token();
    response_data = make_api_call_with_query_params(base_url, query_params, headers)
    if response_data:
        print("API response:")
        print(response_data)
