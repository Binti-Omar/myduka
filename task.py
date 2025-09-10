class BankAccount:
    # constructor _init_
    def __init__(self,owner_name,account_number,balance):
        self.owner_name=owner_name
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
            self.balance+=amount
            print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self,amount):
            self.balance-=amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")

    def display_info(self):
            print(f"Owner Name: {self.owner_name}")
            print(f"Account Number: {self.account_number}")
            print(f"Balance: {self.balance}")

account1= BankAccount("Alice", "123456789", 1000)
account1.deposit(500)
account1.withdraw(200)  
account1.display_info() 


class Student:
    def __init__(self,student_id,name,email,course):
        self.student_id=student_id
        self.name=name
        self.email=email
        self.course=course

    def enroll_course(self,course):
        self.course=course
        print(f"Enrolled in course: {self.course}")

    def drop_course(self,course):
        self.course=course
        print(f"Dropped course: {self.course}")

    def set_grade(self,course,grade):
        self.grade=grade
        print(f"Set grade for {self.course}: {self.grade}")

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Courses: {self.course}")
        print(f"Grades: {self.grade}")

student1= Student("S123", "Bob", "bob.gmail.com","Math")
student1.enroll_course("Science")
student1.set_grade("Math", "A")
student1.display_info()

class Car:
    def __init__(self,brand,model,year,fuel_capacity):
          self.brand=brand
          self.model=model
          self.year=year
          self.fuel_capacity=fuel_capacity
          self.fuel_level=0
          self.is_running=False

    def start(self):
            if self.fuel_level>0:
                 self.is_running=True
                 print("Car has started")
            else:
                 print("Cannot start car because fuel level is zero.")

    def stop(self):
            self.is_running=False
            print("Car has stopped")

    def refuel(self,amount):
            if self.fuel_level + amount <= self.fuel_capacity:
                 self.fuel_level+=amount
                 print(f"Refueled: {amount}, New Fuel Level: {self.fuel_level}")
            else:
                 print("Cannot refuel beyond fuel capacity.")

    def drive(self,distance):
            if self.is_running and self.fuel_level>0:
                fuel_needed=distance*0.5
                if fuel_needed<=self.fuel_level:
                    self.fuel_level=fuel_needed
                    print(f"Drove: {distance} km, Fuel Consumed: {fuel_needed}, Remaining Fuel Level: {self.fuel_level}")
                else:
                    print("Not enough fuel to drive the distance.")
            else:
                print("Car is not running since the fuel level is zero.")
          
    def display_info(self):
            print(f"Brand: {self.brand}")
            print(f"Model: {self.model}")
            print(f"Year: {self.year}")
            print(f"Fuel Capacity: {self.fuel_capacity}")
            print(f"Fuel Level: {self.fuel_level}")
            print(f"Is Running: {self.is_running}")

my_car= Car("Toyota", "Corolla", 2020, 50)
my_car.refuel(30)
my_car.start()
my_car.drive(100)
my_car.stop()
my_car.display_info()


