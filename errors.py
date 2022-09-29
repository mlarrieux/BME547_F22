def function_name():
    names = ['mimi', 'michael', 'jiselle']

    try:
        bestie = names[4]
    except IndexError:
        print("The index 4 does not exist in the list names.")


def main():
    function_name()


if __name__ == "__main__":
    main()
