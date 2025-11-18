import asyncio

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

    async def run(self):
        self.__is_run = True

        while self.__is_run:
            self.__set_mileage()
            await asyncio.sleep(0)

    def stop(self):
        self.__is_run = False

async def test():
    haval = UsedCar("Haval", 2020)
    haval.__mileage = 100000
    haval.get_mileage() # Вернет 270000
    #   haval.__set_mileage() # Здесь будет ругаться компилятор

    asyncio.create_task(haval.run())
    await asyncio.sleep(1)
    haval.stop()
    haval.get_mileage() # Вернет 270000

if __name__ == "__main__":
    asyncio.run(test())