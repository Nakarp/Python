import random
from classes.bcolors import bcolors


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
        self.hp -= dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + "    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.BLUE1 + bcolors.BOLD + "    Actions" + bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("----------------")
        print("\n" + bcolors.PINK + bcolors.BOLD + "    Magic" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.GREEN + bcolors.BOLD + "    ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("         " + str(i) + ".", item["item"].name, ":", item["item"].description, " (x" + str(item["cuantity"]) +")")
            i += 1

    def get_stats(self):
        print("                        _________________________            __________")
        print(bcolors.BOLD + self.name + "          " + bcolors.ENDC + str(self.hp) +"/" + str(self.maxhp) + " |" + bcolors.GREEN +
              "██████████               " + bcolors.ENDC + "|   " + str(self.mp) + " /" + str(self.maxmp) + " |" + bcolors.BLUE1 +
              "██████████" + bcolors.ENDC + "|")