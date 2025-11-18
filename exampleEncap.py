from exampleObjClass import Car

class UsedCar(Car):
    def __init__(self, model, year):
        super().__init__(model, year)
        self.__mileage = 270000
        self.__is_run = False

    def get_mileage(self):
        print(f"Пробег машины: {self.__mileage} км.")

    def __set_mileage(self):
        self.__mileage += 20

    def run(self):
        self.__is_run = True

        while self.__is_run:
            self.__set_mileage()

    def stop(self):
        self.__is_run = False

def test():
    haval = UsedCar("Haval", 2020)
    haval.__mileage = 100000
    haval.get_mileage() # Вернет 270000
    #   haval.__set_mileage() # Здесь будет ругаться компилятор

   # haval.run()
   # haval.stop()
   # haval.get_mileage() # Вернет 270000

if __name__ == "__main__":
    test()