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
        print("Recruit Prices:")
        print("  Spearman (S) - 1W, 1F")
        print("  Archer (A) - 1W, 1G")
        print("  Knight (K) - 1F, 1G")
        print("  Scout (T) - 1W, 1F, 1G")

    def print_year(self):
        print("-Year {}-".format(year+1))
        print()

#player info
class player:
    def __init__(self, wood, food, gold, player_number):
        self.wood = wood
        self.food = food
        self.gold = gold
        self.army = []
        self.spearman = []
        self.archer = []
        self.knight = []
        self.scout = []
        self.player_number = player_number
        self.home_position = home_bases[self.player_number-1]

    def print_resource(self):
        print("[Your Asset: Wood - {} Food - {} Gold - {}]".format(self.wood,self.food,self.gold))
        print()

    def print_recruit_turn(self):
        print("+++Player {}'s Stage: Recruit Armies+++".format(self.player_number))
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
            placement_coords = input("You want to recruit a {}. Enter two integers as format ‘x y’ to place your army.\n".format(unit_name))

            if placement_coords == 'DIS':
                game.print_map()
                print()
            elif placement_coords == 'PRIS':
                game.print_prices()
                print()
            elif placement_coords == 'QUIT':
                exit()
            else:
                placement_coords = placement_coords.split(' ')
                #checking for appropriate length
                if len(placement_coords) != 2:
                    print("Sorry, invalid input. Try again.")
                    print()
                else:
                    if placement_coords[0].isnumeric() == False or placement_coords[1].isnumeric() == False:
                        print("Sorry, invalid input. Try again.")
                        print()
                    else:
                        placement_coords[0],placement_coords[1] = int(placement_coords[0]), int(placement_coords[1])

                        #checking if on top of home base
                        if placement_coords[0] == self.home_position[0] and placement_coords[1] == self.home_position[1]:
                            print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
                            print()
                        elif game.map[placement_coords[0]][placement_coords[1]] != '  ':
                            print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
                            print()
                        else:
                            #checking if around home base
                            if placement_coords[0] == self.home_position[0] and placement_coords[1] == self.home_position[1]-1 or placement_coords[0] == self.home_position[0] and placement_coords[1] == self.home_position[1]+1 or placement_coords[0] == self.home_position[0]-1 and placement_coords[1] == self.home_position[1] or placement_coords[0] == self.home_position[0]+1 and placement_coords[1] == self.home_position[1]:
                                game.map[placement_coords[0]][placement_coords[1]] = "{}{}".format(unit,self.player_number)
                                self.army.append(unit)
                                if unit == 'S':
                                    self.spearman.append((placement_coords[0],placement_coords[1]))
                                elif unit == 'A':
                                    self.archer.append((placement_coords[0],placement_coords[1]))
                                elif unit == 'K':
                                    self.knight.append((placement_coords[0],placement_coords[1]))
                                elif unit == 'T':
                                    self.scout.append((placement_coords[0],placement_coords[1]))
                                break
                            else:
                                print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
                                print()

    def home_sweep(self):
        if game.map[self.home_position[0]][self.home_position[1]-1] == "  " or game.map[self.home_position[0]][self.home_position[1]+1] == "  " or game.map[self.home_position[0]-1][self.home_position[1]] == "  " or game.map[self.home_position[0]+1][self.home_position[1]] == "  ":
            return True
        else:
            print("No place to recruit new armies.")
            print()
            return False

    def print_army_to_move(self):
        print("Armies to Move:")

        army_reducable = []
        [army_reducable.append(x) for x in self.army if x not in army_reducable]

        for j in range(len(army_reducable)):
            if army_reducable[j] == 'S':
                print("  Spearman:",end='')
                for i in range(len(self.spearman)-1):
                    print(' {},'.format(self.spearman[i]),end='')
                print(' {}'.format(self.spearman[-1]))
            elif army_reducable[j] == 'A':
                print("  Archer:",end='')
                for i in range(len(self.archer)-1):
                    print(' {},'.format(self.archer[i]),end='')
                print(' {}'.format(self.archer[-1]))                   
            elif army_reducable[j] == 'K':
                print("  Knight:",end='')
                for i in range(len(self.knight)-1):
                    print(' {},'.format(self.knight[i]),end='')
                print(' {}'.format(self.knight[-1]))
            elif army_reducable[j] == 'S':
                print("  Scout:",end='')
                for i in range(len(self.scout)-1):
                    print(' {},'.format(self.scout[i]),end='')
                print(' {}'.format(self.scout[-1]))

        
                





#initialize game
cols, rows = (10,10)
end = False
game = little_battle()
unit = ''
unit_name = ''

game.map[1][1] = "H1"
home_1 = 1,1

game.map[rows-2][cols-2] = "H2"
home_2 = rows-2,cols-2

home_bases = [home_1,home_2]

year = 616

#initialize units
spearman = spearman()
archer = archer()
knight = knight()
scout = scout()

#initialize players
player1 = player(10,10,10,1)
player2 = player(10,10,10,2)

#running the game
#opening
print("Game Started: Little Battle! (enter QUIT to quit the game)")
print()
print(player2.home_position)

game.print_map()
print("(enter DIS to display the map)")
print()

game.print_prices()
print("(enter PRIS to display the price list)")
print()

game.print_year()

player1.print_recruit_turn()
player1.print_resource()

while player1.check_resource() == True:
    if player1.home_sweep() == True:

        unit = player1.purchase_unit()
        if unit == None:
            break
        else:
            unit_name = player1.resolve_unit_name()
            player1.unit_placement()

            print()
            print("You has recruited a {}.".format(unit_name))
            print()

            player1.print_resource()

        game.print_map()
        print()

    else:
        break
player1.print_army_to_move()

print(player1.army)
print(set(player1.army))
print('END OF CODE')


