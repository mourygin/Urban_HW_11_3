
class my_class():
    def __init__(self):
        # super.__init__()
        pass
class Figure:
    def __init__(self, color, *sides):
        self.sides_count = len(sides)
        filled = False
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled
    def get_color(self):
        return self.__color
    def __is_valid_color(color):
        result = True
        if color[0] not in range(0,256):
            result = False
        if color[1] not in range(0,256):
            result = False
        if color[2] not in range(0,256):
            result = False
        return result
    def set_color(self, color):
        if Figure.__is_valid_color(color):
            self.__color = list(color)
        return
    def __is_valid_sides(self, *args):
        result = True
        for i in range(0, len(args[0])):
            if args[0][i] <= 0 or (not isinstance(args[0][i],int)):
                result = False
        if len(args[0]) != self.sides_count:
            result = False
        return result
    def get_sides(self):
        return self.__sides
    def __len__(self):
        result = 0
        for i in self.__sides:
            result += i
        return result
    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(new_sides):
            for i in range(0,self.sides_count):
                self.__sides[i] = new_sides[i]
            return
    def get_var_name(self):
        for k, v in globals().items():
            if v is self:
                return k
    def about(self):
        print('-----------------')
        print('Object name:', self.get_var_name())
        print('Object type:', type(self))
        print('Edges:', self.sides_count)
        print('Edges lenth:', self.get_sides())
        print('Edges sum lenth (perimeter):', self.__len__())
        print('Color (RGB):', self.get_color())
        print('Is filled:', self.filled == True)
        if isinstance(self,Circle):
            print('Radius:', self.get_radius())
            print('Object sum area:', self.__len__() * self.__len__() / 4 / 3.1415)
        elif isinstance(self,Triangle):
            print('Object height =', self.get_height())
            print('Object sum area:', self.get_square())
        elif isinstance(self,Cube):
            print('Object volume =', self.sides_count)
            print('Object surface area:', self.sides_count)
        else:
            pass
        print('-----------------')
class Circle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = list(sides)
        sl = []
        sl.append(self.__sides[0])#[0])
        self.__sides = sl
        self._Figure__sides = sl
        self.sides_count = 1
        self.__color = list(color)
        super().get_color()
        super().set_color(color)
        super().get_sides()
        self.__radius = self.__len__()/2/3.1415
    def get_radius(self):
        return self.__radius
    def get_square(self):
        return self.__len__() * self.__len__() / 4 / 3.1415
class PreVehicle():
    pass
class Vehicle(PreVehicle):
    def __init__(self):
        vehicle_type = "none"
class Mashina():
    pass
class Car():
    def __init__(self, power):
        self.price = 1_000_000
        self.power = power

    def get_horse_powers(self):
        return self.power
class Nissan(Vehicle, Car, Mashina):
    def __init__(self, power, vehicle_type, price):
        Car.__init__(self, power)
        self.vehicle_type = vehicle_type
        self.price = price

    def horse_powers(self):
        super().powers(self)
