from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from random import choices
from time import strftime
import time
t=True
i=0
def music():
    root2.destroy()
    from tkinter import filedialog
    from pygame import mixer

    class MusicPlayer:
        def __init__(self, window):
            window.geometry('320x100')
            window.title('MANDY MUSIC PLAYER')
            window.resizable(0, 0)
            Load = Button(window, text='Load', width=10, font=('Times', 10), command=self.load)
            Play = Button(window, text='Play', width=10, font=('Times', 10), command=self.play)
            Pause = Button(window, text='Pause', width=10, font=('Times', 10), command=self.pause)
            Stop = Button(window, text='Stop', width=10, font=('Times', 10), command=self.stop)
            Load.place(x=0, y=20)
            Play.place(x=110, y=20)
            Pause.place(x=220, y=20)
            Stop.place(x=110, y=60)
            self.music_file = False
            self.playing_state = False

        def load(self):
            self.music_file = filedialog.askopenfilename()

        def play(self):
            if self.music_file:
                mixer.init()
                mixer.music.load(self.music_file)
                mixer.music.play()

        def pause(self):
            if not self.playing_state:
                mixer.music.pause()
                self.playing_state = True
            else:
                mixer.music.unpause()
                self.playing_state = False

        def stop(self):
            mixer.music.stop()

    root = Tk()
    app = MusicPlayer(root)
    root.mainloop()
def calc():
    root2.destroy()
    expression = ""

    def press(num):
        # point out the global expression variable
        global expression

        # concatenation of string
        expression = expression + str(num)

        # update the expression by using set method
        equation.set(expression)

    # Function to evaluate the final expression
    def equalpress():
        # Try and except statement is used
        # for handling the errors like zero
        # division error etc.

        # Put that code inside the try block
        # which may generate the error
        try:

            global expression

            # eval function evaluate the expression
            # and str function convert the result
            # into string
            total = str(eval(expression))

            equation.set(total)

            # initialize the expression variable
            # by empty string
            expression = ""

        # if error is generate then handle
        # by the except block
        except:

            equation.set(" error ")
            expression = ""

    # Function to clear the contents
    # of text entry box
    def clear():
        global expression
        expression = ""
        equation.set("")

    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("MANDY CALCULATOR")

    # set the configuration of GUI window
    gui.geometry("270x150")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                     command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                     command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                     command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                     command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                     command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                     command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                     command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                     command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                     command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                     command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='red',
                  command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='red',
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='red',
                      command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='red',
                   command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='red',
                   command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

    Decimal = Button(gui, text='.', fg='black', bg='red',
                     command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()
def news():
    import requests
    import json
    from win32com.client import Dispatch
    s = Dispatch("SAPI.spvoice")
    r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=f0f38dd7c2064d5d9d2ff75651948664")
    g = r.text
    m = json.loads(g)
    l = m["articles"]
    root3 = Tk()
    root3.geometry("400x650")
    root3.title("TODAY'S NEWS ARE")
    var = StringVar()
    y = Label(root3, textvariable=var)
    y.pack(side="top", fill="x")
    scroll = Scrollbar(root3)
    scroll.pack(side="right", fill="y")
    textt = Text(root3, yscrollcommand=scroll.set)
    textt.pack(expand=True, fill="both")
    scroll.config(command=textt.yview)

    def press():
        for h in l:
            s.speak(h["title"])
        import threading
        threading.Thread(target=press).start()

    Button(root3, text="START", command=press).place(x=30, y=0)
    x = ""
    for h in l:
        x += h["title"]
        x += "\n"
        x += "."

    def every_100(text):
        final_text = ""
        for i in range(0, len(text)):
            final_text += text[i]
            if i % 100 == 0 and i != 0:
                final_text += "\n"
        return final_text

    textt.insert("10.0", f"~~{every_100(x)}")
    textt.update()
    root3.mainloop()
def browser():
    root2.destroy()
    import webbrowser
    from tkinter import ttk
    def search_term():
        if (var2.get() == 1):
            webbrowser.open("https://www.google.com/search?q=" + Term.get(), new=2)
        if (var3.get() == 1):
            webbrowser.open("https://www.youtube.com/results?search_query=" + Term.get(), new=2)
        if (var4.get() == 1):
            webbrowser.open("https://www.imdb.com/find?ref_=nv_sr_fn&q=" + Term.get() + "&s=all", new=2)

    rootm = Tk()
    rootm.resizable(False, False)
    rootm.title("MANDY BROWSER")

    Term = StringVar(rootm, value="")
    Term_entry = ttk.Entry(rootm, textvariable=Term, width=50)
    Term_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W + E)
    Term_entry.focus()

    submit_button = ttk.Button(rootm, text="Submit", command=search_term)
    submit_button.grid(row=0, column=2, padx=9, sticky=W + E)

    check = Frame(rootm).grid(row=0, column=0, columnspan=3)

    var2 = IntVar(rootm, value=0)
    Checkbutton(check, text="Google", variable=var2).grid(row=0, column=4)

    var3 = IntVar(rootm, value=0)
    Checkbutton(check, text="Youtube", variable=var3).grid(row=0, column=5)

    var4 = IntVar(rootm, value=0)
    Checkbutton(check, text="IMDB", variable=var4).grid(row=0, column=6, padx=(0, 30))

    Term_entry.bind("<Return>", (lambda event: search_term()))

    rootm.mainloop()
