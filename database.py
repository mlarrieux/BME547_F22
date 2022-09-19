def create_patient_entry(patient_name, patient_id, patient_age):
    new_patient = [patient_name, patient_id, patient_age, []]
    return new_patient


def main():
    db = []
    db.append(create_patient_entry("Ann Able", 1, 30))
    db.append(create_patient_entry("Bob Boyles", 2, 34))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    add_test_to_patient(db, 3, "HDL", 100)
    print(find_patient(db, 3))
    print(db)

    room_list = ["room 1", "room 2", "room 3", "room 4"]

    for i, patient in enumerate(db):
        print(i)
        print("name = {}, Room = {}".format(patient[0], room_list[i]))

    for patient, room in zip(db, room_list):
        print("Name = {}, Room = {}".format(patient[0], room))


def print_database(db):
    print("This is an output of all patients and information:\n\n")
    for patient in db:
        name = patient[0].split(" ")
        print("First Name: {}\t Last Name: {}\t Patient ID: {}\t Patient\
             Age: {}".format(name[0], name[1], patient[1], patient[2]))


def find_patient(db, id_no):
    for patient in db:
        if patient[1] == id_no:
            return patient
    return False


def add_test_to_patient(db, id_no, test_name, test_value):
    patient = find_patient(db, id_no)
    patient[3].append((test_name, test_value))


if __name__ == "__main__":
    main()
