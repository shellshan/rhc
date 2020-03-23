import requests
import json

url = "http://master-vm.novellab.com:5000/api/v1/execute"

payload = {"cmd": "ls -lhrt", "timeout": 5}
payload = json.dumps(payload)

headers = {
  'Content-Type': 'application/json',
  'Content-Length' : str(len(payload)), # FIX: Not working without Length
  'x-access-tokens': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJleHAiOjE1ODQ5OTkwNjMsImlhdCI6MTU4NDk5NzI2M30.P99x0U8mcuAyjXSfgfVsF-tcg9SCVP-jM4wxNysvM3o',
}

response = requests.request("POST", url, headers=headers, data = payload)

out = response.json()

print(out['output']['stdout'])
