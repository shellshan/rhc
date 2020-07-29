# RHC

REST Host Controller

Used to run host command through REST service.

## Required

  Any Linux/Unix Distribution
	
  Python3.5 and above

## Installation

  **Service should run under the root privilage**
  
  ```
  # clone the repo
  
  cd rhc

  python3 -m venv venv

  source venv/bin/activate

  pip install -r requirements.txt
  
  mkdir /var/log/rhc/

  python app.py
  ```

## API

### Auth

> URL : http://localhost:5000/api/v1/auth

> Headers : Content-Type: application/json

> Payload : {"username": "xxx", "password": "yyy"} #Note: Use system(where RHC deployed) username/password

> Response : 

> {
>    "token": ">valid token<"
> }
  
  
### Execute

> URL : http://localhost:5000/api/v1/execute

> Headers : Content-Type: application/json, x-access-tokens: >valid token from auth<

> Payload : {"cmd": "ls -lhrt"}

> Reponse : 

> {
>    "output": {
>        "returncode": 0,
>        "stderr": "",
>        "stdout": "total 0\n-rw-r--r-- 1 test test 0 Mar 24 02:20 a\n-rw-rw-r-- 1 test test 0 Mar 24 02:31 b\n"
>    },
>    "error": null
> }
