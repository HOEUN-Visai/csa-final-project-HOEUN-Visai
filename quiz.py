from questionary import questions, first_option, second_option, third_option, fourth_option, correct_answers
from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3
from login import *

# voice option
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

mixer.init()

# sound background
mixer.music.load('image/kbc.mp3')
mixer.music.play(-1)


def lifeline50():
    lifeline50Button.config(image=image50X, state=DISABLED)

    # Define question-to-option-button mappings
    question_to_options = {
        questions[0]: [optionButton1, optionButton3],
        questions[1]: [optionButton1, optionButton4],
        questions[2]: [optionButton3, optionButton4],
        questions[3]: [optionButton2, optionButton4],
        questions[4]: [optionButton1, optionButton4],
        questions[5]: [optionButton2, optionButton3],
        questions[6]: [optionButton3, optionButton4],
        questions[7]: [optionButton3, optionButton4],
        questions[8]: [optionButton2, optionButton4],
        questions[9]: [optionButton2, optionButton4],
        questions[10]: [optionButton2, optionButton3],
        questions[11]: [optionButton1, optionButton3],
        questions[12]: [optionButton1, optionButton2],
        questions[13]: [optionButton2, optionButton4],
        questions[14]: [optionButton1, optionButton3],
    }

    current_question = questionArea.get(1.0, 'end-1c')

    # Hide specific option buttons based on the current question
    if current_question in question_to_options:
        buttons_to_hide = question_to_options[current_question]
        for button in buttons_to_hide:
            button.config(text='')


def audiencePoleLifeline():
    audiencePoleButton.config(image=audiencePoleX, state=DISABLED)
    ProgressbarA.place(x=580, y=190)
    ProgressbarB.place(x=620, y=190)
    ProgressbarC.place(x=660, y=190)
    ProgressbarD.place(x=700, y=190)

    ProgressbarLabelA.place(x=580, y=320)
    ProgressbarLabelB.place(x=620, y=320)
    ProgressbarLabelC.place(x=660, y=320)
    ProgressbarLabelD.place(x=700, y=320)

    # help 2
    if questionArea.get(1.0, 'end-1c') == questions[0]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=60)
        ProgressbarD.config(value=90)
    if questionArea.get(1.0, 'end-1c') == questions[1]:
        ProgressbarA.config(value=20)
        ProgressbarB.config(value=95)
        ProgressbarC.config(value=70)
        ProgressbarD.config(value=50)
    if questionArea.get(1.0, 'end-1c') == questions[2]:
        ProgressbarA.config(value=85)
        ProgressbarB.config(value=90)
        ProgressbarC.config(value=40)
        ProgressbarD.config(value=60)
    if questionArea.get(1.0, 'end-1c') == questions[3]:
        ProgressbarA.config(value=90)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=70)
        ProgressbarD.config(value=20)
    if questionArea.get(1.0, 'end-1c') == questions[4]:
        ProgressbarA.config(value=20)
        ProgressbarB.config(value=70)
        ProgressbarC.config(value=95)
        ProgressbarD.config(value=60)
    if questionArea.get(1.0, 'end-1c') == questions[5]:
        ProgressbarA.config(value=95)
        ProgressbarB.config(value=40)
        ProgressbarC.config(value=20)
        ProgressbarD.config(value=70)
    if questionArea.get(1.0, 'end-1c') == questions[6]:
        ProgressbarA.config(value=100)
        ProgressbarB.config(value=80)
        ProgressbarC.config(value=10)
        ProgressbarD.config(value=20)
    if questionArea.get(1.0, 'end-1c') == questions[7]:
        ProgressbarA.config(value=40)
        ProgressbarB.config(value=90)
        ProgressbarC.config(value=20)
        ProgressbarD.config(value=50)
    if questionArea.get(1.0, 'end-1c') == questions[8]:
        ProgressbarA.config(value=50)
        ProgressbarB.config(value=30)
        ProgressbarC.config(value=100)
        ProgressbarD.config(value=80)
    if questionArea.get(1.0, 'end-1c') == questions[9]:
        ProgressbarA.config(value=70)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=30)
        ProgressbarD.config(value=20)
    if questionArea.get(1.0, 'end-1c') == questions[10]:
        ProgressbarA.config(value=80)
        ProgressbarB.config(value=40)
        ProgressbarC.config(value=50)
        ProgressbarD.config(value=60)
    if questionArea.get(1.0, 'end-1c') == questions[11]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=80)
        ProgressbarC.config(value=70)
        ProgressbarD.config(value=20)
    if questionArea.get(1.0, 'end-1c') == questions[12]:
        ProgressbarA.config(value=40)
        ProgressbarB.config(value=20)
        ProgressbarC.config(value=70)
        ProgressbarD.config(value=90)
    if questionArea.get(1.0, 'end-1c') == questions[13]:
        ProgressbarA.config(value=70)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=90)
        ProgressbarD.config(value=80)
    if questionArea.get(1.0, 'end-1c') == questions[14]:
        ProgressbarA.config(value=40)
        ProgressbarB.config(value=30)
        ProgressbarC.config(value=60)
        ProgressbarD.config(value=70)


