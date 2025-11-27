import json
import requests
api_url = "http://localhost:58001/api/v1/ticket"

headers = {
    "content-type": "application/json"
}

body_json = {
    "username": "tp-redes",
    "password": "admin"
}

resp = requests.post(api_url, json.dumps(body_json), headers=headers)

print("Ticket request status: ", resp.status_code)
response_json = resp.json()
print (response_json)
serviceTicket = response_json["response"]["serviceTicket"]

print("The service ticket number is: ", serviceTicket) 