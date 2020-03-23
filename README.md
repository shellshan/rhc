# RHC

REST Host Controller

Used to run host command through REST service.

## Required

  Any Linux Distribution
	
  Python3.x

## Installation

  Should be run under the root privilage
  
  cd rhc

  python3 -m venv venv

  source venv/bin/activate

  pip install -f requirements.txt

  python app.py

## API

### Auth

> URL : http://localhost:5000/api/v1/auth

> Payload : {"username": "xxx", "password": "yyy"}

> Response : 

> {
>    "token": ">valid token<"
> }
  
  
### Execute

> URL : http://localhost:5000/api/v1/execute

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
