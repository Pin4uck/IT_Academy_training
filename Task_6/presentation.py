import business_logic as bl


def get_query(message):
    return input(message + "\n")


def show_message(message):
    print(message)


def calc(res, operator):
    while True:
        inp_expression = bl.valid(get_query("Please enter an expression:"))
        expression = f'{res}{operator}{inp_expression}'
        res = bl.string_count(inp_expression if res == "new" else expression)
        show_message(f'Your result is: {res}')
        return res


def save(res):
    bl.save_result(res)
    show_message('Result saved!')


def show():
    show_message(bl.show_results())


def clear():
    return bl.clear()


if __name__ == "__main__":
    first_expr = bl.valid(get_query("Please enter an expression"))
    result = bl.string_count(first_expr)
    show_message(f'Your result is: {result}')
    while True:
        operation = get_query("Please select the operation:\n"
                              "\t'+' to the result, '-' from the result, '*' the result, '/' the result\n"
                              "\t'new' to count new an expression, 'save' the result, 'show' the results,  'clear' the result, 'exit':")
        if operation == "+":
            result = calc(result, '+')
        elif operation == "-":
            result = calc(result, '-')
        elif operation == "*":
            result = calc(result, '*')
        elif operation == "/":
            result = calc(result, '/')
        elif operation == "new":
            result = ''
            calc(operation, None)
        elif operation == "save":
            save(result)
        elif operation == "show":
            show()
        elif operation == "clear":
            clear()
        elif operation == "exit":
            clear()
            break
        else:
            show_message("Wrong input, try again!")
            continue
