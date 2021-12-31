# Задание: Написать функцию для вычисления n первых чисел Фибоначчи.
# Примеры вызова:
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34

def valid():
    while True:
        try:
            input_data = int(input('Enter the number of fibonacci numbers:\n'))
            if input_data < 0:
                print('Incorrect input, please try again!')
                continue
            break
        except ValueError:
            print('Incorrect input, please try again!')
            continue
    return input_data


def fib(n, a=0, b=1, res_fib=[]):
    if n > 0:
        res_fib.append(a)
        fib(n - 1, b, a + b, res_fib)
    return res_fib


if __name__ == '__main__':
    fib(valid())
