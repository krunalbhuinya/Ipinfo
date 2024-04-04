#this tool make by kx207
#python program ip address info 
import os
import requests
import time

y =  "\033[33m"
red = "\033[31m"
rs = "\033[0m"
g = "\033[32m"
k = """

██╗███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗
██║████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔═══██╗╚██╗ ██╔╝
██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║   ██║ ╚████╔╝
██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║   ██║  ╚██╔╝
██║██║ ╚████║██║     ╚██████╔╝██████╔╝╚██████╔╝   ██║
╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝

                                    ip address info
api use this "http://ip-api.com/json/"


"""
print(red+k+rs)
url = 'http://ip-api.com/json/' 
m = input(f'{y}Enter ip address and if your ip address pass enter :-{rs}') 
y = '?fields=status,status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query'


def data(m): #api requests funconsan
 response = requests.get(url+m+y)
 data = response.json()
 return data
data = data(m)

print("  ")
print(f"{g}ip: {data['query']}{rs}")
if 'status' in data:                                         
  print(f"{g}status: {data['status']}{rs}")
else:                                                         
  print(f"{red}Status information not available{rs}")
print(f"{g}continent: {data['continent']}{rs}")
print(f"{g}continentCode: {data['continentCode']}{rs}")
print(f"{g}region: {data['region']}{rs}")
print(f"{g}regionName: {data['regionName']}{rs}")
print(f"{g}city: {data['city']}{rs}")
print(f"{g}district: {data['district']}{rs}")
print(f"{g}zip: {data['zip']}{rs}")
print(f"{g}lat: {data['lat']}{rs}")
print(f"{g}lon: {data['lon']}{rs}")
print(f"{g}timezone: {data['timezone']}{rs}")
print(f"{g}offset: {data['offset']}{rs}")
print(f"{g}currency: {data['currency']}{rs}")
print(f"{g}isp: {data['isp']}{rs}")
print(f"{g}org: {data['org']}{rs}")
print(f"{g}as: {data['as']}{rs}")
print(f"{g}asname: {data['asname']}{rs}")
if 'mobile' in data:
  print(f"{g}mobile: {data['mobile']}{rs}")
else:
  print(f"{red}moblie information not available{rs}")
if 'proxy' in data:
  print(f"{g}proxy: {data['proxy']}{rs}")
else:
  print(f"{red}proxy information not available{rs}")
print(f"{g}hosting: {data['hosting']}{rs}")
if 'dns' in data:
  print(f"{g}dns: {data['dns']}{rs}")
else:
  print(f"{red}moblie information not available{rs}")
#print(f"geo: {data['geo']}")
if 'geo' in data:
  print(f"{g}geo: {data['geo']}{rs}")
else:
  print(f"{red}moblie information not available{rs}")
#print(f"dnsip: {data['ip']}")
if 'ip' in data:
  print(f"{g}gns ip: {data['ip']}{rs}")
else:
  print(f"{red}dnsip information not available{rs}")
print("  ")
with open('ipLogs.txt', "a") as file:
                   file.write(f"{k}\n")
                   file.write(f"ip: {data['query']}\n")
#             file.write(f"status: {data['status']}\n")
                   if 'status' in data:
                     file.write(f"status: {data['status']}\n")
                   else:
                     file.write("status information not available\n")
                   file.write(f"continent: {data['continent']}\n")
                   file.write(f"region: {data['region']}\n")
                   file.write(f"regionName: {data['regionName']}\n")
                   file.write(f"city: {data['city']}\n")
                   file.write(f"district: {data['district']}\n")
                   file.write(f"zip: {data['zip']}\n")
                   file.write(f"lat: {data['lat']}\n")
                   file.write(f"lon: {data['lon']}\n")
                   file.write(f"timezone: {data['timezone']}\n")
                   file.write(f"offset: {data['offset']}\n")
                   file.write(f"currency: {data['currency']}\n")
                   file.write(f"isp: {data['isp']}\n")
                   file.write(f"org: {data['org']}\n")
                   file.write(f"as: {data['as']}\n")
                   file.write(f"asname: {data['asname']}\n")
#                   file.write(f"mobile: {data['mobile']}\n")
                   if 'mobile' in data:
                     file.write(f"mobile: {data['mobile']}\n")                                     
                   else:
                     file.write("moblie information not available\n")  
                   file.write(f"hosting: {data['hosting']}\n")
#                   file.write(f"dns: {data['dns']}\n")
                   if 'dns' in data:            
                     file.write(f"dns: {data['dns']}\n")                 
                   else:
                     file.write("dns information not available\n")
#                   file.write(f"geo: {data['geo']}\n")
                   if 'geo' in data:                                                 
                     file.write(f"geo: {data['geo']}\n")                 
                   else:
                     file.write("geo information not available\n")
 #                  file.write(f"dnsip: {data['ip']}\n")
                   if 'ip' in data:                                                 
                      file.write(f"dnsip: {data['ip']}\n")                 
                   else:
                      file.write("dnsip information not available\n")
                   file.write(f"time \n")
                   file.write(f"********************************\n")      
