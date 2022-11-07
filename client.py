# client.py

import requests

in_data = {'patient_id': 453, 'attending_username': 'mimi.m', 'patient_age': 5}

# konrad type here
in_data = {'attending_username': "konrad.m",
           'attending_email': 'kon@gmail.com',
           'attending_phone': "304-444-9090"}

r = requests.post("http://vcm-29248.vm.duke.edu:5000/api/new_attending",
                  json=in_data)
print(r.status_code)
print(r.text)

in_data = {'patient_id': "1",
           'heart_rate': '50'}

r = requests.post("http://vcm-29248.vm.duke.edu:5000/api/heart_rate",
                  json=in_data)
print(r.status_code)
print(r.text)

r = requests.get("http://vcm-29248.vm.duke.edu:5000/api/status/1")
print(r.status_code)
print(r.text)
# ******************************************************************************

# mimi type here

r = requests.get("http://vcm-29248.vm.duke.edu:5000/api/patients/ferd.j")
print(r.status_code)
print(r.text)

in_data = {"patient_id": '24',
           "attending_username": 'lemon.b',
           "patient_age": '22'}

r = requests.post("http://vcm-29248.vm.duke.edu:5000/api/new_patient",
                  json=in_data)
print(r.status_code)
print(r.text)

r = requests.get("http://vcm-29248.vm.duke.edu:5000/api/heart_rate/1")
print(r.status_code)
print(r.text)

r = requests.get("http://vcm-29248.vm.duke.edu:5000/api/heart_rate/average/2")
print(r.status_code)
print(r.text)

in_data = {'patient_id': 4, 'heart_rate_average_since': '2018-09-18 13:55:26'}

r = requests.post("http://vcm-29248.vm.duke.edu:5000/api/heart_rate/'\
                  'interval_average", json=in_data)
print(r.status_code)
print(r.text)

r = requests.get("http://vcm-29248.vm.duke.edu:5000/api/patients/mimi.m")
print(r.status_code)
print(r.text)
