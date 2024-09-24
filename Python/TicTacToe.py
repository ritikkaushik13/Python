from tkinter import *
import random
import mysql.connector
from tkinter import simpledialog
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database='tictac'
)
c = conn.cursor()
# c.execute("create database tictac")
# c.execute("create table scores(player1 varchar(20),p1score int,player2 varchar(20),p2score int)")


root = Tk()
root.title("Tic Tac Toe")
root.geometry("400x500")
player1 = simpledialog.askstring("Input", "Enter name of Player 1 (X):")
player2 = simpledialog.askstring("Input", "Enter name of Player 2 (O):")
players = ['X','O']
player = random.choice(players)
buttons = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
root.config(bg="skyblue")
if player == 'X':
    turn = Label(root, text=player1 + ' turn', font=("poppins", 14), fg="white", bg='#00364C')
    turn.pack(fill=BOTH, expand=1,padx=5,pady=5)
else:
    turn = Label(root, text=player2 + ' turn', font=("poppins", 14), fg="white", bg='#00364C')
    turn.pack(fill=BOTH, expand=1,padx=5,pady=5)

frame = Frame(root)
frame.pack()

def new_game():
    global player
    player = random.choice(players)
    for rows in range(3):
        for col in range(3):
            buttons[rows][col].config(text="",bg="#F0F0F0")

    if player == 'X':
        turn.config(text=player1+" turn")
    else:
        turn.config(text=player2 + " turn")




reset = Button(root, text="Reset", font=("poppins",7), height=3,width=8,command=new_game)
reset.pack(side="top",fill=BOTH, expand=1,padx=3,pady=3)

def check_winner():
    for rows in range(3):
        if buttons[rows][0]['text']== buttons[rows][1]['text']== buttons[rows][2]['text']!="":
            buttons[rows][0].config(bg='green')
            buttons[rows][1].config(bg='green')
            buttons[rows][2].config(bg='green')
            return True

    for col in range(3):
        if buttons[0][col]['text']==buttons[1][col]['text']==buttons[2][col]['text']!="":
            buttons[0][col].config(bg="green")
            buttons[1][col].config(bg="green")
            buttons[2][col].config(bg="green")
            return True

    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text']!="":
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True
    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text']!="":
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True
    elif empty_space() is False:
        for rows in range(3):
            for col in range(3):
                buttons[rows][col].config(bg='beige')
        return "Tie"
    else:
        return False

def empty_space():
    box=9
    for rows in range(3):
        for col in range(3):
            if buttons[rows][col]['text']!="":
                box-= 1

    if box==0:
        return False
    else:
        return True

def next_turn(rows,col):
    global player
    if buttons[rows][col]['text']=="" and check_winner() is False:
        if player=='X':
            buttons[rows][col].config(text='X')
            if check_winner() is False:
                player = "O"
                turn.config(text=player2 +" turn")
            elif check_winner() is True:
                turn.config(text=player1+ " Wins")
            elif check_winner() == "Tie":
                turn.config(text="Tie")
        else:
            buttons[rows][col].config(text='O')
            if check_winner() is False:
                player = "X"
                turn.config(text=player1 +" turn")
            elif check_winner() is True:
                turn.config(text=player2+ " Wins")
            elif check_winner() == "Tie":
                turn.config(text="Tie")

for rows in range(3):
    for col in range(3):
        buttons[rows][col] = Button(frame,text="",font=("poppins",13, "bold"),width=12,height=6, command= lambda row=rows,coll=col : next_turn(row,coll))
        buttons[rows][col].grid(row=rows,column=col)



root.mainloop()
conn.close()