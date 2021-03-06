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

        self.army = []

        self.spearman = []
        self.spearman_post = []

        self.archer = []
        self.archer_post = []

        self.knight = []
        self.knight_post = []

        self.scout = []
        self.scout_post = []

        self.player_number = players[self.player_number_input-1]
        self.home_position = home_bases[self.player_number_input-1]

    def print_resource(self):
        print("[Your Asset: Wood - {} Food - {} Gold - {}]".format(self.wood,self.food,self.gold))

    def print_recruit_turn(self):
        print("+++Player {}'s Stage: Recruit Armies+++".format(self.player_number))
        print()

    def check_resource(self):
        if self.wood>0 or self.food>0 or self.gold>0:
            return True
        else:
            print("No resources to recruit any armies.")
            return False

    def purchase_unit(self):
        while True:
            print()
            unit = input("Which type of army to recruit, (enter) ???S???, ???A???, ???K???, or ???T???? Enter ???NO??? to end this stage.\n")

            #buying a spearman
            if unit == "S":
                if self.wood<1 or self.food<1:
                    print("Insufficient resources. Try again.")
                else:
                    self.wood = self.wood - spearman.wood_cost
                    self.food = self.food - spearman.food_cost
                    self.gold = self.gold - spearman.gold_cost
                    return 'S'
            #buying an archer
            elif unit == "A":
                if self.wood<1 or self.gold<1:
                    print("Insufficient resources. Try again.")
                else:
                    self.wood = self.wood - archer.wood_cost
                    self.food = self.food - archer.food_cost
                    self.gold = self.gold - archer.gold_cost
                    return 'A'
            #buying a knight
            elif unit == "K":
                if self.food<1 or self.gold<1:
                    print("Insufficient resources. Try again.")
                else:
                    self.wood = self.wood - knight.wood_cost
                    self.food = self.food - knight.food_cost
                    self.gold = self.gold - knight.gold_cost
                    return 'K'
            #buying a scout
            elif unit == "T":
                if self.wood<1 or self.food<1 or self.gold<1:
                    print("Insufficient resources. Try again.")
                else:
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
            placement_coords = input("You want to recruit a {}. Enter two integers as format ???x y??? to place your army.\n".format(unit_name))

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
            if all([v == '' for v in self.spearman]):
                pass
            else:
                print("  Spearman:",end='')
                for i in range(len(self.spearman)-1):
                    if self.spearman[i] == '':
                        pass
                    else:
                        print(' {},'.format(self.spearman[i]),end='')
                print(' {}'.format(self.spearman[-1]))

        if 'A' in self.army:
            if all([v == '' for v in self.archer]):
                pass
            else:
                print("  Archer:",end='')
                for i in range(len(self.archer)-1):
                    if self.archer[i] == '':
                        pass
                    else:
                        print(' {},'.format(self.archer[i]),end='')
                print(' {}'.format(self.archer[-1]))
   
        if 'K' in self.army:
            if all([v == '' for v in self.knight]):
                pass
            else:
                print("  Knight:",end='')
                for i in range(len(self.knight)-1):
                    if self.knight[i] == '':
                        pass
                    else:
                        print(' {},'.format(self.knight[i]),end='')
                print(' {}'.format(self.knight[-1]))          

        if 'T' in self.army:
            if all([v == '' for v in self.scout]):
                pass
            else:
                print("  Scout:",end='')
                for i in range(len(self.scout)-1):
                    if self.scout[i] == '':
                        pass
                    else:
                        print(' {},'.format(self.scout[i]),end='')
                print(' {}'.format(self.scout[-1]))

        print()

    def print_move_turn(self):
        print()
        print("===Player {}'s Stage: Move Armies===".format(self.player_number))

    def check_armies(self):
        if (all([v == '' for v in self.spearman]) or len(self.spearman) == 0 ) and (all([v == '' for v in self.archer]) or len(self.archer) == 0 ) and (all([v == '' for v in self.knight]) or len(self.knight) == 0) and (all([v == '' for v in self.scout]) or len(self.scout) == 0):
            print("No Army to Move: next turn.")
            print()
            return False
        else:
            return True

    def unit_movement_input(self):
        while True:
            print()
            self.print_army_to_move()
            movement_input = input("Enter four integers as a format ???x0 y0 x1 y1??? to represent move unit from (x0, y0) to (x1, y1) or ???NO??? to end this turn.\n")
            if movement_input == 'NO':
                print()
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
                            print("Invalid move. Try again.")
                        else:
                            current_coords = (movement_input[0],movement_input[1])
                            desired_coords = (movement_input[2],movement_input[3])
                            tile = game.map[desired_coords[0]][desired_coords[1]]

                            #checking if a friendly unit is already in tile
                            if '{}'.format(self.player_number) in tile:
                                print("Invalid move. Try again")

                            #checking if the unit exists 
                            elif current_coords in self.spearman or current_coords in self.archer or current_coords in self.knight or current_coords in self.scout:

                                #scout move input checking
                                if current_coords in self.scout:
                                    if desired_coords[0] == current_coords[0]+1 and desired_coords[1] == current_coords[1] or desired_coords[0] == current_coords[0]-1 and desired_coords[1] == current_coords[1] or desired_coords[0] == current_coords[0] and desired_coords[1] == current_coords[1]+1 or desired_coords[0] == current_coords[0] and desired_coords[1] == current_coords[1]-1:
                                        opponent = players[self.player_number-2]
                                        if 'H{}'.format(opponent) in tile:
                                            if current_coords in self.spearman:
                                                unit_name = "Spearman"
                                            elif current_coords in self.archer:
                                                unit_name = "Archer"
                                            elif current_coords in self.knight:
                                                unit_name = "Knight"
                                            elif current_coords in self.scout:
                                                unit_name = 'Scout'
                                            print("The army {} captured the enemy???s capital.".format(unit_name))
                                            print()
                                            king = input("What???s your name, commander?\n")
                                            print()
                                            print("***Congratulation! Emperor {} unified the country in {}.***".format(king,year))
                                            exit()
                                        else:
                                            return(current_coords,desired_coords)

                                    elif desired_coords[0] == current_coords[0]+2 and desired_coords[1] == current_coords[1] or desired_coords[0] == current_coords[0]-2 and desired_coords[1] == current_coords[1] or desired_coords[0] == current_coords[0] and desired_coords[1] == current_coords[1]+2 or desired_coords[0] == current_coords[0] and desired_coords[1] == current_coords[1]-2:
                                        if current_coords[0] == desired_coords[0]:
                                            difference = desired_coords[1] - current_coords[1]
                                            choice = 'y{}'.format(difference)

                                        elif current_coords[1] == desired_coords[1]:
                                            difference = desired_coords[0] - current_coords[0]
                                            choice = 'x{}'.format(difference)

                                        if choice == 'y2':
                                            tile = game.map[desired_coords[0]][(desired_coords[1]-1)]
                                            opponent = players[self.player_number-2]
                                            if 'H{}'.format(opponent) in tile:
                                                if current_coords in self.spearman:
                                                    unit_name = "Spearman"
                                                elif current_coords in self.archer:
                                                    unit_name = "Archer"
                                                elif current_coords in self.knight:
                                                    unit_name = "Knight"
                                                elif current_coords in self.scout:
                                                    unit_name = 'Scout'
                                                print(unit_name)
                                                print("The army {} captured the enemy???s capital.".format(unit_name))
                                                print()
                                                king = input("What???s your name, commander?\n")
                                                print()
                                                print("***Congratulation! Emperor {} unified the country in {}.***".format(king,year))
                                                exit()
                                            else:
                                                return(current_coords,desired_coords)

                                        elif choice == 'y-2':
                                            tile = game.map[desired_coords[0]][(desired_coords[1]+1)]
                                            opponent = players[self.player_number-2]
                                            if 'H{}'.format(opponent) in tile:
                                                if current_coords in self.spearman:
                                                    unit_name = "Spearman"
                                                elif current_coords in self.archer:
                                                    unit_name = "Archer"
                                                elif current_coords in self.knight:
                                                    unit_name = "Knight"
                                                elif current_coords in self.scout:
                                                    unit_name = 'Scout'
                                                print(unit_name)
                                                print("The army {} captured the enemy???s capital.".format(unit_name))
                                                print()
                                                king = input("What???s your name, commander?\n")
                                                print()
                                                print("***Congratulation! Emperor {} unified the country in {}.***".format(king,year))
                                                exit()                                                
                                            else:
                                                return(current_coords,desired_coords)

                                        elif choice == 'x2':
                                            tile = game.map[(desired_coords[0]-1)][desired_coords[1]]
                                            opponent = players[self.player_number-2]

                                            if 'H{}'.format(opponent) in tile:
                                                if current_coords in self.spearman:
                                                    unit_name = "Spearman"
                                                elif current_coords in self.archer:
                                                    unit_name = "Archer"
                                                elif current_coords in self.knight:
                                                    unit_name = "Knight"
                                                elif current_coords in self.scout:
                                                    unit_name = 'Scout'
                                                print(unit_name)
                                                print("The army {} captured the enemy???s capital.".format(unit_name))
                                                print()
                                                king = input("What???s your name, commander?\n")
                                                print()
                                                print("***Congratulation! Emperor {} unified the country in {}.***".format(king,year))
                                                exit()  
                                            else:
                                                return(current_coords,desired_coords)

                                        elif choice == 'x-2':
                                            tile = game.map[(desired_coords[0]+1)][desired_coords[1]]
                                            opponent = players[self.player_number-2]
                                        
                                            if 'H{}'.format(opponent) in tile:
                                                if current_coords in self.spearman:
                                                    unit_name = "Spearman"
                                                elif current_coords in self.archer:
                                                    unit_name = "Archer"
                                                elif current_coords in self.knight:
                                                    unit_name = "Knight"
                                                elif current_coords in self.scout:
                                                    unit_name = 'Scout'
                                                print(unit_name)
                                                print("The army {} captured the enemy???s capital.".format(unit_name))
                                                print()
                                                king = input("What???s your name, commander?\n")
                                                print()
                                                print("***Congratulation! Emperor {} unified the country in {}.***".format(king,year))
                                                exit()  
                                            else:
                                                return(current_coords,desired_coords)
                                    else:
                                        print("Invalid move. Try again")
                                #others move input checking 
                                else:
                                    if desired_coords[0] == current_coords[0]+1 and desired_coords[1] == current_coords[1] or desired_coords[0] == current_coords[0]-1 and desired_coords[1] == current_coords[1] or desired_coords[0] == current_coords[0] and desired_coords[1] == current_coords[1]+1 or desired_coords[0] == current_coords[0] and desired_coords[1] == current_coords[1]-1:
                                        opponent = players[self.player_number-2]
                                        if 'H{}'.format(opponent) in tile:
                                            if current_coords in self.spearman:
                                                unit_name = "Spearman"
                                            elif current_coords in self.archer:
                                                unit_name = "Archer"
                                            elif current_coords in self.knight:
                                                unit_name = "Knight"
                                            elif current_coords in self.scout:
                                                unit_name = 'Scout'
                                            print(unit_name)
                                            print("The army {} captured the enemy???s capital.".format(unit_name))
                                            print()
                                            king = input("What???s your name, commander?\n")
                                            print()
                                            print("***Congratulation! Emperor {} unified the country in {}.***".format(king,year))
                                            exit()

                                        else:
                                            return(current_coords,desired_coords)
                                    else:
                                        print("Invalid move. Try again")
                            else:
                                print("Invalid move. Try again")
    
    def spearman_output(self):
        index = self.spearman.index(current_coords)
        game.map[current_coords[0]][current_coords[1]] = '  '
        game.map[desired_coords[0]][desired_coords[1]] = 'S{}'.format(self.player_number)
        self.spearman_post[index] = desired_coords
        self.spearman[index] = ''

    def archer_output(self):
        index = self.archer.index(current_coords)
        game.map[current_coords[0]][current_coords[1]] = '  '
        game.map[desired_coords[0]][desired_coords[1]] = 'A{}'.format(self.player_number)
        self.archer_post[index] = desired_coords
        self.archer[index] = ''

    def knight_output(self):
        index = self.knight.index(current_coords)
        game.map[current_coords[0]][current_coords[1]] = '  '
        game.map[desired_coords[0]][desired_coords[1]] = 'K{}'.format(self.player_number)
        self.knight_post[index] = desired_coords
        self.knight[index] = ''

    def scout_output(self):
        index = self.scout.index(current_coords)
        game.map[current_coords[0]][current_coords[1]] = '  '
        game.map[desired_coords[0]][desired_coords[1]] = 'T{}'.format(self.player_number)
        self.scout_post[index] = desired_coords
        self.scout[index] = ''

    def opponent_knight_death(self):
        if self.player_number_input == 1:
            player2.knight.remove(desired_coords)
        elif self.player_number_input == 2:
            player1.knight.remove(desired_coords)
        game.map[desired_coords[0]][desired_coords[1]] = '  '

    def opponent_archer_death(self):
        if self.player_number_input == 1:
            player2.archer.remove(desired_coords)
        elif self.player_number_input == 2:
            player1.archer.remove(desired_coords)
        game.map[desired_coords[0]][desired_coords[1]] = '  '

    def opponent_spearman_death(self):
        if self.player_number_input == 1:
            player2.spearman.remove(desired_coords)
        elif self.player_number_input == 2:
            player1.spearman.remove(desired_coords)
        game.map[desired_coords[0]][desired_coords[1]] = '  '

    def opponent_scout_death(self):
        if self.player_number_input == 1:
            player2.scout.remove(desired_coords)
        elif self.player_number_input == 2:
            player1.scout.remove(desired_coords)
        game.map[desired_coords[0]][desired_coords[1]] = '  '
              
    def self_spearman_death(self):
        index = self.spearman.index(current_coords)
        del self.spearman[index]
        del self.spearman_post[index]
        game.map[current_coords[0]][current_coords[1]] = '  '

    def self_archer_death(self):
        index = self.archer.index(current_coords)
        del self.archer[index]
        del self.archer_post[index]
        game.map[current_coords[0]][current_coords[1]] = '  '

    def self_knight_death(self):
        index = self.knight.index(current_coords)
        del self.knight[index]
        del self.knight_post[index]
        game.map[current_coords[0]][current_coords[1]] = '  '

    def self_scout_death(self):
        index = self.scout.index(current_coords)
        del self.scout[index]
        del self.scout_post[index]
        game.map[current_coords[0]][current_coords[1]] = '  ' 

    def resolve_coordinates(self):
        self.spearman = self.spearman_post.copy() 
        self.archer = self.archer_post.copy()
        self.knight = self.knight_post.copy()
        self.scout = self.scout_post.copy()
        self.spearman_post = []
        self.archer_post = []
        self.knight_post = []
        self.scout_post = []

    def copy_to_post(self):
        self.spearman_post = self.spearman.copy()
        self.archer_post = self.archer.copy()
        self.knight_post = self.knight.copy()
        self.scout_post = self.scout.copy()

    def resolve_unit_from_coordinates(self):
        if current_coords in self.spearman:
            return "Spearman"
        elif current_coords in self.archer:
            return "Archer"
        elif current_coords in self.knight:
            return "Knight"
        elif current_coords in self.scout:
            return 'Scout'
        
    def unit_movement_output_general(self):
        tile = game.map[desired_coords[0]][desired_coords[1]]
        print()
        print("You have moved {} from {} to {}.".format(unit_name,current_coords,desired_coords))
        if tile == '~~':
            print("We lost the army {} due to your command!".format(unit_name))
            if current_coords in self.spearman:
                self.self_spearman_death()
            elif current_coords in self.archer:
                self.self_archer_death()
            elif current_coords in self.knight:
                self.self_knight_death()

        elif tile == 'GG':
            self.gold += 2
            if current_coords in self.spearman:
                self.spearman_output()
            elif current_coords in self.archer:
                self.archer_output()
            elif current_coords in self.knight:
                self.knight_output()
            print("Good. We collected 2 Gold")

        elif tile == 'FF':
            self.food += 2
            if current_coords in self.spearman:
                self.spearman_output()
            elif current_coords in self.archer:
                self.archer_output()
            elif current_coords in self.knight:
                self.knight_output()
            print("Good. We collected 2 Food")

        elif tile == 'WW':
            self.wood += 2
            if current_coords in self.spearman:
                self.spearman_output()
            elif current_coords in self.archer:
                self.archer_output()
            elif current_coords in self.knight:
                self.knight_output()
            print("Good. We collected 2 Wood")

        else:
            if current_coords in self.spearman:
                if 'K' in tile:
                    print("Great! We defeated the enemy Knight!")
                    self.opponent_knight_death()
                    self.spearman_output()
                elif 'T' in tile:
                    print("Great! We defeated the enemy Scout!")   
                    self.opponent_scout_death()
                    self.spearman_output()
                elif 'A' in tile:
                    print("We lost the army Spearman due to your command!")
                    self.self_spearman_death()
                elif 'S' in tile:
                    print("We destroyed the enemy Spearman with massive loss!")
                    self.opponent_spearman_death()
                    self.self_spearman_death()
                else:
                    self.spearman_output()
            elif current_coords in self.archer:
                if 'S' in tile:
                    print("Great! We defeated the enemy Spearman!")
                    self.opponent_spearman_death()
                    self.archer_output()
                elif 'T' in tile:
                    print("Great! We defeated the enemy Scout!")
                    self.opponent_scout_death()
                    self.archer_output()
                elif 'K' in tile:
                    print("We lost the army Spearman due to your command!")
                    self.self_archer_death()
                elif 'A' in tile:
                    print("We destroyed the enemy Archer with massive loss!")
                    self.opponent_archer_death()
                    self.self_archer_death()
                else:
                    self.archer_output()
            elif current_coords in self.knight:
                if 'A' in tile:
                    print("Great! We defeated the enemy Archer!")
                    self.opponent_archer_death()
                    self.knight_output()
                elif 'T' in tile:
                    print("Great! We defeated the enemy Scout!")
                    self.opponent_scout_death()
                    self.knight_output()
                elif 'S' in tile:
                    print("We lost the army Knight due to your command!")
                    self.self_knight_death()
                elif 'K' in tile:
                    print("We destroyed the enemy Knight with massive loss!")
                    self.opponent_knight_death()
                    self.self_knight_death()
                else:
                    self.knight_output()
            else:
                pass

    def scout_movement_choice(self):
        if current_coords[0] == desired_coords[0]:
            difference = desired_coords[1] - current_coords[1]
            if abs(difference) == 1:
                return 1
            else:
                return 'y{}'.format(difference)

        elif current_coords[1] == desired_coords[1]:
            difference = desired_coords[0] - current_coords[0]
            if abs(difference) == 1:
                return 1
            else: 
                return 'x{}'.format(difference)

    def unit_movement_output_scout(self):
        tile = game.map[desired_coords[0]][desired_coords[1]]
        opponent = players[self.player_number-2]
        print()
        print("You have moved {} from {} to {}.".format(unit_name,current_coords,desired_coords))

        if choice == 1:
            if tile == '~~':
                print("We lost the army {} due to your command!".format(unit_name))
                self.self_scout_death()

            elif tile == 'GG':
                self.gold += 2
                self.scout_output()
                print("Good. We collected 2 Gold")

            elif tile == 'FF':
                self.food += 2
                self.scout_output()
                print("Good. We collected 2 Food")

            elif tile == 'WW':
                self.wood += 2
                self.scout_output()
                print("Good. We collected 2 Wood")

            else:
                if 'S' in tile or 'A' in tile or 'K' in tile:
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()

                elif 'T' in tile:
                    print("We destroyed the enemy Scout with massive loss!")
                    self.self_scout_death()
                    self.opponent_scout_death()

                else:
                    self.scout_output()

        elif choice == 'y-2':
            tile = game.map[desired_coords[0]][(desired_coords[1]+1)]

            if tile == '~~':
                print("We lost the army {} due to your command!".format(unit_name))
                self.self_scout_death()
            elif tile == 'GG':
                self.gold += 2
                print("Good. We collected 2 Gold")
                game.map[desired_coords[0]][(desired_coords[1]+1)] = '  '

                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    self.scout_output()
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print("We lost the army {} due to your command!".format(unit_name))
                        self.self_scout_death()

                    elif 'T' in tile:
                        self.self_scout_death()
                        self.opponent_scout_death()

                    else:
                        self.scout_output()

            elif tile == 'FF':
                self.food += 2
                print("Good. We collected 2 Food")
                game.map[desired_coords[0]][(desired_coords[1]+1)] = '  '
                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    self.scout_output()
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print("We lost the army {} due to your command!".format(unit_name))
                        self.self_scout_death()

                    elif 'T' in tile:
                        self.self_scout_death()
                        self.opponent_scout_death()

                    else:
                        self.scout_output()

            elif tile == 'WW':
                self.wood += 2
                print("Good. We collected 2 Wood")
                game.map[desired_coords[0]][(desired_coords[1]+1)] = '  '

                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    self.scout_output()
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print("We lost the army {} due to your command!".format(unit_name))
                        self.self_scout_death()

                    elif 'T' in tile:
                        self.self_scout_death()
                        self.opponent_scout_death()

                    else:
                        self.scout_output()

            elif 'S{}'.format(opponent) in tile or 'A{}'.format(opponent) in tile or 'K{}'.format(opponent) in tile:
                print("We lost the army {} due to your command!".format(unit_name))
                self.self_scout_death()

            elif 'T{}'.format(opponent) in tile:
                print("We destroyed the enemy Scout with massive loss!")
                self.self_scout_death()

                a = desired_coords[0],desired_coords[1]+1
                
                if self.player_number_input == 1:
                    player2.scout.remove(a)
                elif self.player_number_input == 2:
                    player1.scout.remove(a)
                game.map[a[0]][a[1]] = '  '                

            else:
                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    self.scout_output()
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print("We lost the army {} due to your command!".format(unit_name))
                        self.self_scout_death()

                    elif 'T' in tile:
                        self.self_scout_death()
                        self.opponent_scout_death()
                    else:
                        self.scout_output()   

        elif choice == 'y2':
            tile = game.map[desired_coords[0]][(desired_coords[1]-1)]
            if tile == '~~':
                print("We lost the army {} due to your command!".format(unit_name))
                self.self_scout_death()
            elif tile == 'GG':
                self.gold += 2
                print("Good. We collected 2 Gold")
                game.map[desired_coords[0]][(desired_coords[1]-1)] = '  '

                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    self.scout_output()
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print("We lost the army {} due to your command!".format(unit_name))
                        self.self_scout_death()

                    elif 'T' in tile:
                        self.self_scout_death()
                        self.opponent_scout_death()

                    else:
                        self.scout_output()

            elif tile == 'FF':
                self.food += 2
                print("Good. We collected 2 Food")
                game.map[desired_coords[0]][(desired_coords[1]-1)] = '  '

                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    self.scout_output()
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print("We lost the army {} due to your command!".format(unit_name))
                        self.self_scout_death()

                    elif 'T' in tile:
                        self.self_scout_death()
                        self.opponent_scout_death()

                    else:
                        self.scout_output()

            elif tile == 'WW':
                self.wood += 2
                print("Good. We collected 2 Wood")
                game.map[desired_coords[0]][(desired_coords[1]-1)] = '  '

                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    self.scout_output()
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print("We lost the army {} due to your command!".format(unit_name))
                        self.self_scout_death()

                    elif 'T' in tile:
                        self.self_scout_death()
                        self.opponent_scout_death()

                    else:
                        self.scout_output()

            elif 'S{}'.format(opponent) in tile or 'A{}'.format(opponent) in tile or 'K{}'.format(opponent) in tile:
                print("We lost the army {} due to your command!".format(unit_name))
                self.self_scout_death()

            elif 'T{}'.format(opponent) in tile:
                print("We destroyed the enemy Scout with massive loss!")
                self.self_scout_death()

                a = desired_coords[0],desired_coords[1]-1
                
                if self.player_number_input == 1:
                    player2.scout.remove(a)
                elif self.player_number_input == 2:
                    player1.scout.remove(a)
                game.map[a[0]][a[1]] = '  ' 

            else:
                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    self.scout_output()
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print('We lost the army Scout due to your command!')
                        self.self_scout_death()
                    elif 'T' in tile:
                        print('We destroyed the enemy Scout with massive loss!')
                        self.self_scout_death()
                        self.opponent_scout_death()
                    else:
                        self.scout_output()   
        
        elif choice == 'x-2':
            tile = game.map[(desired_coords[0]+1)][desired_coords[1]]

            if tile == '~~':
                print("We lost the army {} due to your command!".format(unit_name))
                self.self_scout_death()

            elif tile == 'GG':
                self.gold += 2
                print("Good. We collected 2 Gold")
                game.map[(desired_coords[0]+1)][desired_coords[1]] = '  '

                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    self.scout_output()
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print("We lost the army {} due to your command!".format(unit_name))
                        self.self_scout_death()

                    elif 'T' in tile:
                        self.self_scout_death()
                        self.opponent_scout_death()

                    else:
                        self.scout_output()

            elif tile == 'FF':
                self.food += 2
                print("Good. We collected 2 Food")
                game.map[(desired_coords[0]+1)][desired_coords[1]] = '  '

                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    self.scout_output()
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print("We lost the army {} due to your command!".format(unit_name))
                        self.self_scout_death()

                    elif 'T' in tile:
                        self.self_scout_death()
                        self.opponent_scout_death()

                    else:
                        self.scout_output()

            elif tile == 'WW':
                self.wood += 2
                print("Good. We collected 2 Wood")
                game.map[(desired_coords[0]+1)][desired_coords[1]] = '  '

                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    self.scout_output()
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print("We lost the army {} due to your command!".format(unit_name))
                        self.self_scout_death()

                    elif 'T' in tile:
                        self.self_scout_death()
                        self.opponent_scout_death()

                    else:
                        self.scout_output()

            elif 'S{}'.format(opponent) in tile or 'A{}'.format(opponent) in tile or 'K{}'.format(opponent) in tile:
                print("We lost the army {} due to your command!".format(unit_name))
                self.self_scout_death()

            elif 'T{}'.format(opponent) in tile:
                print('We destroyed the enemy Scout with massive loss!')
                self.self_scout_death()
                
                a = desired_coords[0]+1,desired_coords[1]
                
                if self.player_number_input == 1:
                    player2.scout.remove(a)
                elif self.player_number_input == 2:
                    player1.scout.remove(a)
                game.map[a[0]][a[1]] = '  '                 

            else:
                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print("We lost the army {} due to your command!".format(unit_name))
                        self.self_scout_death()
                    elif 'T' in tile:
                        print("We destroyed the enemy Scout with massive loss!")
                        self.self_scout_death()
                        self.opponent_scout_death()
                    else:
                        self.scout_output()   

        elif choice == 'x2':
            tile = game.map[(desired_coords[0]-1)][desired_coords[1]]

            if tile == '~~':
                print("We lost the army {} due to your command!".format(unit_name))
                self.self_scout_death()

            #checking resources
            elif tile == 'GG':
                self.gold += 2
                print("Good. We collected 2 Gold")
                game.map[(desired_coords[0]-1)][desired_coords[1]] = '  '

                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    self.scout_output()
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print("We lost the army {} due to your command!".format(unit_name))
                        self.self_scout_death()

                    elif 'T' in tile:
                        print("We destroyed the enemy Scout with massive loss!")
                        self.self_scout_death()
                        self.opponent_scout_death()

                    else:
                        self.scout_output()

            elif tile == 'FF':
                self.food += 2
                print("Good. We collected 2 Food")
                game.map[(desired_coords[0]-1)][desired_coords[1]] = '  '

                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    self.scout_output()
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print("We lost the army {} due to your command!".format(unit_name))
                        self.self_scout_death()

                    elif 'T' in tile:
                        self.self_scout_death()
                        self.opponent_scout_death()

                    else:
                        self.scout_output()   

            elif tile == 'WW':
                self.wood += 2
                print("Good. We collected 2 Wood")
                game.map[(desired_coords[0]-1)][desired_coords[1]] = '  '

                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    self.scout_output()
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print("We lost the army {} due to your command!".format(unit_name))
                        self.self_scout_death()

                    elif 'T' in tile:
                        self.self_scout_death()
                        self.opponent_scout_death()

                    else:
                        self.scout_output()   

            #checking for enemies
            elif 'S{}'.format(opponent) in tile or 'A{}'.format(opponent) in tile or 'K{}'.format(opponent) in tile:
                print("We lost the army {} due to your command!".format(unit_name))
                self.self_scout_death()

            elif 'T{}'.format(opponent) in tile:
                print("We destroyed the enemy Scout with massive loss!")
                self.self_scout_death()
                
                a = desired_coords[0]-1,desired_coords[1]
                
                if self.player_number_input == 1:
                    player2.scout.remove(a)
                elif self.player_number_input == 2:
                    player1.scout.remove(a)
                game.map[a[0]][a[1]] = '  '                 

            #checking 2 tiles away
            else:
                tile = game.map[desired_coords[0]][desired_coords[1]]
                if tile == '~~':
                    print("We lost the army {} due to your command!".format(unit_name))
                    self.self_scout_death()
                elif tile == 'GG':
                    self.gold += 2
                    self.scout_output()
                    print("Good. We collected 2 Gold")

                elif tile == 'FF':
                    self.food += 2
                    self.scout_output()
                    print("Good. We collected 2 Food")

                elif tile == 'WW':
                    self.wood += 2
                    self.scout_output()
                    print("Good. We collected 2 Wood")
                else:
                    if 'S' in tile or 'A' in tile or 'K' in tile:
                        print("We lost the army {} due to your command!".format(unit_name))
                        self.self_scout_death()

                    elif 'T' in tile:
                        print("We destroyed the enemy Scout with massive loss!")
                        self.self_scout_death()
                        self.opponent_scout_death()

                    else:
                        self.scout_output()   



