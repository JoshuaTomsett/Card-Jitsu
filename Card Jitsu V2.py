import tkinter as tk
import random
import csv

global number_of_cards
number_of_cards = 0

global player_win_list
player_win_list = []

global computer_win_list
computer_win_list = []


class Hand(object):

    def __init__(self,cardlist=[],namelist=[]):

        self.cardlist = list(cardlist)  ## cardlist contains all data
        self.namelist = list(namelist)  ## namelist contains only names

    def clearHand(self):
        self.cardlist = []

    def addCard(self,card):
        self.cardlist.append(card)
        self.namelist.append(card[2])

    def removeCard(self,index):
        del self.namelist[index]
        del self.cardlist[index]

    def displayHand(self):
        return self.namelist


class Deck(Hand):
    
    def __init__(self,):
        
        self.cardlist = []

    def removeCard(self,number):
        del self.cardlist[number]

    def getRandom(self):
        global number_of_cards
        number_test = len(deck.cardlist) - number_of_cards
        test = True
        while test is True:
            number = random.randint(0,38)
            if number < number_test:
                number_of_cards += 1
                test = False
                return self.cardlist[number]

    def add_Card_deck(self,card):
        self.cardlist.append(card)


class Card(object):

    def __init__(self,suit,value,name):

        self.suit = str(suit)
        self.value = int(value)
        self.name = str(name)
         
    def Name(self):
        return self.name

    def Value(self):
        return self.value

    def Suit(self):
        return self.suit

player_hand = Hand()
computer_hand = Hand()
deck = Deck()


