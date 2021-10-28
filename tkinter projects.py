from tkinter import *
import random

# initialize window
root=Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Rock,Paper,Scissors")
root.config(bg="#D6EAF8")

# these are all the functions

# function to start the game
def play():
    user_pick=var1.get()
    if user_pick==comp_pick:
        Result.set("Tie , Both Selected The Same :)")
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')



# to reset everything
def Reset():
    Result.set("")
    var1.set("")


# to exit
def Exit():
    root.destroy()

Label(root,text="Rock, Paper, Scissors",font="Times 20 bold",bg="#AED6F1",fg="#154360",padx=80).pack()


# for user choice 

var1=StringVar()

Label(root,text="Choose any one :rock, paper, scissors",font="Times 16 bold",bg="#D6EAF8",fg="#154360").place(x=20,y=70)

Entry(root, font = 'Times 15', textvariable = var1 , bg = '#EBF5FB',fg="#154360").place(x=90 , y = 110)



# computer choice

comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

# defining buttons
Result=StringVar()

Entry(root, font = 'Times 10 bold', textvariable = Result, bg ='#EBF5FB',fg="#154360",width = 50,).place(x=25, y = 220)

Button(root, font = 'Times 13 bold', text = 'PLAY'  ,padx =5,bg ='#5499C7' ,command = play).place(x=155,y=310)

Button(root, font = 'Times 13 bold', text = 'RESET'  ,padx =5,bg ='#5499C7' ,command = Reset).place(x=70,y=310)

Button(root, font = 'Times 13 bold', text = 'EXIT'  ,padx =5,bg ='#E74C3C' ,command = Exit).place(x=230,y=310)

root.mainloop()




