import time
import random

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def calc(a, b, operation):
    print(operation(a, b))


class Producer:
    def __init__(self):
        self.on_value = None

    def start(self):
        if self.on_value is None:
            print('on_value callback must be set')
            return
        while True:
            time.sleep(random.randint(1, 5))
            value = random.randint(100, 1000)
            # Call the callback function with the current value
            self.on_value(value)


def get_value(value):
    print("We got the value:", value)


def save_value(value):
    with open('values.txt', 'a') as output:
        output.write(str(value) + '\n')


def main():
    producer = Producer()
    # Define a callback
    producer.on_value = get_value
    producer.start()


if __name__ == '__main__':
    main()
