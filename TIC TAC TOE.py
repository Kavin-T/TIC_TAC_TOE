import random 
class tic_tac_toe:
    def __init__(self):
        self.grid=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.position_index={1:[0,0,0],2:[0,1,0],3:[0,2,0],4:[1,0,0],5:[1,1,0],6:[1,2,0],7:[2,0,0],8:[2,1,0],9:[2,2,0]}
        self.empty_position=[pos for pos in range(1,10)]
    def position_input(self,choice="X",computer=0):    
        if computer==1:
            position=random.choice(self.empty_position)
        else:
            position=int(input("ENTER THE POSITION:"))
        while (1>position or position>9) or (self.position_index[position][2]==1):
            if computer==1:
                position=random.choice(self.empty_position)
            else:
                print("ENTER VALID POSITION [1-9]")
                position=int(input("ENTER THE POSITION:"))
        else:
            self.grid[self.position_index[position][0]][self.position_index[position][1]]=choice
            self.position_index[position][2]=1 
            self.empty_position.remove(position)
    def check_win(self):
        for row in self.grid:
            if row[0]==row[1]==row[2]!=" ":
                return(row[0])
        for col in range(3):
            if self.grid[0][col]==self.grid[1][col]==self.grid[2][col]!=" ":
                return(self.grid[0][col])
        if self.grid[0][0]==self.grid[1][1]==self.grid[2][2]!=" ":
                return(self.grid[0][0])
        if self.grid[0][2]==self.grid[1][1]==self.grid[2][0]!=" ":
                return(self.grid[0][2])
        return("D")
    def position_display(self):
        print("POSITION")
        print("-------------")
        print(f"| 1 | 2 | 3 |")
        print("-------------")
        print(f"| 4 | 5 | 6 |")
        print("-------------")
        print(f"| 7 | 8 | 9 |")
        print("-------------")
    def grid_display(self):
        print("-------------")
        print(f"| {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} |")
        print("-------------")
        print(f"| {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} |")
        print("-------------")
        print(f"| {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]} |")
        print("-------------")
    #def position_of_O(self):
def play():
    game=tic_tac_toe()
    print("1.SINGLEPLAYER\n2.MULTIPLAYER")
    choice=int(input("ENTER THE CHOICE(1/2):"))
    while 1>choice or choice>2:
        choice=int(input("ENTER VALID CHOICE(1/2):"))
    game=tic_tac_toe()    
    rounds=0
    game.grid_display()
    game.position_display()
    while rounds<10:
        print("PLAYER 1")
        game.position_input()
        game.grid_display()
        win=game.check_win()
        if win!="D" or rounds==8:
            break
        if choice==1:
            print("COMPUTER")
            game.position_input("O",1)
        else:
            print("PLAYER 2")
            game.position_input("O")
        game.grid_display()
        win=game.check_win()
        if win!="D":
            break
        rounds+=2
    if win=="D":
        print("GAME DRAW")
    else:
        print(f"{win} WINS!!!")
print("1.PLAY\n2.EXIT")
choice=int(input("ENTER YOUR CHOICE(1/2):"))
while choice==1:
    play()
    print("1.REPLAY\n2.EXIT")
    choice=int(input("ENTER YOUR CHOICE(1/2):"))
else:
    print("GAME EXITED")