from exampleObjClass import Car

class SuperCar(Car):

    def __init__(self, model, year, is_turbine):
        super().__init__(model, year)
        self.is_turbine = is_turbine

    def drive_very_fast(self):
        print(f"{self.model} is driving very fast...")

    def stop(self):
        print(f"{self.model} is NEVER stopping...")

def test():
    gtr = SuperCar(model='GT-R', year='2024', is_turbine=True)
    gtr.run()
    gtr.stop()
    gtr.drive_very_fast()

if __name__ == "__main__":
     test()