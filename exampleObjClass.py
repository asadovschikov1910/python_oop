class Car:
    def __init__(self, model, year: str, color = "clear"):
        self.model = model
        self.year = year
        self.color = color

    def run(self):
        print(f"{self.model} is running...")

    def stop(self):
        print(f"{self.model} is stopped...")

def test():
    lada = Car('Lada', '2015', color='red')
    lada.run()
    lada.color = 'blue'
#gittest
    bmw = Car('BMW', 2020)
    bmw.run()

    audi = Car('Audi', '2023', color='green')
    audi.stop()

    print(lada.model)
    print(lada.year)

if __name__ == "__main__":
     test()