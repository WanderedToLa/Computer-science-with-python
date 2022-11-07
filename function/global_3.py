g_var = 10

def func():
    global g_var # 전역변수 g_var를 함수안에서 사용
    g_var = 20

if __name__ == '__main__':
    print('g_var = {} before'.format(g_var))
    func()
    print('g_var = {} after'.format(g_var))