def main():

    global number_of_cards
    number_of_cards = 0

    root = tk.Tk()
    root.geometry("1920x1080")
    root.attributes('-fullscreen', True)

    back_image = tk.PhotoImage(file="Images/background_new.gif")
    background = tk.Label(root,image = back_image)
    background.place(x=0,y=0)


    def help_func():
        global banner_down
        banner_down = True

        help_image = tk.PhotoImage(file="Images/rules.gif")
        help_banner = tk.Label(root,image=help_image)
        help_banner.photo = help_image
        help_banner.place(x=564,y=0)

        help_img = tk.PhotoImage(file="Images/question_mark.gif")
        help_button_2 = tk.Button(root,image=help_img,command = lambda : [help_func_2() , help_button_2.destroy() , help_banner.destroy()])
        help_button_2.photo = help_img
        help_button_2.place(x=891,y=441)

    def countdown(mode):
        
        if mode == "countdown":
            global counter
            counter = 21

            def count():
                global counter
                counter = counter - 1
                timer_label.config(text=str(counter))

                if counter == 0:
                    random_card = random.randint(0,4)

                    if random_card == 0:
                        display_player_1.invoke()

                    if random_card == 1:
                        display_player_2.invoke()

                    if random_card == 2:
                        display_player_3.invoke()

                    if random_card == 3:
                        display_player_4.invoke()

                    if random_card == 4:
                        display_player_5.invoke()

                else:
                    timer_label.after(1000, count)
            count()

        elif mode == "stop":
            timer_label.destroy()
            new_timer_label = tk.Label(root,text=str(counter),font=("Helvetica",50,"bold"),bg="#319d31",width=2)
            new_timer_label.place(x=920,y=730)

    def winning_images(user,suit):

        if user == "computer":

            if suit == "water":
                computer_img_1 = tk.PhotoImage(file="Images/water.gif")
                computer_image_1 = tk.Label(root,image=computer_img_1)
                computer_image_1.photo = computer_img_1
                computer_image_1.place(x=27,y=324)

            if suit == "fire":
                computer_img_2 = tk.PhotoImage(file="Images/fire.gif")
                computer_image_2 = tk.Label(root,image=computer_img_2)
                computer_image_2.photo = computer_img_2
                computer_image_2.place(x=27,y=485)

            if suit == "ice":
                computer_img_3 = tk.PhotoImage(file="Images/ice.gif")
                computer_image_3 = tk.Label(root,image=computer_img_3)
                computer_image_3.photo = computer_img_3
                computer_image_3.place(x=27,y=647)

        elif user == "player":

            if suit == "water":
                player_img_1 = tk.PhotoImage(file="Images/water.gif")
                player_image_1 = tk.Label(root,image=player_img_1)
                player_image_1.photo = player_img_1
                player_image_1.place(x=1830,y=327)

            if suit == "fire":
                player_img_2 = tk.PhotoImage(file="Images/fire.gif")
                player_image_2 = tk.Label(root,image=player_img_2)
                player_image_2.photo = player_img_2
                player_image_2.place(x=1830,y=488)

            if suit == "ice":
                player_img_3 = tk.PhotoImage(file="Images/ice.gif")
                player_image_3 = tk.Label(root,image=player_img_3)
                player_image_3.photo = player_img_3
                player_image_3.place(x=1830,y=649)


    def winner(play_card,comp_card):           ## if x is False the player wins

        computer_value = comp_card.Value()
        player_value = play_card.Value()

        if play_card.Suit() == "ice":                         ## player has ice
                if comp_card.Suit() == "ice":
                    if computer_value > player_value:
                        x = True

                    elif player_value > computer_value:
                        x = False
                    
                elif comp_card.Suit() == "fire":
                    x = True

                elif comp_card.Suit() == "water":
                    x = False

        elif play_card.Suit() == "fire":                      ## player has fire
            if comp_card.Suit() == "ice":
                x = False

            elif comp_card.Suit() == "fire":
                if computer_value > player_value:
                    x = True

                elif player_value > computer_value:
                    x = False

            elif comp_card.Suit() == "water":
                x = True

        elif play_card.Suit() == "water":                     ## player has water
            if comp_card.Suit() == "ice":
                x = True

            elif comp_card.Suit() == "fire":
                x = False

            elif comp_card.Suit() == "water":
                if computer_value > player_value:
                    x = True

                elif player_value > computer_value:
                    x = False

        if x == True:                                           ##  computer won
            if comp_card.Suit() in computer_win_list:
                pass

            else:
                computer_win_list.append(comp_card.Suit())
                winning_images("computer",comp_card.Suit())
            

        elif x == False:                                        ##  player won
            if play_card.Suit() in player_win_list:
                pass

            else:
                player_win_list.append(play_card.Suit())
                winning_images("player",play_card.Suit())

        if len(player_win_list) == 3:

            def win_delay():
                win_image = tk.PhotoImage(file="Images/winner.gif")
                win_label = tk.Label(root,image=win_image)
                win_label.photo = win_image
                win_label.place(x=448,y=103)

                quit_image = tk.PhotoImage(file="Images/win_quit.gif")
                quit_button = tk.Button(root,image=quit_image,command = lambda: root.destroy())
                quit_button.photo = quit_image
                quit_button.place(x=730,y=940)
            root.after(2000, win_delay)

        elif len(computer_win_list) == 3:

            def lose_delay():
                lose_image = tk.PhotoImage(file="Images/loser.gif")
                lose_label = tk.Label(root,image=lose_image)
                lose_label.photo = lose_image
                lose_label.place(x=448,y=103)

                quit_image = tk.PhotoImage(file="Images/lose_quit.gif")
                quit_button = tk.Button(root,image=quit_image,command = lambda: root.destroy())
                quit_button.photo = quit_image
                quit_button.place(x=730,y=940)
            root.after(2000, lose_delay)

        else:
            root.after(3000, lambda : [root.destroy(), main()])


    def display_card(chosen_card,image_name):

        # global banner_down
        # if banner_down == True:
        #     help_button_2.invoke()

        countdown("stop")
        display_player_1.config(state=tk.DISABLED)
        display_player_2.config(state=tk.DISABLED)
        display_player_3.config(state=tk.DISABLED)
        display_player_4.config(state=tk.DISABLED)
        display_player_5.config(state=tk.DISABLED)

        player_chosen_card = tk.Label(root,image=image_name)
        player_chosen_card.place(x=1438,y=384)
        player_index = player_hand.namelist.index(chosen_card)

        computer_card = computer_hand.namelist[random.randint(0,4)]
        computer_image = tk.PhotoImage(file="Cards/"+computer_card+".gif")
        computer_chosen_card = tk.Label(root,image=computer_image)
        computer_chosen_card.photo = computer_image
        computer_chosen_card.place(x=328,y=384)
        computer_index = computer_hand.namelist.index(computer_card)


        player_card_class = player_hand.cardlist[player_index]
        play_card = Card(str(player_card_class[0]),int(player_card_class[1]),str(player_card_class[2]))

        computer_card_class = computer_hand.cardlist[computer_index]
        comp_card = Card(str(computer_card_class[0]),int(computer_card_class[1]),str(computer_card_class[2]))

        computer_hand.removeCard(computer_hand.namelist.index(computer_card))       # remove computer card from hand
        player_hand.removeCard(player_hand.namelist.index(chosen_card))             # remove play card from hand

        winner(play_card,comp_card)
        

    ###################################################  Main ###################################################
    
    ##                                                  import cards and add to deck
    full_card_list = []
    deck.cardlist = []
    with open("Deck.csv", 'rt') as text_file:
        reader = csv.reader(text_file)
        full_card_list = list(reader)

    for i in full_card_list:
        deck.add_Card_deck(i)

    ##                                                  add 5 cards to computer hand
    computer_hand.cardlist = []
    computer_hand.namelist = []
    for i in range(0,5):
        newcard = deck.getRandom()
        computer_hand.addCard(newcard)
        deck.removeCard(deck.cardlist.index(newcard))
    ##                                                  add 5 cards to player hand
 
    player_hand.cardlist = []
    player_hand.namelist = []
    for i in range(0,5):
        newcard = deck.getRandom()
        player_hand.addCard(newcard)
        deck.removeCard(deck.cardlist.index(newcard))
    ##                                                  Display the players cards

    img1 = tk.PhotoImage(file="Cards/"+player_hand.namelist[0]+".gif")
    display_player_1 = tk.Button(root,image=img1,command=lambda: [display_card(player_hand.namelist[0],img1) , display_player_1.destroy()])
    display_player_1.place(x=846,y=882)

    img2 = tk.PhotoImage(file="Cards/"+player_hand.namelist[1]+".gif")
    display_player_2 = tk.Button(root,image=img2,command=lambda: [display_card(player_hand.namelist[1],img2) , display_player_2.destroy()])
    display_player_2.place(x=1027,y=882)

    img3 = tk.PhotoImage(file="Cards/"+player_hand.namelist[2]+".gif")
    display_player_3 = tk.Button(root,image=img3,command=lambda: [display_card(player_hand.namelist[2],img3) , display_player_3.destroy()])
    display_player_3.place(x=1208,y=882)

    img4 = tk.PhotoImage(file="Cards/"+player_hand.namelist[3]+".gif")
    display_player_4 = tk.Button(root,image=img4,command=lambda: [display_card(player_hand.namelist[3],img4) , display_player_4.destroy()])
    display_player_4.place(x=1389,y=882)

    img5 = tk.PhotoImage(file="Cards/"+player_hand.namelist[4]+".gif")
    display_player_5 = tk.Button(root,image=img5,command=lambda: [display_card(player_hand.namelist[4],img5) , display_player_5.destroy()])
    display_player_5.place(x=1570,y=882)

    ##                                                  Display won cards icons

    for suit in player_win_list:
        winning_images("player",suit)

    for suit in computer_win_list:
        winning_images("computer",suit)

    ##                                                      help button

    def help_func_2():
        global banner_down
        banner_down = False

        help_img = tk.PhotoImage(file="Images/question_mark.gif")
        help_button = tk.Button(root,image=help_img,command = lambda : [help_func() , help_button.destroy()])
        help_button.photo = help_img
        help_button.place(x=891,y=31)
    help_func_2()

    ##                                                          Timer

    timer_label = tk.Label(root,text="",font=("Helvetica",50,"bold"),bg="#319d31",width=2)
    timer_label.place(x=920,y=730)
    countdown("countdown")

    def exit_fullscreen(placeholder):
        root.attributes('-fullscreen', False)
        root.state('zoomed')
    root.bind('<Escape>',exit_fullscreen)

    def fullscreen(placeholder):
        root.attributes('-fullscreen', True)
    root.bind('<F11>',fullscreen)

    root.mainloop()

main()
