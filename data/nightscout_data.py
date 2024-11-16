import requests

def get_nightscout_data(api_url):
    response = requests.get(f"{api_url}/api/v1/entries.json")
    
    if response.status_code == 200:
        return response.json() 
    else:
        print("Error fetching data from Nightscout")
        return None
