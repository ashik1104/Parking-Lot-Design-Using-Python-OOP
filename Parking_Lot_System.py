class Car:
    def __init__(self, license_number, model, color):
        self.license = license_number
        self.model = model
        self.color = color

    def __repr__(self):
        return f'{self.license} {self.model} {self.color}'


class Garage:
    def __init__(self):
        self.car_added = []
        self.spots = 10
        self.car_info = {'Tickets': [], 'License': [], 'Model': [], 'Color': []}
        self.ticket = []
        self.available_spot = ['a1', 'b1', 'c1', 'd1', 'e1', 'a2', 'b2', 'c2', 'd2', 'e2']
        self.income = 0

    def See_available_spot(self):
        print('                                           Available Spot')
        print('                                        ------------------')
        print("                      ", self.available_spot)
        print('                      --------------------------------------------------------------', '\n\n')

    def add_car_to_garage(self, car, spot_name):
        if spot_name in self.available_spot:
            user_data = str(car).split(' ')
            # print(user_data)
            self.spots -= 1
            self.car_added.append(user_data)
            ticket = spot_name + user_data[0]
            self.car_info['Tickets'].append(ticket)
            self.car_info['License'].append(user_data[0])
            self.car_info['Model'].append(user_data[1])
            self.car_info['Color'].append(user_data[2])
            print(f'Successfully parked!!! Your ticket : {ticket}')
            self.available_spot.remove(spot_name)
        else:
            print('Spot is not available')

    def depart(self, ticket, hours):
        if ticket not in self.car_info['Tickets']:
            print('No car found')
        else:
            for i, val in enumerate(self.car_info['Tickets']):
                if val == ticket:
                    self.car_info['License'].pop(i)
                    self.car_info['Model'].pop(i)
                    self.car_info['Color'].pop(i)
                    self.car_info['Tickets'].pop(i)
                    print('Car removed successfully from the garage')
            for i, data in enumerate(self.car_added):
                if data[0] == ticket[2:]:
                    self.car_added.pop(i)

            if hours > 30:
                print(f'Bill : ${hours * 5 + 100}')
                self.income += hours * 5 + 100
            else:
                print(f'Bill : ${hours * 5}')
                self.income += hours * 5
            self.available_spot.append(ticket[0:2])
            self.available_spot.sort()
            self.spots += 1


My_garage = Garage()

print('          *****************************WELCOME TO OUR PARKING SYSTEM***************************')
print('                                   ------------------------------------')

while True:
    print('Options : ')
    print('1. Available spot.')
    print('2. Park your car.')
    print('3. Depart your car.')
    print('4. Total car in the garage.')
    print('5. Total income.')

    choice = int(input('Give choice : '))

    if choice == 1:
        My_garage.See_available_spot()
    elif choice == 2:
        car_license = input('Enter license number : ')
        car_model = input('Enter model number : ')
        car_color = input('Enter color of the car : ')
        Spot_name = input('Enter spot name : ')
        user_car = Car(car_license, car_model, car_color)
        My_garage.add_car_to_garage(user_car, Spot_name)
        print()
    elif choice == 3:
        Ticket = input('Enter your ticket : ')
        Hours = int(input('Enter time duration(in hour) : '))
        My_garage.depart(Ticket, Hours)
        print()
    elif choice == 4:
        print(f'Cars in the garage : {My_garage.car_added}')
        print()
    elif choice == 5:
        print(f'Total income : {My_garage.income}')
        print()
    else:
        print('Please enter correct choice or go to the hell...')
        print()
