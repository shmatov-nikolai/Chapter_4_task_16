class Hero_1():
    def __init__(self, name = 'Red_Gamer', id_ = "RED",  power = 50, level = 1, units = 50, special_points = 50):
        self.name = name
        self.id_ = "RED"
        self.units = units
        self.level = 1
        self.power = power
        self.special_points = special_points
    def __str__(self):
        return f'Герой {self.name}, уровень: {self.level} - сила героя {self.power} , количество солдат {self.units}'
    
    def change_level(self):
        if self.units >= 200:
            self.units -= 200
            self.level +=1
            self.power = 50 * self.level
            self.special_points = self.power
            print(f'Герой {self.name} повысил уровень, сила героя: {self.power}, текущий уровень: {self.level}')
        else:
            print(f"Для повышения уровня героя необходимо иметь 200 солдат, вам нехватает {200 - self.units} солдат")
            
    
    def use_superpower(self):
        if self.special_points != 50*self.level:
            print("Недостаточно силы")
        else:
            self.units += self.special_points
            self.special_points = 0
            
            print(f"Супер сила активированна, теперь у вас {self.units} солдат")



class Hero_2():
    def __init__(self, name = 'Blue_Gamer', id_ = "Blue", power = 50, level = 1, units = 50, special_points = 50 ):
        self.name = name
        self.id_ = "Blue"
        self.units = units
        self.level = 1
        self.power = power
        self.special_points = special_points
        
    def __str__(self):
        return f'Герой {self.name}, уровень: {self.level} - сила героя {self.power} , количество солдат {self.units}'
    
    def change_level(self):
        if self.units >= 200:
            self.units -= 200
            self.level +=1
            self.power = 50 * self.level
            self.special_points = self.power
            print(f'Герой {self.name} повысил уровень, сила героя: {self.power}, текущий уровень: {self.level}')
        else:
            print(f"Для повышения уровня героя необходимо иметь 200 солдат, вам нехватает {200 - self.units} солдат")
    
    def use_superpower(self):
        if self.special_points != 50*self.level:
            print("Недостаточно силы")
        else:
            self.units += self.special_points
            self.special_points = 0
            
            print(f"Супер сила активированна, теперь у вас {self.units} солдат")
