
from tkinter import *
from tkinter import messagebox
import random


def start():
    global root
    global start_button, start_game1,start_game2
    root = Tk()
    root.title('War - Card Game')
    canvas = Canvas(root, height=600, width=600, bg='darkgreen')
    canvas.grid(columnspan=5, rowspan=5)
    start_game1 = Label(root, text='WAR', fg='white', bg='darkgreen',font=("Helvetica",50,"bold"))
    start_game2 = Label(root, text='CARD GAME', fg='white', bg='darkgreen', font=("Helvetica",50,"bold"))
    start_game1.grid(row=0, column=2)
    start_game2.grid(row=1, column=2)
    start_button = Button(root, text="Start",command=register,font=("Helvetica",20,"bold"),justify='center')
    start_button.grid(column=2, row=2)

    root.mainloop()

def register():
    global root, enter, player1, player2, PLAYER1, PLAYER2
    global start_game1, start_game2, start_button

    start_button.grid_remove()
    start_game1.grid_remove()
    start_game2.grid_remove()
    
    PLAYER1 = Label(root, text='Player 1:', bg='darkgreen')
    PLAYER1.grid(column=1, row=1)
    p1name= StringVar()
    player1 = Entry(root, textvariable=p1name)
    player1.grid(column=2, row=1)

    PLAYER2 = Label(root, text='Player 2:', bg='darkgreen')
    PLAYER2.grid(column=1, row=2)   
    p2name = StringVar()
    player2 = Entry(root, textvariable=p2name)
    player2.grid(column=2, row=2)

    #player1.pack()
    #player2.pack()

    enter = Button(root, text="Enter", command=play)
    enter.grid(column=2, row=3)
    #enter.pack()

def play():
    global root, enter, player1, player2, p1_pic, p2_pic, p1score, p2score
    global deck, p1_label, p2_label, PLAYER1, PLAYER2, count
    global p1score_label, p2score_label

    p1score = 0
    p2score = 0
    count = 0

    enter.grid_remove()
    player1.grid_remove()
    player2.grid_remove()
    PLAYER1.grid_remove()
    PLAYER2.grid_remove()
    
    card_ready()

    p1_label = Label(root, text=player1.get(), bg='darkgreen')
    p1_label.grid(row=3, column=1)

    p2_label = Label(root, text=player2.get(), bg='darkgreen')
    p2_label.grid(row=3, column=3)

    deck_pic = PhotoImage(file='./cards/d.png')
    deck_img = resize(deck_pic)

    deck_button = Button(root, image=deck_img, command=shuffle)
    deck_button.image = deck_img
    deck_button.grid(row=0, column=2)

    p1score_label = Label(root,text=str(p1score), bg='darkgreen')
    p1score_label.grid(row=4, column=3)        
    p2score_label = Label(root,text=str(p2score), bg='darkgreen')
    p2score_label.grid(row=4, column=1)    

def card_ready():
    global deck, root

    deck = []
        
    suits = ['hearts', 'spades', 'diamonds', 'clubs']
    
    values = [None, None, '2' ,'3','4', '5', '6', '7', 
                    '8', '9', '10', 'jack', 'queen', 'king','ace']
    
    for suit in suits:
        for value in values:
            if value != None:
                deck.append(f'{value}_of_{suit}')
    root.title(f'War - Card Game   {len(deck)} Cards Left')

def shuffle():
    global deck,root, count, p1score, p2score
    global p1, p2, p1_label, p2_label, playagain, player1, player2
    global img1_label, img2_label, p1score_label, p2score_label
    
#    p1_label.grid_remove()
#    p2_label.grid_remove()
    p1 = []
    p2 = []

    try:
        if count != 0 and len(deck) != 0:
            img1_label.grid_remove()
            img2_label.grid_remove()
            p1score_label.grid_remove()
            p2score_label.grid_remove()
        
        card = random.choice(deck)
        deck.remove(card)
        p1.append(card)
        get_p1card(card)

        card = random.choice(deck)
        deck.remove(card)
        p2.append(card)
        get_p2card(card)
        if compare(p1[0], p2[0]) == True:
            p1score += 1
        else:
            p2score += 1

        p1score_label = Label(root,text=str(p1score), bg='darkgreen')
        p1score_label.grid(row=4, column=3)        
        p2score_label = Label(root,text=str(p2score), bg='darkgreen')
        p2score_label.grid(row=4, column=1)

        count += 1

        root.title(f'War - Card Game   {len(deck)} Cards Left')
    except:
        root.title('War - Card Game   No Cards Left')
        if p1score > p2score:
            msg = messagebox.showwarning(f"Game Over - {player1.get()} Wins", "No more cards left in the deck")
        elif p1score < p2score:
            msg = messagebox.showwarning(f"Game Over - {player2.get()} Wins", "No more cards left in the deck")
        else:
            msg = messagebox.showwarning("Game Over - It's a TIE", "No more cards left in the deck")
        playagain = Button(root, text="Play Again", command=play_again)
        playagain.grid(row=4, column=2)        

def get_p1card(card):
    global root, p1_label, img1_label, p1_pic

    img = PhotoImage(file=f'cards/{card}.png')
    img = resize(img)

    img1_label = Label(root, image=img, bg='darkgreen')
    img1_label.image = img
    img1_label.grid(row=2,column=1)

    p1_label = Label(root, text=player1.get(), bg='darkgreen')
    p1_label.grid(row=3, column=1)

def get_p2card(card):
    global root, p2_label, img2_label, p2_pic

    img = PhotoImage(file=f'cards/{card}.png')
    img = resize(img)

    img2_label = Label(root, image=img, bg='darkgreen')
    img2_label.image = img
    img2_label.grid(row=2,column=3)

    p2_label = Label(root, text=player2.get(), bg='darkgreen')
    p2_label.grid(row=3, column=3)

def resize(pic):
    apic = pic.subsample(4)
    return apic

def compare(card1, card2):
    suitrank = ['hearts', 'spades', 'diamonds', 'clubs']

# Define value 
    if 'jack' in card1:
        card_1 = 11
    elif 'queen' in card1:
        card_1 = 12
    elif 'king' in card1:
        card_1 = 13
    elif 'ace' in card1:
        card_1 = 14
    else:
        card_1 = int(card1.split("_", 1)[0])

    if 'jack' in card2:
        card_2 = 11
    elif 'queen' in card2:
        card_2 = 12
    elif 'king' in card2:
        card_2 = 13
    elif 'ace' in card2:
        card_2 = 14
    else:
        card_2 = int(card2.split("_", 1)[0])
    #print(card_1, card_2)

    if 'hearts' in card1:
        card1suit = suitrank.index('hearts')
    elif 'spades' in card1:
        card1suit = suitrank.index('spades')
    elif 'diamonds' in card1:
        card1suit = suitrank.index('diamonds')
    elif 'clubs' in card1:
        card1suit = suitrank.index('clubs')

    if 'hearts' in card2:
        card2suit = suitrank.index('hearts')
    elif 'spades' in card2:
        card2suit = suitrank.index('spades')
    elif 'diamonds' in card2:
        card2suit = suitrank.index('diamonds')
    elif 'clubs' in card2:
        card2suit = suitrank.index('clubs')
    #print(card1suit)
    
    #Compare Cards
    if card_1 > card_2:
        return True
    elif card_1 == card_2:
        if card1suit > card2suit:
            return True
        else:
            return False
    else:
        return False



def play_again():
    global root, playagain, img1_label, img2_label, p1_pic, p2_pic

    img1_label.grid_remove()
    img2_label.grid_remove()
    playagain.grid_remove()

    play()

start()
