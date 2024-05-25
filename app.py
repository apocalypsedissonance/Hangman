import tkinter as tk
from tkinter import *
import random
import os
from urllib.request import Request, urlopen
from tkinter import font
from tkinter import Text


url="https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')
words = webpage.split()
words = [x for x in words if len(x) > 4 and not x[0].isupper() and "'" not in x]

class Game:

    def __init__(self):

        self.window = Tk()
        self.mistakes = 0
        self.window.geometry('750x485')
        self.window.title("Hangman Game")
        self.theword = random.choice(words)
        self.canvas = (tk.Canvas(self.window, width=305, height=485))
        self.canvas.place(relx=0, rely=.0)
        self.bkgd = PhotoImage(file = os.path.join(os.getcwd(),'HangmanImages', 'HangmanThingy.png'))
        self.canvas.create_image(150,243, image=self.bkgd)

        self.fontSize = font.Font(size=20)
        self.mistext = ("Mistakes left: " + str(6 - self.mistakes))
        self.mistakesLeft = (Label(master=self.window, font= self.fontSize, text= self.mistext))
        self.mistakesLeft.place(relx=.7,rely=.9)
        self.letters = []
        for x in self.theword:
            self.letters.append("_ ")
        self.wordyword = ''.join(self.letters)
        self.word_shown = (Label(master= self.window, text=self.wordyword, font= self.fontSize))
        self.word_shown.place(relx=.45,rely=.3)
        self.guess = Text(master= self.window, height=1, width=3, font=self.fontSize)
        self.guess.place(relx=.9, rely=.3)

        self.guessbutton = Button(master= self.window, width=5, height=1, text="guess", font=font.Font(size=15, family=("Times New Roman")), command= lambda:self.click())
        self.guessbutton.place(relx=.89, rely=.4)
        self.guesslabel =Label(self.window, text="Guesses will appear here!", font=font.Font(size=13))
        self.guesslabel.place(relx=.5,rely=.8)
        self.guesses =[]
        self.window.mainloop()

    def mistake(self):
        if 6 == self.mistakes:
            self.kill()
            self.gameover(winlose = 0)

        if self.mistakes <=6:
            self.mistext = ("Mistakes left: " + str(5 - self.mistakes))
            self.mistakesLeft.config(text=self.mistext)
            self.mistakes+=1

        if self.mistakes == 1:
            self.addhead()
        if self.mistakes==2:
            self.addtorso()
        if self.mistakes==3:
            self.addl_arm()
        if self.mistakes==4:
            self.addr_arm()
        if self.mistakes==5:
            self.addl_leg()
        if self.mistakes==6:
            self.addr_leg()

    def click(self):
        letter = self.guess.get('1.0').strip()
        if len(letter) > 0:
            self.guess.delete('1.0', END)
            self.find(letter = letter)
            self.guesses.append(letter)
            self.guesslabel.config(text=', '.join(self.guesses))

    def find(self, letter):
        match = 0
        where_we_at = 0
        for x in self.theword:
            if letter == x:
                self.letters[where_we_at] = (x+" ")
                match += 1
            where_we_at+=1


        self.wordyword = ''.join(self.letters)
        self.word_shown.config(text=self.wordyword)

        if not '_ ' in self.letters:
            self.gameover(winlose=1)

        if match == 0:
            self.mistake()

    def gameover(self, winlose):
        self.end = Tk()
        self.end.geometry('300x100')
        self.end.title("Game Over")
        if winlose==0:
            self.end.config(bg="red")
            endtxt = ("You Lose! The word was " + self.theword)
        if winlose==1:
            self.end.config(bg="green")
            endtxt= ("You Win! The word was " + self.theword)
        endlabel = Label(master=self.end, text = endtxt, font= self.fontSize).place(relx=.5, rely=.3, anchor=CENTER)
        again = Button(master=self.end,text="Play Again", font=self.fontSize, command=lambda: self.playagain())
        again.place(relx=.2, rely=.5)
        quit= Button(master=self.end, text = "Quit", font=self.fontSize, command= lambda: self.stop())
        quit.place(relx=.7, rely=.5)

    def stop(self):
        self.end.destroy()
        self.window.destroy()
    def playagain(self):
        self.window.destroy()
        self.end.destroy()
        new_game = Game()

    def addhead(self):
        self.head = PhotoImage(file=os.path.join(os.getcwd(), 'HangmanImages', 'NewestHangmanHead.png'))
        self.head = self.head.subsample(3, 3)
        self.thehead = self.canvas.create_image(200, 160, image=self.head)

    def addtorso(self):
        self.canvas.create_line(200,220,200,310, width=5)
    def addl_arm(self):
        self.canvas.create_line(200,220, 170,290, width=5)

    def addr_arm(self):
        self.canvas.create_line(200,220, 230, 290, width=5)

    def addl_leg(self):
        self.canvas.create_line(200,305,170,400, width=5)

    def addr_leg(self):
        self.canvas.create_line(200,305,230, 400, width=5)

    def kill(self):
        self.canvas.delete(self.thehead)
        self.canvas.create_oval(170,140,240,210,width=5, fill="RoyalBlue")
        self.canvas.create_line(185,160,200,180,width=4)
        self.canvas.create_line(200,160,185,180, width=4)
        self.canvas.create_line(215, 160, 230, 180, width=4)
        self.canvas.create_line(230, 160, 215, 180, width=4)
        self.canvas.create_oval(221,188,228,200, fill="Salmon")
        self.canvas.create_line(200,190,231,190, width=5)
        Label(self.window, text="bleh").place(relx=.15,rely=.3)

my_game = Game()