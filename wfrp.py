players = {}


class PlayerInv(object):

    def __init__(self, name, gold, silver, penny):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.penny = penny
        self.inv = {
                    "gold":gold,
                    "silver":silver,
                    "penny":penny
                    }

    def subtract_money(self, gold, silver, penny):
        sub_total = gold*240 + silver*20 + penny #in wfrp 1g = 12s and 1s = 20p
        inv_total = (self.inv["gold"]*240 + self.inv["silver"]*20
                     + self.inv["penny"])

        new_total = inv_total - sub_total

        if new_total <= 0:
            new_total = 0
        else:
            new_gold, sub_silver = divmod(new_total, 240)
            new_silver, new_penny = divmod(sub_silver, 20)
            self.inv = {
                        "gold":new_gold,
                        "silver":new_silver,
                        "penny":new_penny
                        }

def add_inventory():
    print "Please type in the player's name and how much money he has.\n"

    p_name = raw_input("Please type in the player's name.\n")
    
    while True:
        p_gold = raw_input("How much gold does %s have?\n" % p_name)
        try:
            p_gold = int(p_gold)
            break
        except ValueError:
            print "Incorrect input. Please input a number."
    
    while True:
        p_silver = raw_input("How much silver does %s have?\n" % p_name)
        try:
            p_silver = int(p_silver)
            break
        except ValueError:
            print "Incorrect input. Please input a number."

    while True:
        p_penny = raw_input("How mmany pennies does %s have?\n" % p_name)
        try:
            p_penny = int(p_penny)
            break
        except ValueError:
            print "Incorrect input. Please input a number."

    new_player = PlayerInv(p_name, p_gold, p_silver, p_penny)
    players[p_name] = new_player

def check_inventory():
    print "Type the name of a player you wish to check."

    while True:
        p_name = raw_input("> ")

        if p_name in players:
            print "Here's %s's inventory." % p_name                
            print players[p_name].inv 
            break
        else:
            print "No player named %s found. Returning to main menu." % p_name
            break
        
def del_inventory():
    print "Type the name of a player you wish to remove."

    while True:
        p_name = raw_input("> ")

        if p_name in players:
            print "You're about to remove %s from database." % p_name
            print "Are you sure?\n"
            print "y/n"

            answer = raw_input("> ")
            if answer is 'y':
                print "Removing %s. Goodbye!" % p_name
                players.pop(p_name, None)
                break
            else:
                print "Ok. Returning to main menu."
                break
        else:
            print "No player named %s found. Returning to main menu." % p_name
            break

def modify_inv():
    print "Type in the name of the player you wish to modify."

    while True:
        p_name = raw_input("> ")

        if p_name in players:
            print players[p_name].inv
            print "How much gold do you want to remove?"
            in_gold = int(raw_input("> "))
            print "How much silver do you want to remove?"
            in_silver = int(raw_input("> "))
            print "How many pennies do you want to remove?"
            in_penny = int(raw_input("> "))

            p_inv = players.get(p_name)

            if p_inv:
                p_inv.subtract_money(in_gold, in_silver, in_penny)
                break
 
        else:
            print "No player named %s found. Returning to main menu." % p_name
            break


menu_options = {
                '1':add_inventory,
                '2':check_inventory,
                '3':del_inventory,
                '4':modify_inv
                }


def menu():

    print "Hello, traveler. What would you like to do?\n"
    print "1. Add new inventory."
    print "2. Check existing inventory."
    print "3. Remove inventory."
    print "4. Modify existing inventory."
    print "5. Exit."

    while True:

        answer = raw_input("> ")
        run = menu_options.get(answer)

        if run:
            run()
        elif answer is '5':
            break
            exit(0)
        else:
            print "Incorrect input. Please try again."


menu()