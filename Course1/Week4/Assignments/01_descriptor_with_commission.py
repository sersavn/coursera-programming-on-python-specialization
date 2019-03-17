'''
Часто при зачислении каких-то средств на счет с нас берут комиссию.
Давайте реализуем похожий механизм с помощью дескрипторов.
Напишите дескриптор Value, который будет использоваться в нашем классе Account.
'''

class Value:
    def __init__(self):
        self.value = None

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        self.amount = value * (1-obj.commission)

'''
class Account:
    amount = Value()
    def __init__(self, commission):
        self.commission = commission

new_account = Account(0.1)
new_account.amount = 100

print('finally', new_account.amount)
'''
