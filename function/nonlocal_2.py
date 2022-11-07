def outer():
    a = 2
    b = 3

    def inner():
        nonlocal a # nonlocal -> outer의 지역변수 a를 사용
        a = 100
    inner()

    print('locals in outer : a = {} , b = {}'.format(a , b))

if __name__ == '__main__':
    outer()