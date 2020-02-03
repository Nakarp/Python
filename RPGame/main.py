from classes.game import Person
from classes.bcolors import bcolors
from classes.magic import Spell
from  classes.inventory import Item

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")


# Create some Item:
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores MP/HP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's MP/HP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "cuantity": 15}, {"item": hipotion, "cuantity": 5}, {"item": superpotion, "cuantity": 5},
                {"item": elixer, "cuantity": 5}, {"item": hielixer, "cuantity": 2}, {"item": grenade, "cuantity": 5}]

# Instantiate People
player1 = Person("Papa:", 450, 65, 60, 34, player_spells, player_items)
player2 = Person("YO:  ", 450, 65, 60, 34, player_spells, player_items)      #name, hp, mp, atk, df, magic, inventory
player3 = Person("Otro:", 450, 65, 60, 34, player_spells, player_items)
enemy = Person("Enemy:", 1200, 65, 45, 25,[] , [])                           #name, hp, mp, atk, df, inventory

players = [player1, player2, player3]

running = True
i = 0

print(bcolors.RED1 + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("===============")

    print("\n\n")
    print("NAME                     HP                                  MP")
    for player in players:
        player.get_stats()

    for player in players:

        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) -1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attack for", dmg, "points of damage.")

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.YELLOW1 + "\nNot Enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.BLUE1 + "\n" + spell.name + " heals for", str(magic_dmg), "HP" + bcolors.ENDC)
            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print(bcolors.BLUE1 + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice =  int(input("    Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["cuantity"] == 0:
                print(bcolors.RED1 + "\n" + "None left..." + bcolors.ENDC)
                continue

            player.items[item_choice]["cuantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.GREEN + "\n" + item.name, "heals from", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.GREEN + "\n" + item.name + "fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.RED1 + "\n" + item.name, "deals", str(item.prop), "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("-------------------------")
    print("Enemy HP:" + bcolors.RED1 + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.GREEN + bcolors.BOLD + "You win!!" + bcolors.ENDC)
        running = 0
    elif player.get_hp() == 0:
        print(bcolors.RED2 + bcolors.BOLD + "Your enemy defeated you!!" + bcolors.ENDC)
        running = 0