def game():
    root2.destroy()
    import turtle
    import time
    import random

    delay = 0.1
    score = 0
    high_score = 0

    # Creating a window screen
    wn = turtle.Screen()
    wn.title("MANDY GAME")
    wn.bgcolor("blue")
    # the width and height can be put as user's choice
    wn.setup(width=600, height=600)
    wn.tracer(0)

    # head of the snake
    head = turtle.Turtle()
    head.shape("square")
    head.color("white")
    head.penup()
    head.goto(0, 0)
    head.direction = "Stop"

    # food in the game
    food = turtle.Turtle()
    colors = random.choice(['red', 'green', 'black'])
    shapes = random.choice(['square', 'triangle', 'circle'])
    food.speed(0)
    food.shape(shapes)
    food.color(colors)
    food.penup()
    food.goto(0, 100)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 250)
    pen.write("Score : 0  High Score : 0", align="center",
              font=("candara", 24, "bold"))

    # assigning key directions
    def goup():
        if head.direction != "down":
            head.direction = "up"

    def godown():
        if head.direction != "up":
            head.direction = "down"

    def goleft():
        if head.direction != "right":
            head.direction = "left"

    def goright():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    wn.listen()
    wn.onkeypress(goup, "w")
    wn.onkeypress(godown, "s")
    wn.onkeypress(goleft, "a")
    wn.onkeypress(goright, "d")

    segments = []

    # Main Gameplay
    while True:
        wn.update()
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
        if head.distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x, y)

            # Adding segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("orange")  # tail colour
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
        # Checking for head collisions with body segments
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        move()
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                colors = random.choice(['red', 'blue', 'green'])
                shapes = random.choice(['square', 'circle'])
                for segment in segments:
                    segment.goto(1000, 1000)
                segment.clear()

                score = 0
                delay = 0.1
                pen.clear()
                pen.write("Score : {} High Score : {} ".format(
                    score, high_score), align="center", font=("candara", 24, "bold"))
        time.sleep(delay)
    wn.mainloop()
