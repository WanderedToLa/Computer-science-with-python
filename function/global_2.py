# 함수 안에서 지역변수 변경
g_var = 10

def func():
    g_var = 20 # 전역 변수를 변경한것이 아닌 지역변수 생성
    print('g_var ={} in function'.format(g_var))

if __name__ == '__main__':
    func()
    print('g_var ={} in main'.format(g_var))