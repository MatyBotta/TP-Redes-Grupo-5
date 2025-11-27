import json
import requests
api_url = "http://localhost:58001/api/v1/network-device"

headers={"X-Auth-Token": "NC-3-04ada5e8703142f88e7d-nbi"}

resp = requests.get(api_url, headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()
print()
print (response_json)
print()
print()
networkDevices = response_json["response"]

for networkDevice in networkDevices:
    if networkDevice.get("reachabilityStatus") == "Unreachable":
        continue # Salta al siguiente dispositivo sin hacer nada
    print(networkDevice["hostname"], "\t", networkDevice["platformId"], "\t", networkDevice["managementIpAddress"])