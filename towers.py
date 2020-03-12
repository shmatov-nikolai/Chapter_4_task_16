
class Castle_1():
    def __init__(self, name = "Замок Красного Лорда", id = "RED", units = 500, katapulta = 'Нет', level = 500):
        self.name = name
        self.id = id
        self.units = units
        self.katapulta = katapulta
        self.level = level
    def __str__(self):
        return f"{self.name} гарнизон: {self.units}, Наличие катапульты: {self.katapulta}"
    def katapulta_build(self):
        if self.units >= 1000:
            self.katapulta = 'Да' 
            print("Катапульта создана!!!")
        else:
            print(f"недостаточно солдат, вам нехватает {1000 - self.units} солдат")
    def update_soldat(self):
        if self.units < self.level:
            self.units += 25

class Castle_2():
    def __init__(self, name = "Замок Синего Лорда", id = "Blue", units = 500, katapulta = 0, level = 500):
        self.name = name
        self.id = id
        self.units = units
        self.katapulta = katapulta
        self.level = level
    def __str__(self):
        return f"{self.name} гарнизон: {self.units}, Наличие катапульты: {self.katapulta}"
    def katapulta_build(self):
        if self.units >= 1000:
            self.katapulta = 'Да'
            print("Катапульта создана!!!")
        else:
            print(f"недостаточно солдат, вам нехватает {1000 - self.units} солдат")
    def update_soldat(self):
        if self.units < self.level:
            self.units += 25

class Tower_1():
    def __init__(self, name = "Башня-1", id = 'Нейтральная', units =25, power = 25, level = 1):
        self.name = name
        self.id = id
        self.units = units
        self.power = power
        self.level = level
    
    def __str__(self):
        return f"Башня: {self.name}, уровень: {self.level}, состояние: {self.id}, гарнизон: {self.units} солдат"

    def update_soldat(self):
        if self.id != "Нейтральная":
            if self.units < self.power:
                self.units += 5
    
    def level_up_tower(self):
        self.level += 1
        self.power = self.level * 25
        print(f"Отлично, уровень Башни повышен, теперь она собирает до {self.units} солдат")


class Tower_2():
    def __init__(self, name = "Башня-2", id = 'Нейтральная', units =25, power = 25, level = 1):
        self.name = name
        self.id = id
        self.units = units
        self.power = power
        self.level = level
    
    def __str__(self):
        return f"Башня: {self.name}, уровень: {self.level}, состояние: {self.id}, гарнизон: {self.units} солдат"

    def update_soldat(self):
        if self.id != "Нейтральная":
            if self.units < self.power:
                self.units += 5
    
    def level_up_tower(self):
        self.level += 1
        self.power = self.level * 25
        print(f"Отлично, уровень Башни повышен, теперь она собирает до {self.units} солдат")
          


class Tower_3():
    def __init__(self, name = "Башня-3", id = 'Нейтральная', units =25, power = 25, level = 1):
        self.name = name
        self.id = id
        self.units = units
        self.power = power
        self.level = level
    
    def __str__(self):
        return f"Башня: {self.name}, уровень: {self.level}, состояние: {self.id}, гарнизон: {self.units} солдат"

    def update_soldat(self):
        if self.id != "Нейтральная":
            if self.units < self.power:
                self.units += 5
    
    def level_up_tower(self):
        self.level += 1
        self.power = self.level * 25
        print(f"Отлично, уровень Башни повышен, теперь она собирает до {self.units} солдат")



class Tower_4():
    def __init__(self, name = "Башня-4", id = 'Нейтральная', units =25, power = 25, level = 1):
        self.name = name
        self.id = id
        self.units = units
        self.power = power
        self.level = level
    
    def __str__(self):
        return f"Башня: {self.name}, уровень: {self.level}, состояние: {self.id}, гарнизон: {self.units} солдат"

    def update_soldat(self):
        if self.id != "Нейтральная":
            if self.units < self.power:
                self.units += 5
    
    def level_up_tower(self):
        self.level += 1
        self.power = self.level * 25
        print(f"Отлично, уровень Башни повышен, теперь она собирает до {self.units} солдат")
