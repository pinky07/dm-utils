import requests
import json
def test():
  url = "https://stoplight.io/mocks/batchdata/batchdata/20349728/property/lookup/all-attributes"

  payload = json.dumps({
    "requests": [
      {
        "address": {
          "street": "101 Portsmouth Cir",
          "city": "Victoria",
          "state": "TX",
          "zip": "77904-2501"
        }
      }
    ]
  })
  headers = {
    'Authorization': 'Msj1je96lIBvEYYUytA91FNDnnRz6uHIRWyAFrew',
    'Content-Type': 'application/json',
    'Cookie': 'GCLB=CJTw7omUhsK5mgE; __cf_bm=7HovQkAHIaUcV9ZOQRDuyFroh.j5l.UBVcu.AyQaxjg-1651253112-0-ARWX3PTqDGwHjsQS8tjRYOz//QtCHmkLf0tFXH+U23Czxi6un0Ot+VEwGEKD1HiddeLmAUUTu5f+B2n+ijA6KjY='
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  pretty_json = json.loads(response.text)
  print (json.dumps(pretty_json, indent=2))
test()