import os
import requests
import json
import pytest
#with open("config.json",'r') as file:
    #data=json.load(file)
#@pytest.fixture(params=[("RAMYA","SOUMYA"), ("HARIH","SEEMA")])
#def new(request):
    #return request.param

#def test_new(new):
    #print(str(new[0]))
    #print(str(new[1]))
@pytest.fixture
def setup():
    BaseURL = "https://api.restful-api.dev/objects"
    payload1 = {"name": "lenovo2",
                "data": {"Generation": "4th",
                         "Price": "519.99", "Capacity": "256 GB"}
                }
    print(type(payload1))
    return [BaseURL,payload1]

def test_get(setup):
    response_get =requests.get(f"{setup[0]}/{1}")
    print(response_get.status_code)
    print(response_get.json())
    print(response_get.text)

def test_post(setup):
    #payload = {
    #"name": "lenovo1"}

    response_post = requests.post(setup[0],json=setup[1])
    print(response_post.status_code)
    data=response_post.json()
    print(json.dumps(data))
    print(data['id'])
