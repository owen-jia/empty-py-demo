
class Company:
    def __init__(self, name="", address="", count=0):
        self.name = name
        self.address = address
        self.count = count

    def info(self):
        print(f"Company,name:{self.name},address:{self.address},persons:{self.count}")

