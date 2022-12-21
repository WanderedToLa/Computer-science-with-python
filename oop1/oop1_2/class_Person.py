class Person:
    def __init__(self , name , money):
        self.name = name
        self.money = money

    def give_money(self , other , money):
        self.money -= money
        other.get_money(money)

    def get_money(self , money):
        self.money += money

    def show(self):
        print('{} : {}'.format(self.name , self.money))

if __name__ == '__main__':
    w = Person('wooseok' , 5000)
    s = Person('seokmin' , 2000)

    w.show()
    s.show()

    w.give_money(s , 2000)
    print('')

    w.show()
    s.show()