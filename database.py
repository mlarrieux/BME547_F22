class Patient:

    def __init__(self) -> None:
        self.first_name = ''
        self.last_name = ''
        self.id = ''
        self.age = ''
        self.tests = []

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


def create_patient_entry(patient_first_name, patient_last_name, patient_id,
                         patient_age):

    # if we want a dictionary

    # new_patient = {'first name': patient_first_name,
    #                'last name': patient_last_name,
    #                "ID": patient_id, 'age': patient_age, 'test_results': ''}

    # OR

    # new_patient = Patient()
    # new_patient.first_name = patient_first_name
    # new_patient.last_name = patient_last_name
    # new_patient.id = patient_id
    # new_patient.age = patient_age

    # OR

    new_patient = Patient(patient_first_name, patient_last_name, patient_id,
                          patient_age)
    return new_patient


def get_full_name(patient):
    return patient['first name'] + ' ' + patient['last name']


def adult_or_minor(patient):
    if patient['age'] >= 18:
        return 'adult'
    else:
        return 'minor'


def print_database(db):
    print("This is an output of all patients and information:\n\n")
    for patient_key in db:
        print("First Name: {}\t Last Name: {}\t Patient ID: {}\t Patient\
             Age: {}".format(get_full_name(db[patient_key]),
              db[patient_key]['last name'],
              db[patient_key]["ID"], db[patient_key]['age']))


def find_patient(db, id_no):
    patient = db[id_no]
    return patient


def add_test_to_patient(db, id_no, test_name, test_value):
    patient = find_patient(db, id_no)
    patient['test_results'] = (test_name, test_value)


def main():
    db = {}
    db[1] = create_patient_entry("Ann", "Able", 1, 30)
    db[2] = create_patient_entry("Bob", "Boyles", 2, 34)
    db[3] = create_patient_entry("Chris", "Chou", 3, 25)
    add_test_to_patient(db, 3, "HDL", 100)
    print_database(db)

    print("Patient {} is a {}".format(get_full_name(db[2]),
                                      adult_or_minor(db[2])))


if __name__ == "__main__":
    main()
