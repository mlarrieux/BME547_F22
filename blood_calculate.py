from operator import truediv


def interface():
    print("Blood Calculator")
    print("Options:")
    print("9 - Quit")
    print("1 - Analyze HDL")
    print("3 - Analyze LDL")
    print("5 - Analyze Total Cholesterol")
    keep_running = True
    while keep_running:
        choice = input("Enter choice: ")
        if choice == '9':
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "3":
            LDL_driver()
        elif choice == "5":
            total_cholesterol_driver()

def input_HDL():
    HDL_input = input("Enter the HDL value:")
    return int(HDL_input)

def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"

def HDL_driver():
    hdl_value = input_HDL()
    answer = check_HDL(hdl_value)
    output_HDL_result(hdl_value, answer)
    return hdl_value

def output_HDL_result(hdl_value, charac):
    print("The result for an HDL value of {} is {}".format(hdl_value, charac))

def input_LDL():
    LDL_input = input("Enter the LDL value:")
    return int(LDL_input)

def check_LDL(LDL_value):
    if LDL_value >= 190:
        return "Very High"
    elif 160 <= LDL_value < 190:
        return "High"
    elif 130 <= LDL_value < 160:
        return "Borderline High"
    else:
        return "Normal"

def LDL_driver():
    ldl_value = input_LDL()
    answer = check_LDL(ldl_value)
    output_LDL_result(ldl_value, answer)
    return ldl_value

def output_LDL_result(ldl_value, charac):
    print("The result for an LDL value of {} is {}".format(ldl_value, charac))

def total_cholesterol_driver():
    ldl_value = LDL_driver()
    hdl_value = HDL_driver()
    total_cholesterol_value = ldl_value + hdl_value
    answer = check_total_cholesterol(total_cholesterol_value)
    output_total_cholesterol_result(total_cholesterol_value, answer)

def check_total_cholesterol(total_cholesterol_value):
    if total_cholesterol_value >= 240:
        return "High"
    elif 200 <= total_cholesterol_value < 240:
        return "Borderline High"
    else:
        return "Normal"

def output_total_cholesterol_result(total_cholesterol_value, charac):
    print("The result for a total cholesterol value of {} is {}".format(total_cholesterol_value, charac))

interface()