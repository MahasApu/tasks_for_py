class LRUcache:

    def __init__(self, capacity=8):
        self.capacity = capacity
        self.amount_calls = 0
        self.last_called = []
        self.cache = {}

    def __replace_elem__(self, key):
        for i in range(self.last_called.index(key), len(self.last_called) - 1):
            # перемещение элемента в конец списка
            # в качестве последнего вызванного
            buffer = self.last_called[i]
            self.last_called[i] = self.last_called[i + 1]
            self.last_called[i + 1] = buffer

    def put(self, key, value):
        if key in self.cache.keys():
            self.__replace_elem__(key)
            # self.cache[key] = self.cache.pop(key)
        else:
            if self.amount_calls >= self.capacity:
                del self.cache[self.last_called[0]]
                self.last_called.pop(0)
            self.last_called.append(key)
        # обновление значения по ключу
        self.cache[key] = value
        self.amount_calls += 1

    def get(self, key):
        if key in self.cache.keys():
            self.__replace_elem__(key)
            self.amount_calls += 1
            print(self.cache[key])
        else:
            print("{elem} is not found".format(elem=key))

    def show(self):
        print("\nCurrent cache")
        print(self.cache)

    def show_last_called(self):
        print("\nCurrent last_called")
        print(self.last_called)
