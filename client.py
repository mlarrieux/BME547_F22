# client.py

import requests

out_data = {"name": "David Ward",
            "hdl_value": 150}

r = requests.post("http://127.0.0.1:5000/hdl_check", json=out_data)
print(r.status_code)
print(r.text)


out_data = {'a': 5, 'b': 9}

r = requests.post("http://127.0.0.1:5000/add_numbers", json=out_data)
print(r.status_code)
print(r.text)
