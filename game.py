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
        self.player_number_input = player_number
        self.army = player_armies[self.player_number_input-1]
        self.spearman = player_spearmans[self.player_number_input-1]
        self.archer = player_archers[self.player_number_input-1]
        self.knight = player_knights[self.player_number_input-1]
        self.scout = player_scouts[self.player_number_input-1]
        self.player_number = players[self.player_number_input-1]
        self.home_position = home_bases[self.player_number_input-1]

    def print_resource(self):
        print("[Your Asset: Wood - {} Food - {} Gold - {}]".format(self.wood,self.food,self.gold))

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
            print()
            unit = input("Which type of army to recruit, (enter) ‘S’, ‘A’, ‘K’, or ‘T’? Enter ‘NO’ to end this stage.\n")

            #buying a spearman
            if unit == "S":
                self.wood = self.wood - spearman.wood_cost
                self.food = self.food - spearman.food_cost
                self.gold = self.gold - spearman.gold_cost
                return 'S'
            #buying an archer
            elif unit == "A":
                self.wood = self.wood - archer.wood_cost
                self.food = self.food - archer.food_cost
                self.gold = self.gold - archer.gold_cost
                return 'A'
            #buying a knight
            elif unit == "K":
                self.wood = self.wood - knight.wood_cost
                self.food = self.food - knight.food_cost
                self.gold = self.gold - knight.gold_cost
                return 'K'
            #buying a scout
            elif unit == "T":
                self.wood = self.wood - scout.wood_cost
                self.food = self.food - scout.food_cost
                self.gold = self.gold - scout.gold_cost
                return 'T'
            #skip buying 
            elif unit == "NO":
                return
            #user asks to display map
            elif unit == "DIS":
                game.print_map()
            #user asks to check prices
            elif unit == "PRIS":
                game.print_prices()
            #quitting the game
            elif unit == "QUIT":
                exit()
            #invalid inputs
            else:
                print("Sorry, invalid input. Try again.")

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
            print()
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
                else:
                    #checking for integers
                    if placement_coords[0].isnumeric() == False or placement_coords[1].isnumeric() == False:
                        print("Sorry, invalid input. Try again.")
                    else:
                        placement_coords[0],placement_coords[1] = int(placement_coords[0]), int(placement_coords[1])

                        #checking if on top of home base and if in bounds
                        if placement_coords[0] == self.home_position[0] and placement_coords[1] == self.home_position[1] or placement_coords[0] not in range(rows) or placement_coords[1] not in range(cols):
                            print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
                        elif game.map[placement_coords[0]][placement_coords[1]] != '  ':
                            print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
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

    def home_sweep(self):
        #checking if one of 4 positions around home base are empty
        if game.map[self.home_position[0]][self.home_position[1]-1] == "  " or game.map[self.home_position[0]][self.home_position[1]+1] == "  " or game.map[self.home_position[0]-1][self.home_position[1]] == "  " or game.map[self.home_position[0]+1][self.home_position[1]] == "  ":
            return True
        else:
            print("No place to recruit new armies.")
            return False

    def print_army_to_move(self):
        print("Armies to Move:")

        if 'S' in self.army:
            print("  Spearman:",end='')
            for i in range(len(self.spearman)-1):
                print(' {},'.format(self.spearman[i]),end='')
            print(' {}'.format(self.spearman[-1]))

        if 'A' in self.army:
            print("  Archer:",end='')
            for i in range(len(self.archer)-1):
                print(' {},'.format(self.archer[i]),end='')
            print(' {}'.format(self.archer[-1]))   
   
        if 'K' in self.army:
            print("  Knight:",end='')
            for i in range(len(self.knight)-1):
                print(' {},'.format(self.knight[i]),end='')
            print(' {}'.format(self.knight[-1]))            

        if 'T' in self.army:
            print("  Scout:",end='')
            for i in range(len(self.scout)-1):
                print(' {},'.format(self.scout[i]),end='')
            print(' {}'.format(self.scout[-1]))

        print()

    def print_move_turn(self):
        print()
        print("===Player {}'s Stage: Move Armies===".format(self.player_number))
        print()

    def check_armies(self):
        if len(self.army) != 0:
            return True
        else:
            print("No Army to Move: next turn.")
            print()
            return False

    def unit_movement_input(self):
        while True:
            print()
            movement_input = input("Enter four integers as a format ‘x0 y0 x1 y1’ to represent move unit from (x0, y0) to (x1, y1) or ‘NO’ to end this turn.\n")
            if movement_input == 'NO':
                return
            elif movement_input == 'DIS':
                game.print_map()
                print()
            elif movement_input == 'PRIS':
                game.print_prices()
                print()
            elif movement_input == 'QUIT':
                exit()
            else:
                movement_input = movement_input.split(' ')
                #checking if length is 4
                if len(movement_input) != 4:
                    print("Invalid move. Try again.")
                else:
                    #checking for integers
                    if movement_input[0].isnumeric() == False or movement_input[1].isnumeric() == False or movement_input[2].isnumeric() == False or movement_input[3].isnumeric() == False:
                        print("Invalid move. Try again.")
                    else:
                        movement_input[0],movement_input[1],movement_input[2],movement_input[3] = int(movement_input[0]),int(movement_input[1]),int(movement_input[2]),int(movement_input[3])
                        #checking if in bounds
                        if movement_input[0] not in range(rows) or movement_input[1] not in range(cols) or movement_input[2] not in range(rows) or movement_input[3] not in range(cols):
                            print("Invalid. Try again.")
                        else:
                            current_coords = (movement_input[0],movement_input[1])
                            desired_coords = (movement_input[2],movement_input[3])
                            if current_coords in self.scout:
                                if desired_coords[0] == current_coords[0]+2 or desired_coords[0] == current_coords[0]-2 or desired_coords[1] == current_coords[1]+2 or desired_coords[1] == current_coords[1]-2:
                                    print("pass")
                                    break
                                else:
                                    print("NOT AD, TRY AGAIN")
                            else:
                                if desired_coords[0] == current_coords[0]+1 and desired_coords[1] == current_coords[1] or desired_coords[0] == current_coords[0]-1 and desired_coords[1] == current_coords[1] or desired_coords[0] == current_coords[0] and desired_coords[1] == current_coords[1]+1 or desired_coords[0] == current_coords[0] and desired_coords[1] == current_coords[1]-1:
                                    return (current_coords,desired_coords)
                                else:
                                    print("NOT AD, Try again")
    
    def spearman_output(self):
        index = self.spearman.index(current_coords)
        del self.spearman[index]
        game.map[current_coords[0]][current_coords[1]] = '  '
        game.map[desired_coords[0]][desired_coords[1]] = 'S{}'.format(self.player_number)
        self.spearman.insert(index, desired_coords)        
        
    def unit_movement_output_general(self):
        tile = game.map[desired_coords[0]][desired_coords[1]]
        if tile == '~~':
            print("lost the army <Spearman/Archer/Knight/Scout> due to your command!")
        elif tile == 'GG':
            self.gold += 2
            print("Good. We collected 2 Gold")
        elif tile == 'FF':
            self.food += 2
            print("Good. We collected 2 Food")
        elif tile == 'WW':
            self.wood += 2
            print("Good. We collected 2 Wood")
        else:
            if current_coords in self.spearman:
                opponent = players[self.player_number-1]
                if 'K' in tile:
                    #removing the knight from opponent's army
                    knight_list = player_knights[opponent]
                    knight_list.remove(desired_coords)
                    army_list = player_armies[opponent]
                    del army_list[0]
                    #put the spearman on the board
                    self.spearman_output()
                else:
                    self.spearman_output()

