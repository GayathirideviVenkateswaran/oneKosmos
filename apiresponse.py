#!/usr/bin/env python
import requests
import json
import string
from jsonschema import validate
from Library.LibraryFile import *
from Schema.schema import *
from Resources.resource import *
import sys

def test_eula():
    try:
        #Get - health API
        print("Eula Test case Started")
        resp = requests.get(HealthCheckURL) 
        print("Validate Health Check")
        if(resp.status_code==200):
             #Get - Eula of the given tenant
            resp_eula = requests.get(tenantURL+sys.argv[1])
            print("Assert Json response not null")
            assert is_not_empty(resp_eula.json())
            y = json.loads(resp_eula.content)
            print("Eula of the given tenant is : ")
            print(y["eula_b64"])
            print("Validate Schema")
            validate(instance=resp_eula.json(), schema=schema)
            print("Eula Test completed")
    except AssertionError as e:
        print("Error Occured in Assertion"+str(e))
    except ValueError as ex:
        print("Error Occured in response"+str(ex))

test_eula()