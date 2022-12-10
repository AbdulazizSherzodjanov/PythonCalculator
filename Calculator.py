from tkinter import *  # tkinterni import qildik

oyna = Tk()  # oyna ochdik
oyna.title('Calculator')  # sarlavha
oyna.geometry('400x440')  # razmer
oyna.configure(bg='#00001A')  # orqa rangi


def tozalash():
    ekran.delete(0, END)


def nolr():
    ekran.insert(END, 0)


def birr():
    ekran.insert(END, 1)


def ikkir():
    ekran.insert(END, 2)


def uchr():
    ekran.insert(END, 3)


def tortr():
    ekran.insert(END, 4)


def beshr():
    ekran.insert(END, 5)


def oltir():
    ekran.insert(END, 6)


def yettir():
    ekran.insert(END, 7)


def sakkizr():
    ekran.insert(END, 8)


def toqqizr():
    ekran.insert(END, 9)


def bolish():
    try:
        if ekran.get()[-1] != '/' and ekran.get()[-1] != '*' and ekran.get()[-1] != '-' and ekran.get()[-1] != '+':
            ekran.insert(END, '/')
    except:
        pass


def kopaytirish():
    try:
        if ekran.get()[-1] != '*' and ekran.get()[-1] != '/' and ekran.get()[-1] != '-' and ekran.get()[-1] != '+':
            ekran.insert(END, '*')
    except:
        pass


def minusb():
    try:
        if ekran.get()[-1] != '-' and ekran.get()[-1] != '*' and ekran.get()[-1] != '/' and ekran.get()[-1] != '+':
            ekran.insert(END, '-')
    except:
        pass


def pulsb():
    try:
        if ekran.get()[-1] != '+' and ekran.get()[-1] != '*' and ekran.get()[-1] != '-' and ekran.get()[-1] != '+':
            ekran.insert(END, '+')
    except:
        pass


def nuqtab():
    if ekran.get() == '' and (
            ekran.get()[-1] != '.' and ekran.get()[-1] != '*' and ekran.get()[-1] != '-' and ekran.get()[-1] != '+'):
        ekran.insert(END, '0.')


    else:
        ekran.insert(END, '.')


def ekr():
    ekran.delete(0, END)
    ekran.configure(fg='black')
    teng.configure(bg='orange', state=NORMAL)


def tengb():
    try:
        misol = ekran.get()

        ekran.delete(0, END)

        n = eval(misol)
        n1 = str(n)
        if n1.endswith('.0'):
            n = int(n)
            ekran.insert(END, n)
        else:
            ekran.insert(END, n)
    except:
        ekran.delete(0, END)
        ekran.configure(fg='red')
        ekran.insert(END, 'Error')
        teng.configure(state=DISABLED, bg='silver')

        ekran.after(1500, ekr)


def birdel():
    try:
        ek = ekran.get()
        ekran.delete(0, END)
        ekran.insert(0, ek[:-1])
    except:
        pass


def plminb():
    try:
        if ekran.get()[0] != '-':
            ekran.insert(0, '-')
        else:
            ekran.delete(0, 1)
    except:
        pass


oyna.resizable(False, False)

ekran = Entry(oyna, bd=5, font=('Arial', 25), width=21, justify=RIGHT)
ekran.place(x=10, y=10)

ce = Button(text='Ce', font=('Arial', 20,), bg='peru', fg='white', width=4, command=tozalash)
ce.place(x=10, y=90)

c = Button(text='C', font=('Arial', 20,), bg='peru', fg='white', width=4, command=tozalash)
c.place(x=112, y=90)

tozala = Button(text='⏪', font=('Arial', 20,), bg='peru', fg='white', width=4, command=birdel)
tozala.place(x=214, y=90)

bolinma = Button(text='➗', font=('Arial', 20,), bg='orange', fg='white', width=4, command=bolish)
bolinma.place(x=316, y=90)

yetti = Button(text='7', font=('Arial', 20,), bg='white', fg='black', width=4, command=yettir)
yetti.place(x=10, y=160)

sakkiz = Button(text='8', font=('Arial', 20,), bg='white', fg='black', width=4, command=sakkizr)
sakkiz.place(x=112, y=160)

toqqiz = Button(text='9', font=('Arial', 20,), bg='white', fg='black', width=4, command=toqqizr)
toqqiz.place(x=214, y=160)

kopaytir = Button(text='✖', font=('Arial', 20,), bg='orange', fg='white', width=4, command=kopaytirish)
kopaytir.place(x=314, y=160)

tort = Button(text='4', font=('Arial', 20,), bg='white', fg='black', width=4, command=tortr)
tort.place(x=10, y=230)

besh = Button(text='5', font=('Arial', 20,), bg='white', fg='black', width=4, command=beshr)
besh.place(x=112, y=230)

olti = Button(text='6', font=('Arial', 20,), bg='white', fg='black', width=4, command=oltir)
olti.place(x=214, y=230)

minus = Button(text='➖', font=('Arial', 20,), bg='orange', fg='white', width=4, command=minusb)
minus.place(x=314, y=230)

bir = Button(text='1', font=('Arial', 20,), bg='white', fg='black', width=4, command=birr)
bir.place(x=10, y=300)

ikki = Button(text='2', font=('Arial', 20,), bg='white', fg='black', width=4, command=ikkir)
ikki.place(x=112, y=300)

uch = Button(text='3', font=('Arial', 20), bg='white', fg='black', width=4, command=uchr)
uch.place(x=214, y=300)

puls = Button(text='➕', font=('Arial', 20,), bg='orange', fg='white', width=4, command=pulsb)
puls.place(x=314, y=300)

nol = Button(text='0', font=('Arial', 20,), bg='white', fg='black', width=4, command=nolr)
nol.place(x=110, y=370)

teng = Button(text='=', font=('Arial', 20,), bg='orange', fg='white', width=4, command=tengb)
teng.place(x=214, y=370)

nuqta = Button(text='.', font=('Arial', 20,), bg='orange', fg='white', width=4, command=nuqtab)
nuqta.place(x=314, y=370)
pulsm = Button(text='±', font=('Arial', 20,), bg='orange', fg='white', width=4, command=plminb)
pulsm.place(x=13, y=370)

oyna.mainloop()