def player1_recruit_units():
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

                print("You has recruited a {}.".format(unit_name))
                print()

                player1.print_resource()

            game.print_map()

        else:
            break

def player2_recruit_units():
    player2.print_recruit_turn()
    player2.print_resource()

    while player2.check_resource() == True:
        if player2.home_sweep() == True:

            unit = player1.purchase_unit()
            if unit == None:
                break
            else:
                unit_name = player2.resolve_unit_name()
                player2.unit_placement()

                print("You has recruited a {}.".format(unit_name))
                print()

                player2.print_resource()

            game.print_map()

        else:
            break







#initialize game
cols, rows = (5,5)
end = False
game = little_battle()
unit = ''
unit_name = ''
current_coords = 0,0
desired_coords = 0,0

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
players = [1,2]

player1_army = []
player1_spearman = []
player1_archer = []
player1_knight = []
player1_scout = []

player2_army = []
player2_spearman = []
player2_archer = []
player2_knight = []
player2_scout = []

player_armies = [player1_army, player2_army]
player_spearmans = [player1_spearman, player2_spearman]
player_archers = [player1_archer, player2_archer]
player_knights = [player1_knight, player2_knight]
player_scouts = [player1_scout, player2_scout]


player1 = player(10,10,10,1)

player2 = player(10,10,10,2)

#running the game
#opening
print("Game Started: Little Battle! (enter QUIT to quit the game)")
print()

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

            print("You has recruited a {}.".format(unit_name))
            print()

            player1.print_resource()

        game.print_map()

    else:
        break

player2.print_recruit_turn()
player2.print_resource()

while player2.check_resource() == True:
    if player2.home_sweep() == True:

        unit = player1.purchase_unit()
        if unit == None:
            break
        else:
            unit_name = player2.resolve_unit_name()
            player2.unit_placement()

            print("You has recruited a {}.".format(unit_name))
            print()

            player2.print_resource()

        game.print_map()

    else:
        break

while True:
    player1.print_move_turn()
    player1.print_army_to_move()
    while player1.check_armies() == True:
        coords = player1.unit_movement_input()
        if coords == 'None':
            break
        else:
            current_coords = coords[0]
            desired_coords = coords[1]
        break
    print(player1.spearman)

    print(current_coords)
    print(desired_coords)
    player1.unit_movement_output_general()
    game.print_map()
    print(player2_knight)

print('END OF CODE')
