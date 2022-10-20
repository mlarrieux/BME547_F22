# client.py

import requests

in_data = {'date': "12/12/1969", 'units': "years"}

r = requests.post("http://127.0.0.1:5000/age", json=in_data)
print(r.status_code)
print(r.text)


# out_data = {'a': 5, 'b': 9}

# r = requests.post("http://127.0.0.1:5000/add_numbers", json=out_data)
# print(r.status_code)
# print(r.text)
