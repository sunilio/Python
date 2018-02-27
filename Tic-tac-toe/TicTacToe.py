
class Player():

    def __init__(self):

        self.Name = ''
        self.PlayingMark = ''
        self.won = 0
        self.draw = 0
        self.lost = 0
        self.score = 0

    def get_score(self):  # this function is for calculating the score using formulae

        return((self.won * 2) + self.draw - self.lost)

    def __str__(self): # this function is for printing the Statistics

        return('\n\nStatistics :   '+ self.Name + "\n\n\n    WON                   DRAW                   LOST                   Overall SCORE")



class Deck(object):


    Board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    Player1choices = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    Player2choices = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def __init__(self):

        play = ''
        play = ''



    def __str__(self):  # this function is for printing the board

        return ("       |     |     \n   " + self.Board[0] + "   |  " + self.Board[1] + "  |  " + self.Board[2] + "\n  _____|_____|_____\n       |     |     \n "
             "  " + self.Board[3] + "   |  "  + self.Board[4] +  "  |  "+ self.Board[5] + "  \n  _____|_____|____\n       |     |     \n   "  + self.Board[6] + ""
                "   |  " + self.Board[7] + "  |  " + self.Board[8] + "\n       |     |     \n\n")





class TicTacToe():

    Player1= Player()

    Deck_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def __init__(self):
        Player1 = ""
        Player2 = ""





    def validate_user_input(ch ):

        '''
        validates the user input if it is out of scope
        '''




        if ch == '0' or ch == '1' or ch == '2' or ch == '3' or ch == '4' or ch == '5' or ch == '6' or ch == '7' or ch== '8':
            return True
        else:
            return False



    def game_over(self,n1,m1):


        p = Deck()

        # checks the player 1 has won or not

        if ( p.Player1choices[0] == '0' and p.Player1choices[1] == '1' and p.Player1choices[2] == '2') or (p.Player1choices[3] == '3' and \
                p.Player1choices[4] == '4'  and p.Player1choices[5] == '5' ) or ( p.Player1choices[6] == '6' and p.Player1choices[7] == '7' and p.Player1choices[8] == '8')\
            or ( p.Player1choices[0] == '0' and p.Player1choices[3] == '3' and p.Player1choices[6] == '6') or ( p.Player1choices[1] == '1' and p.Player1choices[4] == '4' and p.Player1choices[7] == '7')\
            or ( p.Player1choices[2] == '2' and p.Player1choices[5] == '5' and p.Player1choices[8] == '8') or ( p.Player1choices[0] == '0' and p.Player1choices[4] == '4' and p.Player1choices[8] == '8')\
            or ( p.Player1choices[6] == '6' and p.Player1choices[4] == '4' and p.Player1choices[2] == '2'):

            print("GAME WON BY.......", n1.Name,"!! \n \n")
            n1.won = n1.won + 1

            m1.lost = m1.lost+1

            p.Player1choices[0] = ' '
            p.Player1choices[1] = ' '
            p.Player1choices[2] = ' '
            p.Player1choices[3] = ' '
            p.Player1choices[4] = ' '
            p.Player1choices[5] = ' '
            p.Player1choices[6] = ' '
            p.Player1choices[7] = ' '
            p.Player1choices[8] = ' '

            p.Player2choices[0] = ' '
            p.Player2choices[1] = ' '
            p.Player2choices[2] = ' '
            p.Player2choices[3] = ' '
            p.Player2choices[4] = ' '
            p.Player2choices[5] = ' '
            p.Player2choices[6] = ' '
            p.Player2choices[7] = ' '
            p.Player2choices[8] = ' '




            p.Board[0] = ' '
            p.Board[1] = ' '
            p.Board[2] = ' '
            p.Board[3] = ' '
            p.Board[4] = ' '
            p.Board[5] = ' '
            p.Board[6] = ' '
            p.Board[7] = ' '
            p.Board[8] = ' '



            self.Deck_list[0] = ' '
            self.Deck_list[1] = ' '
            self.Deck_list[2] = ' '
            self.Deck_list[3] = ' '
            self.Deck_list[4] = ' '
            self.Deck_list[5] = ' '
            self.Deck_list[6] = ' '
            self.Deck_list[7] = ' '
            self.Deck_list[8] = ' '

            return True

        # checks the player 2 has won or not

        elif ( p.Player2choices[0] == '0' and p.Player2choices[1] == '1' and p.Player2choices[2] == '2') or (p.Player2choices[3] == '3' and p.Player2choices[4] == '4' and p.Player2choices[5] == '5') or\
                (p.Player2choices[6] == '6' and p.Player2choices[7] == '7' and p.Player2choices[8] == '8') or (p.Player2choices[0] == '0' and p.Player2choices[3] == '3' and p.Player2choices[6] == '6') or \
            (p.Player2choices[1] == '1' and p.Player2choices[4] == '4' and p.Player2choices[7] == '7') or (p.Player2choices[2] == '2' and p.Player2choices[5] == '5' and p.Player2choices[8] == '8') or\
            (p.Player2choices[0] == '0' and p.Player2choices[4] == '4' and p.Player2choices[8] == '8') or (p.Player2choices[6] == '6' and p.Player2choices[4] == '4' and p.Player2choices[2] == '2'):



            print("GAME WON BY......",m1.Name,"!! \n \n")

            m1.won= m1.won + 1
            n1.lost=n1.lost + 1


            p.Player2choices[0] = ' '
            p.Player2choices[1] = ' '
            p.Player2choices[2] = ' '
            p.Player2choices[3] = ' '
            p.Player2choices[4] = ' '
            p.Player2choices[5] = ' '
            p.Player2choices[6] = ' '
            p.Player2choices[7] = ' '
            p.Player2choices[8] = ' '


            p.Player1choices[0] = ' '
            p.Player1choices[1] = ' '
            p.Player1choices[2] = ' '
            p.Player1choices[3] = ' '
            p.Player1choices[4] = ' '
            p.Player1choices[5] = ' '
            p.Player1choices[6] = ' '
            p.Player1choices[7] = ' '
            p.Player1choices[8] = ' '



            p.Board[0] = ' '
            p.Board[1] = ' '
            p.Board[2] = ' '
            p.Board[3] = ' '
            p.Board[4] = ' '
            p.Board[5] = ' '
            p.Board[6] = ' '
            p.Board[7] = ' '
            p.Board[8] = ' '

            self.Deck_list[0] = ' '
            self.Deck_list[1] = ' '
            self.Deck_list[2] = ' '
            self.Deck_list[3] = ' '
            self.Deck_list[4] = ' '
            self.Deck_list[5] = ' '
            self.Deck_list[6] = ' '
            self.Deck_list[7] = ' '
            self.Deck_list[8] = ' '



            return True





        elif( p.Board[0] != ' ' and p.Board[1] != ' ' and p.Board[2] != ' ' and p.Board[3] != ' '\
                and p.Board[4] != ' ' and p.Board[5] != ' ' and p.Board[6] != ' ' and p.Board[7] != ' ' and p.Board[8] != ' ' ):  # checks whether the space is full

            print("There is no spaces on the deck so that the match will be considered as draw : ")

            n1.draw= n1.draw + 1
            m1.draw= m1.draw + 1

            p.Player1choices[0] = ' '
            p.Player1choices[1] = ' '
            p.Player1choices[2] = ' '
            p.Player1choices[3] = ' '
            p.Player1choices[4] = ' '
            p.Player1choices[5] = ' '
            p.Player1choices[6] = ' '
            p.Player1choices[7] = ' '
            p.Player1choices[8] = ' '

            p.Player2choices[0] = ' '
            p.Player2choices[1] = ' '
            p.Player2choices[2] = ' '
            p.Player2choices[3] = ' '
            p.Player2choices[4] = ' '
            p.Player2choices[5] = ' '
            p.Player2choices[6] = ' '
            p.Player2choices[7] = ' '
            p.Player2choices[8] = ' '




            p.Board[0] = ' '
            p.Board[1] = ' '
            p.Board[2] = ' '
            p.Board[3] = ' '
            p.Board[4] = ' '
            p.Board[5] = ' '
            p.Board[6] = ' '
            p.Board[7] = ' '
            p.Board[8] = ' '



            self.Deck_list[0] = ' '
            self.Deck_list[1] = ' '
            self.Deck_list[2] = ' '
            self.Deck_list[3] = ' '
            self.Deck_list[4] = ' '
            self.Deck_list[5] = ' '
            self.Deck_list[6] = ' '
            self.Deck_list[7] = ' '
            self.Deck_list[8] = ' '

            return True

        else:

            return False





    def get_user_input(self, n, m):


        n1=n
        m1=m
        p = Deck()
        h = Deck()
        u = Player()


        print(n1.Name,'!!')
        p1 = input('Enter your choice from the above table:\n \n')


        # the while condition will check if the spaces are already chosen are not

        while p1 == self.Deck_list[0] or p1 == self.Deck_list[1] or p1 == self.Deck_list[2] or p1 == self.Deck_list[3] or p1 == self.Deck_list[4]\
                or p1 == self.Deck_list[5] or p1 == self.Deck_list[6] or p1 == self.Deck_list[7] or p1 == self.Deck_list[8]:



            p1 = input("The space has already been chosen....Please choose another one")



        while not self.validate_user_input(p1):  # validates the user input if it is out of the bound

            print(p1, 'is not a valid choice')
            p1 = input("Enter a valid choice:")


        while p1 == self.Deck_list[0] or p1 == self.Deck_list[1] or p1 == self.Deck_list[2] or p1 == self.Deck_list[3] or p1 == self.Deck_list[4]\
                or p1 == self.Deck_list[5] or p1 == self.Deck_list[6] or p1 == self.Deck_list[7] or p1 == self.Deck_list[8]: # again checks for the space chosen or not

            p1 = input("The space has already been chosen....Please choose another space")


        # the if else statement will input the user's input in the board, deck_list and the player choices

        if p1 == '0':

            h.Board[0] = n1.PlayingMark
            self.Deck_list[0] = '0'
            p.Player1choices[0] = '0'


        elif p1 == '1':

            h.Board[1] = n1.PlayingMark
            self.Deck_list[1] = '1'
            p.Player1choices[1] = '1'


        elif p1 == '2':

            h.Board[2] = n1.PlayingMark
            self.Deck_list[2] = '2'
            p.Player1choices[2] = '2'


        elif p1 == '3':

            h.Board[3] = n1.PlayingMark
            self.Deck_list[3] = '3'
            p.Player1choices[3] = '3'


        elif p1 == '4':

            h.Board[4] = n1.PlayingMark
            self.Deck_list[4] = '4'
            p.Player1choices[4] = '4'


        elif p1 == '5':
            h.Board[5] = n1.PlayingMark
            self.Deck_list[5] = '5'
            p.Player1choices[5] = '5'


        elif p1 == '6':
            h.Board[6] = n1.PlayingMark
            self.Deck_list[6] = '6'
            p.Player1choices[6] = '6'


        elif p1 == '7':
            h.Board[7] = n1.PlayingMark
            self.Deck_list[7] = '7'
            p.Player1choices[7] = '7'


        elif p1 == '8':
            h.Board[8] = n1.PlayingMark
            self.Deck_list[8] = '8'
            p.Player1choices[8] = '8'


        print(p.__str__())  # displays the board every time the player enter their choice



        if self.game_over(self,n1, m1):   # checks the game is over by winning or the board is full
            game = '1'
            return game





        print(m.Name,'!!')
        p2 = input("Enter your choice from the above table: \n \n")

        # the while condition will check if the spaces are already chosen are not

        while p2 == self.Deck_list[0] or p2 == self.Deck_list[1] or p2 == self.Deck_list[2] or p2 == self.Deck_list[3] or p2 == self.Deck_list[4]\
                or p2 == self.Deck_list[5] or p2 == self.Deck_list[6] or p2 == self.Deck_list[7] or p2 == self.Deck_list[8]:


            p2 = input("The Space has already been taken. Please choose another space: ")


        while not self.validate_user_input(p2):

            print(p2, ' is not a valid choice')
            p2 = input("Enter a valid choice:")


            while p2 == self.Deck_list[0] or p2 == self.Deck_list[1] or p2 == self.Deck_list[2] or p2 == self.Deck_list[3] or p2 == self.Deck_list[4]\
                    or p2 == self.Deck_list[5] or p2 == self.Deck_list[6] or p2 == self.Deck_list[7] or p2 == self.Deck_list[8]:  # again checks for the space chosen or not

                p2 = input("The Space has already been taken. Please choose another space: ")


        # the if else statement will input the user's input in the board, deck_list and the player choices

        if p2 == '0':
            h.Board[0] = m1.PlayingMark
            self.Deck_list[0] = '0'
            p.Player2choices[0] = '0'

        elif p2 == '1':
            h.Board[1] = m1.PlayingMark
            self.Deck_list[1] = '1'
            p.Player2choices[1] = '1'

        elif p2 == '2':
            h.Board[2] = m1.PlayingMark
            self.Deck_list[2] = '2'
            p.Player2choices[2] = '2'

        elif p2 == '3':
            h.Board[3] = m1.PlayingMark
            self.Deck_list[3] = '3'
            p.Player2choices[3] = '3'

        elif p2 == '4':
            h.Board[4] = m1.PlayingMark
            self.Deck_list[4] = '4'
            p.Player2choices[4] = '4'

        elif p2 == '5':
            h.Board[5] = m1.PlayingMark
            self.Deck_list[5] = '5'
            p.Player2choices[5] = '5'

        elif p2 == '6':
            h.Board[6] = m1.PlayingMark
            self.Deck_list[6] = '6'
            p.Player2choices[6] = '6'

        elif p2 == '7':
            h.Board[7] = m1.PlayingMark
            self.Deck_list[7] = '7'
            p.Player2choices[7] = '7'

        elif p2 == '8':
            h.Board[8] = m1.PlayingMark
            self.Deck_list[8] = '8'
            p.Player2choices[8] = '8'



        print(p.__str__())  # displays the board every time the player enter their choice

        if self.game_over(self, n1, m1):  # checks the game is over by winning or the board is full
            game = '1'
            return game

        else:
            game = '0'
            return game





    def start_game(self):

        # this method is used for accepting user's name and keep calling the get user input function unless the game is over

        print("\n\n                                                                     WELCOME")
        print("                                                     Enter into the Gaming Zone of TIC TAC TOE ")
        print("                                                             Presented by Denil.co ")




        m = Player()
        n = Player()







        n.Name = input("Player 1, Please type your name: \n")      # getting the player1 name
        m.Name = input("\nPlayer 2, Please type your name: \n")    # getting the player2 name

        repeat = 1

        while(repeat == 1):    # this condition keeps repeating unless the mark is either 'X' or 'O'

            print(n.Name, '!! Select your mark : "X" or "O":')

            p = input().upper()

            if p == 'X':
                n.PlayingMark = 'X'
                m.PlayingMark = 'O'
                print(m.Name, '!! Your choice will be "O":')

            elif p == 'O':
                n.PlayingMark = 'O'
                m.PlayingMark = 'X'
                print(m.Name,'!! Your choice will be "X":')
            else:
                while not (p == 'X' or p == 'O'):

                    p = input('\n You must pick between "X" or "O": ')



            p = Deck()  # creating object of the class Deck

            print(p.__str__())   # calling the function __str__ of the class Deck



            p.Board[0] = ' '
            p.Board[1] = ' '
            p.Board[2] = ' '
            p.Board[3] = ' '
            p.Board[4] = ' '
            p.Board[5] = ' '
            p.Board[6] = ' '
            p.Board[7] = ' '
            p.Board[8] = ' '



            game = '0'

            while game == '0':  # this will keep asking the user input unless the game is over

                game = self.get_user_input(self, n, m)  # calling the get_user_input function


            '''
            This is after the game is over, and it asks the user if continue to play or not
            If not it will print the Game Statistics
            '''

            print("\n \nPress 'Y' if you want to play the game again else press other key:  ")
            temp = input().upper()

            if (temp == 'Y'):
                repeat = 1

            else:
                repeat = 0



        a = input("\n\nPress anything for the Game Statistics..................")

        n.score = n.get_score()
        print(n.__str__())

        print("    ", n.won,"                   ",n.draw,"                     ",n.lost,"                       ",n.score)


        m.score = m.get_score()
        print(m.__str__())

        print("    ", m.won,"                   ",m.draw,"                     ",m.lost,"                       ",m.score)





c = TicTacToe  # creating the object of the class TicTacToe
b = TicTacToe  # creating the object of the class TicTacToe

c.start_game(b)  # calling the function start_game