def phoneLifeLine():  # select answer function
    mixer.music.load('image/calling.mp3')
    mixer.music.play()
    callButton.place(x=70, y=260)
    phoneLifeLineButton.config(image=phoneImageX, state=DISABLED)


def phoneClick():
    for i in range(15):
        if questionArea.get(1.0, 'end-1c') == questions[i]:
            engine.say(f'The answer is {correct_answers[i]}')
            engine.runAndWait()
            mixer.music.load('image/kbc.mp3')
            mixer.music.play(-1)


def select(event):
    # global timer_seconds, timer_running
    callButton.place_forget()

    ProgressbarA.place_forget()
    ProgressbarB.place_forget()
    ProgressbarC.place_forget()
    ProgressbarD.place_forget()

    ProgressbarLabelA.place_forget()
    ProgressbarLabelB.place_forget()
    ProgressbarLabelC.place_forget()
    ProgressbarLabelD.place_forget()

    b = event.widget
    value = b['text']
    for i in range(15):
        if value == correct_answers[14]:
            def close():
                root2.destroy()
                root.destroy()

            def playAgain():
                lifeline50Button.config(state=NORMAL, image=image50)
                audiencePoleButton.config(
                    state=NORMAL, image=audiencePole)
                phoneLifeLineButton.config(
                    state=NORMAL, image=phoneImage)

                root2.destroy()
                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[0])
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])

                amountLabel.config(image=amountImage)

                mixer.music.load('image/kbc.mp3')
                mixer.music.play(-1)

            mixer.music.stop()
            mixer.music.load('image/Kbcwon.mp3')
            mixer.music.play()

            root2 = Toplevel()
            root2.overrideredirect(True)
            root2.config(bg='black')
            root2.geometry('500x400+140+30')
            root2.title('You won 0 pounds')
            imgLabel = Label(root2, image=centerImage, bd=0)
            imgLabel.pack(pady=30)

            winLabel = Label(root2, text='You Won', font=(
                'arial', 40, 'bold'), bg='black', fg='white')
            winLabel.pack()
            # add try again button
            playAgainButton = Button(root2, text='Play Again', font=(
                'arial', 20, 'bold'), bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2', command=playAgain)
            playAgainButton.pack()
            # add close button
            closeButton = Button(root2, text='Close', font=(
                'arial', 20, 'bold'), bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2', command=close)
            closeButton.pack()

            # add sad image
            happyImage = PhotoImage(file='image/happy.png')
            happyLabel = Label(root2, image=happyImage, bg='black')
            happyLabel.place(x=30, y=280)

            happyLabel1 = Label(root2, image=happyImage, bg='black')
            happyLabel1.place(x=400, y=280)

            root2.mainloop()
            break

        if value == correct_answers[i]:
            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i+1])
            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourth_option[i+1])
            amountLabel.config(image=amountImages[i])

        if value not in correct_answers:
            def close1():
                root1.destroy()
                root.destroy()

            def tryAgain():
                lifeline50Button.config(state=NORMAL, image=image50)
                audiencePoleButton.config(
                    state=NORMAL, image=audiencePole)
                phoneLifeLineButton.config(
                    state=NORMAL, image=phoneImage)

                root1.destroy()
                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[0])
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])

                amountLabel.config(image=amountImage)

            root1 = Toplevel()
            root1.overrideredirect()
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title('You won 0 pounds')
            imgLabel = Label(root1, image=centerImage, bd=0)
            imgLabel.pack(pady=30)

            loseLabel = Label(root1, text='You Lose', font=(
                'arial', 40, 'bold'), bg='black', fg='white')
            loseLabel.pack()
            # add try again button
            tryAgainButton = Button(root1, text='Try Again', font=(
                'arial', 20, 'bold'), bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2', command=tryAgain)
            tryAgainButton.pack()
            # add close button
            closeButton = Button(root1, text='Close', font=(
                'arial', 20, 'bold'), bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2', command=close1)
            closeButton.pack()

            # add sad image
            sadImage = PhotoImage(file='image/sad.png')
            sadLabel = Label(root1, image=sadImage, bg='black')
            sadLabel.place(x=30, y=280)

            sadLabel1 = Label(root1, image=sadImage, bg='black')
            sadLabel1.place(x=400, y=280)

            root1.mainloop()
            break


root = Tk()
root.geometry('1270x652+0+0')
root.title('Code4U')

root.config(bg='black')

leftFrame = Frame(root, bg='black', padx=90)
leftFrame.grid(row=0, column=0)

topFrame = Frame(leftFrame, bg='black', pady=15)
topFrame.grid()

centerFrame = Frame(leftFrame, bg='black', pady=15)
centerFrame.grid(row=1, column=0)

bottomFrame = Frame(leftFrame)
bottomFrame.grid(row=2, column=0)

rightFrame = Frame(root, pady=25, padx=50, bg='black')
rightFrame.grid(row=0, column=1)

# add image
image50 = PhotoImage(file='image/50-50.png')
image50X = PhotoImage(file='image/50-50-X.png')
lifeline50Button = Button(topFrame, image=image50,
                          bg='black', bd=0, activebackground='black', width=180, height=80, command=lifeline50)
lifeline50Button.grid(row=0, column=0)

audiencePole = PhotoImage(file='image/audiencePole.png')
audiencePoleX = PhotoImage(file='image/audiencePoleX.png')
audiencePoleButton = Button(
    topFrame, image=audiencePole, bg='black', bd=0, activebackground='black', width=180, height=80, command=audiencePoleLifeline)
audiencePoleButton.grid(row=0, column=1)

phoneImage = PhotoImage(file='image/phoneAFriend.png')
phoneImageX = PhotoImage(file='image/phoneAFriendX.png')
phoneLifeLineButton = Button(
    topFrame, image=phoneImage, bg='black', bd=0, activebackground='black', width=180, height=80, command=phoneLifeLine)
phoneLifeLineButton.grid(row=0, column=2)

callImage = PhotoImage(file='image/phone.png')
callButton = Button(root, image=callImage, bd=0, bg='black',
                    activebackground='black',  cursor='hand2', command=phoneClick)

centerImage = PhotoImage(file='image/center.png')
logoLabel = Label(centerFrame, image=centerImage,
                  bg='black', width=300, height=200)
logoLabel.grid(row=0, column=0)

# add amount image on the right side
amountImage = PhotoImage(file='image/Picture0.png')
amountImage1 = PhotoImage(file='image/Picture1.png')
amountImage2 = PhotoImage(file='image/Picture2.png')
amountImage3 = PhotoImage(file='image/Picture3.png')
amountImage4 = PhotoImage(file='image/Picture4.png')
amountImage5 = PhotoImage(file='image/Picture5.png')
amountImage6 = PhotoImage(file='image/Picture6.png')
amountImage7 = PhotoImage(file='image/Picture7.png')
amountImage8 = PhotoImage(file='image/Picture8.png')
amountImage9 = PhotoImage(file='image/Picture9.png')
amountImage10 = PhotoImage(file='image/Picture10.png')
amountImage11 = PhotoImage(file='image/Picture11.png')
amountImage12 = PhotoImage(file='image/Picture12.png')
amountImage13 = PhotoImage(file='image/Picture13.png')
amountImage14 = PhotoImage(file='image/Picture14.png')
amountImage15 = PhotoImage(file='image/Picture15.png')

amountImages = [amountImage1, amountImage2,
                amountImage3, amountImage4, amountImage5, amountImage6, amountImage7, amountImage8, amountImage9, amountImage10, amountImage11, amountImage12, amountImage13, amountImage14, amountImage15]

amountLabel = Label(rightFrame, image=amountImage, bg='black')
amountLabel.grid(row=0, column=0)

# add choice layout
layoutImage = PhotoImage(file='image/lay.png')
layoutLabel = Label(bottomFrame, image=layoutImage, bg='black')
layoutLabel.grid(row=0, column=0)

# add text
questionArea = Text(bottomFrame, font=('arial', 16, 'bold'),
                    width=34, height=2, wrap='word', bg='black', fg='white', bd=0)
questionArea.place(x=70, y=10)

# insert text field
questionArea.insert(END, questions[0])
# option A
labelA = Label(bottomFrame, text="A:", bg='black',
               fg='white', font=('arial', 16, 'bold'))
labelA.place(x=60, y=110)

optionButton1 = Button(bottomFrame, text=first_option[0], font=(
    'arial', 18, 'bold'), bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButton1.place(x=100, y=100)

# option B
labelB = Label(bottomFrame, text="B:", bg='black',
               fg='white', font=('arial', 16, 'bold'))
labelB.place(x=330, y=110)

optionButton2 = Button(bottomFrame, text=second_option[0], font=(
    'arial', 18, 'bold'), bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButton2.place(x=370, y=100)

# option C
labelC = Label(bottomFrame, text="C:", bg='black',
               fg='white', font=('arial', 16, 'bold'))
labelC.place(x=60, y=190)

optionButton3 = Button(bottomFrame, text=third_option[0], font=(
    'arial', 18, 'bold'), bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButton3.place(x=100, y=180)

# option D
labelD = Label(bottomFrame, text="D:", bg='black',
               fg='white', font=('arial', 16, 'bold'))
labelD.place(x=330, y=190)

optionButton4 = Button(bottomFrame, text=fourth_option[0], font=(
    'arial', 18, 'bold'), bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButton4.place(x=370, y=180)

# help 2
ProgressbarA = Progressbar(root, orient=VERTICAL, length=120)
ProgressbarB = Progressbar(root, orient=VERTICAL, length=120)
ProgressbarC = Progressbar(root, orient=VERTICAL, length=120)
ProgressbarD = Progressbar(root, orient=VERTICAL, length=120)

ProgressbarLabelA = Label(root, text='A', font=(
    'arial', 20, 'bold'), bg='black', fg='white')
ProgressbarLabelB = Label(root, text='B', font=(
    'arial', 20, 'bold'), bg='black', fg='white')
ProgressbarLabelC = Label(root, text='C', font=(
    'arial', 20, 'bold'), bg='black', fg='white')
ProgressbarLabelD = Label(root, text='D', font=(
    'arial', 20, 'bold'), bg='black', fg='white')

# navigate option answer
optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)

root.mainloop()
root.destroy()
