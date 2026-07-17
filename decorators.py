


def main_func(func):
    func()
    def wrapper():
        print("Good moring")
        func()
        print("now i did all works , this is eveng")
        func()

    return wrapper



@main_func
def doing():
    a = 1
    b = 2
    c = a+b
    return print(c)

doing()