def gallery():
    root2.destroy()
    from PIL import Image, ImageTk
    root = Tk()
    root.title("MANDY PHOTO VIEWER")
    root.geometry("400x650")
    root.maxsize(400, 650)
    root.minsize(400, 650)
    frame = Frame(root, width=400, height=400, bg='white', relief=GROOVE, bd=2)
    frame.pack(padx=10, pady=10)
    # create thumbanials of all images
    img1 = Image.open('b1.jpg')
    img1.thumbnail((550, 450))
    img2 = Image.open('b22.jpg')
    img2.thumbnail((550, 450))
    img3 = Image.open('b3.jpg')
    img3.thumbnail((550, 450))
    img4 = Image.open('b4.jpg')
    img4.thumbnail((550, 450))
    img5 = Image.open('b5.jpg')
    img5.thumbnail((550, 450))
    img6 = Image.open('b9.jpg')
    img6.thumbnail((550, 450))
    img7 = Image.open('b6.jpg')
    img7.thumbnail((550, 450))
    img8 = Image.open('b7.jpg')
    img8.thumbnail((550, 450))
    img9 = Image.open('b9.jpg')
    img9.thumbnail((550, 450))
    img10 = Image.open('b8.jpg')
    img10.thumbnail((550, 450))

    # open images to use with labels
    image1 = ImageTk.PhotoImage(img1)
    image2 = ImageTk.PhotoImage(img2)
    image3 = ImageTk.PhotoImage(img3)
    image4 = ImageTk.PhotoImage(img4)
    image5 = ImageTk.PhotoImage(img5)
    image6 = ImageTk.PhotoImage(img6)
    image7 = ImageTk.PhotoImage(img7)
    image8 = ImageTk.PhotoImage(img8)
    image9 = ImageTk.PhotoImage(img9)
    image10 = ImageTk.PhotoImage(img10)

    images = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10]
    # configure the image to the Label in frame
    image_label = Label(frame, image=images[i])
    image_label.pack()

    def previous():
        global i
        i = i - 1
        try:
            image_label.config(image=images[i])
        except:
            i = 0
            previous()

    def next():
        global i
        i = i + 1
        try:
            image_label.config(image=images[i])
        except:
            i = -1
            next()

    btn1 = Button(root, text="Previous", bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=previous)
    btn1.pack(side=LEFT, padx=60, pady=5)
    btn2 = Button(root, text="Next", width=8, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE,
                  command=next)
    btn2.pack(side=LEFT, padx=60, pady=5)
    btn3 = Button(root, text="Exit", width=8, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE,
                  command=root.destroy)
    btn3.pack(side=LEFT, padx=60, pady=5)
    root.mainloop()
def back():
    import tkinter.messagebox as tmsg
    t = tmsg.askquestion("TELL US", "DID YOU LIKE THE APP")
    if t == "yes":
        tmsg.showinfo("RATE", "PLEASE RATE US ON PLAYSTORE")
    else:
        tmsg.showinfo("ACCEPTED", "WE WILL TRY TO IMPROVE")
    root2.destroy()
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
def date():
    import datetime
    x=datetime.date.today()
    lbl2.config(text=x)

def check():
    global t
    if var.get()=="mayank"  or var.get()=="yukta" or var.get()=="MAYANK" or var.get()=="YUKTA":
        t=False
        root.destroy()
    else:
        root.destroy()
        import tkinter.messagebox as tksmg
        tksmg.showinfo("SORRY","YOU ARE NOT ALLOWED")
def about():
    import tkinter.messagebox as tksmg
    tksmg.showinfo("ABOUT","THE APP IS MADE BY MAYANK AND YUKTA")
def change():
    y=choices([bg2,bg,bg3,bg4,bg5,bg6,bg7,bg8,bg9])
    stvar.set("busy.....")
    label.update()
    canvas.create_image(0, 0, image=y, anchor="nw")
    import time
    time.sleep(3)
    canvas.update()
    stvar.set("ready")
def exitit():
    root.destroy()
