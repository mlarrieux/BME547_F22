import requests


# Get the IDs for two patients
name = 'ml522'
id1 =\
    requests.get('http://vcm-7631.vm.duke.edu:5002/get_patients/{}'.
                 format(name))

id1_text = id1.json()

recipient_ID = id1_text['Recipient']
donor_ID = id1_text['Donor']

# Obtain the blood type of the two patients

btr =\
    requests.get('http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}'.
                 format(recipient_ID))

recipient_bt = btr.text

btd =\
    requests.get('http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}'.
                 format(donor_ID))

donor_bt = btd.text


def is_donor(recipient, donor):
    if recipient == 'AB+':
        return True
    elif recipient == 'AB-':
        if donor == 'O-' or donor == 'B-' or donor == 'A-' or donor == 'AB-':
            return True
        else:
            return False
    elif recipient == 'B-':
        if donor == 'O-' or donor == 'B-':
            return True
        else:
            return False
    elif recipient == 'B+':
        if donor == 'O-' or donor == 'B-' or donor == 'O+' or donor == 'B+':
            return True
        else:
            return True
    elif recipient == 'A-':
        if donor == 'O-' or donor == 'A-':
            return True
        else:
            return False
    elif recipient == 'A+':
        if donor == 'O-' or donor == 'A-' or donor == 'O+' or donor == 'A+':
            return True
        else:
            return False
    elif recipient == 'O-':
        if donor == recipient:
            return True
        else:
            return False
    elif recipient == 'O+':
        if donor == 'O-' or donor == 'O-':
            return True
        else:
            return False


valid_match = is_donor(recipient_bt, donor_bt)
valid_donor = ''

if valid_match:
    valid_donor = 'Yes'
else:
    valid_donor = 'No'

out_data = {'Name': name, 'Match': valid_donor}

print(out_data)

result =\
    requests.post('http://vcm-7631.vm.duke.edu:5002/match_check',
                  json=out_data)

print(result.status_code)
print(result.text)
