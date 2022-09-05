from operator import truediv


def interface():
    print("Blood Calculator")
    print("Options:")
    print("9 - Quit")
    print("1 - Analyze HDL")
    print("3 - Analyze LDL")
    keep_running = True
    while keep_running:
        choice = input("Enter choice: ")
        if choice == '9':
            return
        elif choice == "1":
            HDL_driver()

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

def output_HDL_result(hdl_value, charac):
    print("The result for an HDL value of {} is {}".format(hdl_value, charac))

def input_LDL():
    LDL_input = input("Enter the LDL value:")
    return int(LDL_input)

interface()