#initialize game
cols, rows = (5,5)
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

player1 = player(4,4,4,1)

player2 = player(2,2,2,2)

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

while True:
    game.print_year()

#player 1 recruit army
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

        else:
            break

#player 1 move army
    player1.copy_to_post()
    player1.print_move_turn()

    while player1.check_armies() == True:
        coords = player1.unit_movement_input()
        if coords == None:
            break
        else:
            current_coords = coords[0]
            desired_coords = coords[1]

            unit_name = player1.resolve_unit_from_coordinates()

            if current_coords in player1.scout:
                choice = player1.scout_movement_choice()
                player1.unit_movement_output_scout()
                game.print_map()
            else:
                player1.unit_movement_output_general()
                game.print_map()

    player1.resolve_coordinates()

#player 2 recruit army
    player2.print_recruit_turn()
    player2.print_resource()

    while player2.check_resource() == True:
        if player2.home_sweep() == True:

            unit = player2.purchase_unit()
            if unit == None:
                break
            else:
                unit_name = player2.resolve_unit_name()
                player2.unit_placement()

                print()
                print("You has recruited a {}.".format(unit_name))
                print()

                player2.print_resource()

            game.print_map()
            

        else:
            break

#player 2 move army
    player2.copy_to_post()
    player2.print_move_turn()

    while player2.check_armies() == True:
        coords = player2.unit_movement_input()
        if coords == None:
            break
        else:
            current_coords = coords[0]
            desired_coords = coords[1]

            unit_name = player2.resolve_unit_from_coordinates()

            if current_coords in player2.scout:
                choice = player2.scout_movement_choice()
                player2.unit_movement_output_scout()
                game.print_map()
            else:
                player2.unit_movement_output_general()
                game.print_map()
                
    player2.resolve_coordinates()

#end of turn
    year += 1

