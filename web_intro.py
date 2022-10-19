import requests

# output_info = {'name': 'Mimi Larrieux',
#                'net_id': 'ml522',
#                'e-mail': 'ml522@duke.edu'}

# r = requests.post('http://vcm-21170.vm.duke.edu:5000/student',
#                   json=output_info)

message_op = {"user": 'mimi', "message": 'sup brah'}

r = requests.post('http://vcm-21170.vm.duke.edu:5001/add_message',
                  json=message_op)

messages =\
    requests.get('http://vcm-21170.vm.duke.edu:5001/get_messages/konrad')

print(messages.text)
