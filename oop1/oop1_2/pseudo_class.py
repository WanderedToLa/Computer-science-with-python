def person_init(name , money):
    obj = {'name':name , 'money':money} #1
    obj['give_money'] = Person[1] #2
    obj['get_money'] = Person[2]
    obj['show'] = Person[3]
    return obj

def give_money(self , other , money): #3
    self['money'] -= money
    other['get_money'](other , money) #4

def get_money(self , money):
    self['money'] += money

def show(self):
    print('{} : {}'.format(self['name'] , self['money']))

Person = person_init , give_money , get_money , show

if __name__ == '__main__':
    #obj create
    w = Person[0]('wooseok' , 5000) #5
    s = Person[0]('seokmin' , 2000)

    w['show'](w)
    s['show'](s)
    print('')

    #message passing
    w['give_money'](w , s , 2000)#6

    w['show'](w)
    s['show'](s)
