class Singleton:

    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def func(self):
        print("Hey there, this is from the singleton class")


c1 = Singleton()
c1.func()

c2 = Singleton()
c2.func()

print("Are the both class instances same?: ", c1 is c2)  # O/P: True