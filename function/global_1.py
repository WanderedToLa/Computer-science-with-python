# 함수안에서 전역변수 접근
g_var = 10

def func():
    print('g_var = {}'.format(g_var))

if __name__ == '__main__':
    func()