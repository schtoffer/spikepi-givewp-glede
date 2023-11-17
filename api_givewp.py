from dotenv import load_dotenv
import os
from requests import get
import json

def main():
    print(api_call())

def api_call(webform=290, startdate=20231101, enddate=20231231, 
type='earnings'):
   
    # Build the Stats Query
    load_dotenv()
    public_key = os.getenv("PUBLIC_KEY")
    token = os.getenv("TOKEN")
    base_url = "https://glede.kirkensbymisjon.no/"
    
    # Get earnings for the given dates
    result = get(f"{base_url}give-api/v1/stats/?key={public_key}&token={token}&type={type}&form={webform}&startdate={startdate}&enddate={enddate}")

    return json.loads(result.content).get('earnings')[0][f"{webform}"]

if __name__ == "__main__":
    main()
