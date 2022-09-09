#lets calculate the speed distance and time using the object oriented python and first class functions
#https://favtutor.com/blogs/python-switch-case
#https://www.geeksforgeeks.org/passing-function-as-an-argument-in-python/
class CalculatorSwitch:

    def operation(self,selection):
        operations = {'1': "speed", '2':"distance",'3':"time"}
        try:
          self.selection = operations[selection]
          return getattr(self, self.selection)()
        except KeyError:
          print("invalid option")

    def speed(self):
        print("lets calculate speed")
        try:
            distance = input("enter the distance in miles ")
            time = input("enter time taken in hours ")
            print(int(distance) / int(time))
        except ValueError:
            print("invalid value")

    def distance(self):
        print("lets calculate distance")
        try:
            speed = input("enter the speed in miles/hr ")
            time = input("enter time taken in hours ")
            print(int(speed) * int(time))
        except ValueError:
            print("invalid value")



    def time(self):
        ("lets calculate time")
        try:
            distance = input("enter the distance in miles ")
            speed = input("enter the speed in miles/hr ")
            print(int(distance) / int(speed))
        except ValueError:
            print("invalid value")





selection = input("choose from the following options: 1.speed, 2.distance 3.time ")

calc = CalculatorSwitch()
calc.operation(selection)