root=Tk()
root.title("TECH EY")
root.geometry("400x650")
root.minsize(400,650)
root.maxsize(400,650)
root.iconbitmap("manku.ico")
#creating variables
var=StringVar()
var.set("hello")
stvar=StringVar()
stvar.set("READY")
#importing image
bg=ImageTk.PhotoImage(file="crop.jpg")
bg2=ImageTk.PhotoImage(file="bggm.jpg")
bg3=ImageTk.PhotoImage(file="bg3.jpg")
bg4=ImageTk.PhotoImage(file="bg4.jpg")
bg5=ImageTk.PhotoImage(file="bg5.jpg")
bg6=ImageTk.PhotoImage(file="bg6.jpg")
bg7=ImageTk.PhotoImage(file="bg7.jpg")
bg8=ImageTk.PhotoImage(file="bg8.jpg")
bg9=ImageTk.PhotoImage(file="bg9.jpg")
#creating canvas and adding image to it as background
canvas=Canvas(root,width=402,height=628)
canvas.create_image(0,0,image=bg3,anchor="nw")
canvas.pack()
style=ttk.Style()
style.configure("TEntry",foreground="green")
f2=Frame(root,bg="grey",borderwidth=12,relief=SUNKEN)
f2.place(x=70,y=90)
e=Label(f2,text="WHAT'S YOUR NAME ?",fg="RED",font="courier 16 bold")
e.pack()
entry=ttk.Entry(root,textvariable=var,font="courier 10 bold")
entry.place(x=120,y=150)
entry.focus_force()
Button(root,text="GET ME IN",command=check,bg="yellow",fg="blue",font="courier 10 bold").place(x=160,y=180)
Button(root,text="ABOUT",command=about,bg="grey",fg="blue",font="courier 10 bold").place(x=20,y=600)
Button(root,text="EXIT",command=exitit,bg="grey",fg="blue",font="courier 10 bold").place(x=320,y=600)
label=Label(root,textvariable=stvar,relief=SUNKEN,anchor="w")
label.pack(side="bottom",fill="x")
Button(root,text="CHANGE WALL PAPER",command=change,bg="grey",fg="black",font="courier 10 bold").place(x=145,y=450)
#CREATING A WATCH
lbl = Label(root, font=('calibri', 10, 'bold'),background='black',foreground='white')
lbl.place(x=220,y=300)
lbl2 = Label(root, font=('calibri', 10, 'bold'),background='black',foreground='white')
lbl2.place(x=120,y=300)
time()
date()
root.mainloop()
if t==False:
    root2 = Tk()
    root2.title("APPS")
    root2.geometry("400x650")
    root2.minsize(400, 650)
    root2.maxsize(400, 650)
    root2.iconbitmap("manku.ico")
    bg3 = ImageTk.PhotoImage(file="bg7.jpg")
    scroll = Scrollbar(root2,orient="horizontal")
    scroll.pack(side="bottom", fill="x")
    canvas2 = Canvas(root2, width=1000, height=1900,xscrollcommand=scroll.set)
    canvas2.create_image(0,0,image=bg3,anchor="nw")
    canvas2.pack()
    scroll.config(command=canvas2.xview)
    #creating buttons
    f1 = Frame(root2, bg="grey", borderwidth=12, relief=RAISED)
    f1.place(x=60,y=80)
    Button(f1,text="NEWS",command=news,bg="yellow",fg="blue",font="courier 10 bold",padx=15,pady=10).pack()
    f2 = Frame(root2, bg="grey", borderwidth=12, relief=SUNKEN)
    f2.place(x=250, y=80)
    Button(f2, text="MUSIC", command=music, bg="yellow", fg="blue", font="courier 10 bold", padx=15, pady=10).pack()
    f3 = Frame(root2, bg="grey", borderwidth=12, relief=SUNKEN)
    f3.place(x=60, y=210)
    Button(f3, text="CALCULATOR", command=calc, bg="yellow", fg="blue", font="courier 10 bold", padx=13, pady=10).pack()
    f4 = Frame(root2, bg="grey", borderwidth=12, relief=RAISED)
    f4.place(x=250, y=210)
    Button(f4, text="BROWSER", command=browser, bg="yellow", fg="blue", font="courier 10 bold", padx=7, pady=10).pack()
    f5 = Frame(root2, bg="grey", borderwidth=12, relief=SUNKEN)
    f5.place(x=60, y=340)
    Button(f5, text="GAME", command=game, bg="yellow", fg="blue", font="courier 10 bold", padx=15, pady=10).pack()
    f6 = Frame(root2, bg="grey", borderwidth=12, relief=SUNKEN)
    f6.place(x=250, y=340)
    Button(f6, text="GALLERY", command=gallery, bg="yellow", fg="blue", font="courier 10 bold", padx=10, pady=10).pack()
    f7 = Frame(root2, bg="grey", borderwidth=12, relief=RAISED)
    f7.place(x=160, y=470)
    Button(f7, text="LEAVE", command=back, bg="red", fg="black", font="courier 10 bold", padx=10, pady=10).pack()
    lbl = Label(root2, font=('calibri', 10, 'bold'), background='black', foreground='white')
    lbl.place(x=310, y=5)
    lbl2 = Label(root2, font=('calibri', 10, 'bold'), background='black', foreground='white')
    lbl2.place(x=230, y=5)
    date()
    time()
    root2.mainloop()
