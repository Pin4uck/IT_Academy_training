class Stack:

    def __init__(self):
        self.__item_pool = []

    def add_item(self, car):
        self.__item_pool.append(car)

    def size_pool(self):
        return len(self.__item_pool)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            while self.__item_pool:
                return self.__item_pool.pop()
            raise RuntimeError('Stack is empty!')
        except RuntimeError as error:
            print(error)
            raise StopIteration


class Queue:

    def __init__(self):
        self.__item_pool = []

    def add_item(self, car):
        self.__item_pool.append(car)

    def size_pool(self):
        return len(self.__item_pool)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            while self.__item_pool:
                return self.__item_pool.pop(0)
            raise RuntimeError('Queue is empty!')
        except RuntimeError as error:
            print(error)
            raise StopIteration


if __name__ == "__main__":
    while True:
        select = input('Hello!\n'
                       'Enter "1" - if you want to play with the queue.\n'
                       'Enter "2" - if you want to play with the stack.\n')
        if select == '1':
            s = Queue()
            break
        elif select == '2':
            s = Stack()
            break
        else:
            print('Wrong input, try again!')
    while True:
        query = input(f'Enter "add" - if you want to add items to the {"queue" if select == "1" else "stack"}.\n'
                      f'Enter "num" - if you want to know the number of elements on the {"queue" if select == "1" else "stack"}.\n'
                      f'enter "get" - if you want to get an item off the {"queue" if select == "1" else "stack"}.\n'
                      '\tIf you\'ve played enough, press "Enter"!=)\n').lower()
        if query == 'add':
            item = input('Enter an item! Or press "Enter"\n')
            while item:
                s.add_item(item)
                item = input('Enter an item! Or press "Enter"\n')
        elif query == 'num':
            a = s.size_pool()
            print(f'There are "{a}" elements on the {"queue" if select == "1" else "stack"}!')
        elif query == 'get':
            a = iter(s)
            num_get = int(input('How many items do you want to get?\n'))
            for i in range(num_get):
                print(f'{"Queue" if select == "1" else "Stack"} element is: {next(a)}')
        elif not query:
            print('Bye!')
            break
        else:
            print('Wrong input, try again!')
