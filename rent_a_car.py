from ast import While
from pickle import PERSID


class Rent():
    def __init__(self,cars) -> None:
        self.cars = cars

    def have_license(self):
        license = input("Do You Have License [y/n] : ")
        while license not in ["y","n"]:
            print("Wrong enter try again [y,n] : ",end="")
            license = input()

        if license == "y":
            return True
        else:
            return False

    def rent_period(self):
        global period
        while True:
            try:
                print("How many days will you rent : ",end="")
                period = int(input())
                while period < 0:
                    print("Wrong enter try again : ", end="")
                    period = int(input())
                break
            except ValueError:
                print("Not an integer") 
                continue

        return period



    def fee(self):
        global fee
        global choose
        print("-----Car List-----")
        print(self.cars)
        print("Choose a car [enter car number] : ",end="")
        choose =input()
        while True:
            if choose not in self.cars.keys():
                print("Wrong enter try again : " , end="")
                choose = input()
                continue
            else:
                break

        fee = period * self.cars[choose][4]

        return fee

    def main(self):
        global period
        global fee
        if self.have_license():
            self.rent_period()
            self.fee()
            return (f"You rented {self.cars[choose][0]} {self.cars[choose][1]} for {period} days and {fee} $")
        else:
            return ("You don't have license , can't rent.")

cars = {
	"1":["honda","S2000",2000,15000,150], #model #release #km #rent fee per a day
	"2":["opel","insignia",2017,32541,225],
	"3":["bmw","x4",2018,12124,325]
}

r = Rent(cars)
print(r.main())