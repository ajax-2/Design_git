# coding: utf-8
from datetime import datetime


def print_time(func):
    def result():
        print(datetime.now())
        return func
    return result()


@print_time
def print_message(message):
    print(message)


if __name__ == '__main__':
    print_message('all things is ok!')
