class Character:
    def __init__(self, name="Link", health=1000):
        self.name = name
        self.health = health

    def attack(self):
        pass


class Hero(Character):
    def __init__(self, name, health=1000, weapon="gun"):
        super().__init__(name, health)
        self.weapon=weapon

    def attack(self):
        print(self.name+" атаковал врага с помощью "+self.weapon)


class Enemy(Character):
    def __init__(self, health, name, damage=-150):
        super().__init__(name, health)
        self.damage=damage


    def attack(self):
        print(self.name+" получил урон "+str(self.damage))




hero = Hero ("Гир", 1000, "автомат")
enemy = Enemy (500, "Веб", -150)

hero.attack()
enemy.attack()