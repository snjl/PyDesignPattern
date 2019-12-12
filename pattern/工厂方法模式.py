from abc import ABCMeta, abstractmethod, ABC


# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Coffee(metaclass=ABCMeta):
    """咖啡"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def getTaste(self):
        pass


class LatteCoffee(Coffee):
    """拿铁咖啡"""

    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return "轻柔而香醇"


class MochaCoffee(Coffee):
    """摩卡咖啡"""

    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return "丝滑与醇厚"


class CoffeeFactory(metaclass=ABCMeta):
    """咖啡机"""

    @staticmethod
    def getCoffee():
        pass


class MochaCoffeeFactory(CoffeeFactory):
    @staticmethod
    def getCoffee():
        return MochaCoffee("摩卡咖啡豆")


class LatteCoffeeFactory(CoffeeFactory):
    @staticmethod
    def getCoffee():
        return LatteCoffee("拿铁咖啡豆")


def testCoffeeMaker():
    latte = MochaCoffeeFactory.getCoffee()
    print("%s已为您准备好了，口感：%s。请慢慢享用！" % (latte.getName(), latte.getTaste()))
    mocha = LatteCoffeeFactory.getCoffee()
    print("%s已为您准备好了，口感：%s。请慢慢享用！" % (mocha.getName(), mocha.getTaste()))


if __name__ == '__main__':
    testCoffeeMaker()
