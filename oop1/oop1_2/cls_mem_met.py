class A:
    c_mem = 10

    @classmethod
    def cls_f(cls): # class 자체의 cls를 인수로 사용함.
        print(cls.c_mem) #10

    def __init__(self , num): 
        self.i_mem = num
    
    def ins_f(self):
        print(self.i_mem)

if __name__ == '__main__':
    print(A.c_mem)
    A.cls_f()

    a = A(20) #init
    print(a.c_mem)
    a.cls_f()