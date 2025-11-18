from abc import ABC, abstractmethod
###
class AbstractCar(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def refuel(self):
        pass
#dsa##gfdgsadg
class GasCar(AbstractCar):
    def start_engine(self):
        print("Запускаю бензиновый двигатель... РрррРРРрРрРр!")

    def refuel(self):
        print("Заправляю бензином на АЗС.")

class ElectricCar(AbstractCar):
    def start_engine(self):
        print("Включаю электромотор... Тишина!")

    def refuel(self):
        print("Подключаю к зарядке.")

def test():
    def use_car(car: AbstractCar):
        car.start_engine()
        car.refuel()

    volga = GasCar()
    tesla = ElectricCar()

    use_car(volga)
    use_car(tesla)

if __name__ == "__main__":
    test()