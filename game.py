#unit info
class units:
    def __init__(self, wood_cost, food_cost, gold_cost):
        self.wood_cost = wood_cost
        self.food_cost = food_cost
        self.gold_cost = gold_cost

class spearman(units):
    def __init__(self):
        self.wood_cost = 1
        self.food_cost = 1
        self.gold_cost = 0

class archer(units):
    def __init__(self):
        self.wood_cost = 1
        self.food_cost = 0
        self.gold_cost = 1

class knight(units):
    def __init__(self):
        self.wood_cost = 0
        self.food_cost = 1
        self.gold_cost = 1

class scout(units):
    def __init__(self):
        self.wood_cost = 1
        self.food_cost = 1
        self.gold_cost = 1

#game info
class little_battle:
    def __init__(self):
        self.map = [["  "]*cols for i in range(rows)]

        self.current_turn = "Player 1"

    def print_map(self):
        #opeining text
        print("Please check the battlefield, commander.")

        #label for the x-axis
        print("  X",end='')
        for k in range(rows-1):
            print("0{} ".format(k),end='')
        print("0{}".format(k+1),end='')
        print("X")

        #printing upper rim
        print(" Y+--",end='')
        for k in range(rows-2):
            print("---", end='')
        print("---+",end='')

        #printing each row
        for i in range(cols):
            print()
            print("0{}|".format(i),end='')
            for j in range(rows):
                print("{}|".format(self.map[j][i]),end='')
        print()
        
        #printing lower rim
        print(" Y+--",end='')
        for k in range(rows-2):
            print("---", end='')
        print("---+")
        

    def print_prices(self):
        print("  Spearman (S) - 1W, 1F")
        print("  Archer (A) - 1W, 1G")
        print("  Knight (K) - 1F, 1G")
        print("  Scout (T) - 1W, 1F, 1G")

class home_base:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#player info
class player:
    def __init__(self, wood, food, gold, player_number):
        self.wood = wood
        self.food = food
        self.gold = gold
        self.army = []
        self.player_number = player_number

    def print_resource(self):
        print("[Your Asset: Wood - {} Food - {} Gold - {}]".format(self.wood,self.food,self.gold))
        print()

    def check_resource(self):
        if self.wood>0 and self.food>0 and self.gold>0:
            return True
        else:
            print("No resources to recruit any armies.")
            return False

    def purchase_unit(self):
        while True:
            unit = input("Which type of army to recruit, (enter) ‘S’, ‘A’, ‘K’, or ‘T’? Enter ‘NO’ to end this stage.\n")
            #buying a spearman
            if unit == "S":
                self.wood = self.wood - spearman.wood_cost
                self.food = self.food - spearman.food_cost
                self.gold = self.gold - spearman.gold_cost
                print()
                return 'S'

            #buying an archer
            elif unit == "A":
                self.wood = self.wood - archer.wood_cost
                self.food = self.food - archer.food_cost
                self.gold = self.gold - archer.gold_cost
                print()
                return 'A'

            #buying a knight
            elif unit == "K":
                self.wood = self.wood - knight.wood_cost
                self.food = self.food - knight.food_cost
                self.gold = self.gold - knight.gold_cost
                print()
                return 'K'

            #buying a scout
            elif unit == "T":
                self.wood = self.wood - scout.wood_cost
                self.food = self.food - scout.food_cost
                self.gold = self.gold - scout.gold_cost
                print()
                return 'T'

            #skip buying 
            elif unit == "NO":
                print()
                return

            #user asks to display map
            elif unit == "DIS":
                game.print_map()
                print()

            #user asks to check prices
            elif unit == "PRIS":
                game.print_prices()
                print()

            #quitting the game
            elif unit == "QUIT":
                exit()

            #invalid inputs
            else:
                print("Sorry, invalid input. Try again.")
                print()

    def resolve_unit_name(self):
        if unit == 'S':
            return 'Spearman'
        elif unit == 'A':
            return 'Archer'
        elif unit == 'K':
            return 'Knight'
        elif unit == 'T':
            return 'Scout'

    def unit_placement(self):
        while True:
            placement_coords = input("You want to recruit a {}. Enter two integers as format ‘x y’ to place your army.\n".format(unit_name)).split(" ")

            if placement_coords == 'DIS':
                game.print_map

            elif placement_coords == 'PRIS':
                game.print_prices

            else:
                #checking for appropriate length
                if len(placement_coords) != 2:
                    print("Sorry, invalid input. Try again.")
                    print()
                else:
                    placement_coords[0],placement_coords[1] = int(placement_coords[0]), int(placement_coords[1])

                    #checking if on top of home base
                    if placement_coords[0] == 1 and placement_coords[1] == 1:
                        print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
                        print()

                    else:
                        #checking if around home base
                        if placement_coords[0] == 1 and placement_coords[1] == 0 or placement_coords[0] == 2 and placement_coords[1] == 1 or placement_coords[0] == 1 and placement_coords[1] == 2 or placement_coords[0] == 0 and placement_coords[1] == 1:
                            game.map[placement_coords[0]][placement_coords[1]] = "{}{}".format(unit,self.player_number)
                            break
                        else:
                            print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
                            print()

    def home_sweep(self):
        if self.player_number == 1:
            if game.map[1][0] == "  " or game.map[2][1] == "  " or game.map[1][2] == "  " or game.map[0][1] == "  ":
                return True
            else:
                print("No place to recruit new armies.")
                return False



#initialize game
cols, rows = (10,10)
end = False
game = little_battle()
unit = ''
unit_name = ''

game.map[1][1] = "H1"
home_1 = [1],[1]

game.map[rows-2][cols-2] = "H2"
home_2 = [rows-2],[cols-2]


#initialize units
spearman = spearman()
archer = archer()
knight = knight()
scout = scout()

#initialize players
player1 = player(10,10,10,1)

#running the game
#opening
print("Game Started: Little Battle! (enter QUIT to quit the game)")
print()
print(home_2)

game.print_map()
print("(enter DIS to display the map)")
print()

game.print_prices()
print("(enter PRIS to display the price list)")
print()

player1.print_resource()

while player1.check_resource() == True:
    if player1.home_sweep() == True:

        unit = player1.purchase_unit()
        if unit == None:
            break
        else:
            unit_name = player1.resolve_unit_name()
            player1.unit_placement()

            print("You has recruited {}.".format(unit))
            print()

            player1.print_resource()

        game.print_map()
        print()

    else:
        break

game.print_map()

print('END OF CODE')


