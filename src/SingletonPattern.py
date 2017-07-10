class SingletonMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            # 不在class 的目录中
            # no instance
            cls._instance[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class SingletonInstance1(metaclass=SingletonMeta):
    def __init__(self, val):
        self.store = val

    @staticmethod
    def get_instance():
        return SingletonInstance1()

    def show(self):
        print(self.store)


class SingletonInstance2(metaclass=SingletonMeta):
    def __init__(self, name_str):
        self.store = name_str

    def show(self):
        print(self.store)


if __name__ == '__main__':
    ins1 = SingletonInstance1(3)
    ins1.show()
    ins2 = SingletonInstance1.get_instance()
    ins1.show()
    ins2.show()
    print('ins1 == ins2 : {}'.format(
        ins1 is ins2
    ))
    
    ins3 = SingletonInstance2('name')
    ins3.show()

