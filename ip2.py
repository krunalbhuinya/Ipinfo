#this tool make by kx207
#python program ip address info 
import os
import requests
import time

def bb():
   os.system('clear')
   print("""

██╗███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗
██║████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔═══██╗╚██╗ ██╔╝
██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║   ██║ ╚████╔╝
██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║   ██║  ╚██╔╝
██║██║ ╚████║██║     ╚██████╔╝██████╔╝╚██████╔╝   ██║
╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝

                                    ip address info
api use this "http://ip-api.com/json/"
""")
#print("save logs in " + ipinfo)

#import requests 
bb()
api_url = 'http://ip-api.com/json/' 
mac = input('Enter ip address and if your ip address pass enter :-') 
api_key = '?fields=status,status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query'
# Send HTTP GET request to the API endpoint
while True:
     response = requests.get(api_url+mac+api_key)
     bb()
# Check if the request was successful
     if response.status_code == 200:
    # Convert response to JSON format
        json_data = response.json()
    # Print the JSON output
        print(json_data) 
        time.sleep(10)
        ipinfo = 'ipinfo.json'
        with open(ipinfo, "a") as file:
             file.write(f"ipinfo: {json_data}\n")
             file.write(F"TIME: ")
     print("save logs in ")
     print(ipinfo)

else:
        # Print an error message in case of failure
        print('Request failed with status code:', response.status_code)
bb()
