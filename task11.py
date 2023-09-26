def singleton(_class):
    orig_instance = None
    is_initialized = False

    new_instance = _class.__new__  # создание нового экземпляра класса
    new_init = _class.__init__

    def __new_init__(cls, *args, **kwargs):

        nonlocal is_initialized

        if not is_initialized:
            is_initialized = True
            return new_init(cls, *args, **kwargs)
        return

    def __create_new__(cls, *args, **kwargs):
        nonlocal orig_instance
        # если экземпляр класса не существовал до этого, то присвоить
        # результат созданного раннее нового экземпляра
        if orig_instance is None:
            orig_instance = new_instance(cls, *args, **kwargs)
        return orig_instance

    _class.__init__ = __new_init__
    _class.__new__ = __create_new__  # присвоение возвращенного orig_instance

    return _class

class Counter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step
        print("hello")

    def increment(self):
        self.count += self.step

@singleton
class GlobalCounter(Counter):
    def __init__(self):
        Counter.__init__(self)
        print("hdhdhd")

gc1 = GlobalCounter()
gc2 = GlobalCounter()
assert id(gc1) == id(gc2)

@singleton
class Test:
    some_global_field = 123

k1 = Test()
k2 = Test()
assert id(k1) == id(k2)

print(Test.some_global_field)