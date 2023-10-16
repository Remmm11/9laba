import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def openfile():
    try:
        text = open(r'C:\py\test.txt', 'r+')
        return text
    except FileNotFoundError:
        try:
            os.mkdir(r'C:\py')
            text = open(r'C:\py\test.txt', 'w')
            text.close()
            text = open(r'C:\py\test.txt', 'r+')
            return text
        except FileNotFoundError:
            text = open(r'C:\py\test.txt', 'r+')
            return text


def dismiss(win):
    win.grab_release()
    win.destroy()


class game:
    def __init__(self, main):
        self.account = {}
        self.main = main
        self.first_click = True
        self.login = ttk.Entry(width=30, justify='center')
        self.password = ttk.Entry(width=30, justify='center')
        self.txtl = Label(text='Логин', font='Arial 14 bold')
        self.txtp = Label(text='Пароль', font='Arial 14 bold')
        self.button_reg = ttk.Button(text='Зарегистрироваться', command=lambda: self.regist())
        self.txt = Label(text='Для игры введите ваш логин и пароль', font='Arial 14 bold')
        self.button_avt = ttk.Button(text='Авторизоваться', command=lambda: self.authorization())

        self.txt.place(x=180, y=70)
        self.txtl.place(x=230, y=120)
        self.txtp.place(x=230, y=150)
        self.login.place(x=310, y=123)
        self.password.place(x=310, y=153)
        self.button_avt.place(x=260, y=210)
        self.button_reg.place(x=360, y=210)

    def authorization(self):
        s_l = self.login.get()
        s_p = self.password.get()

        if len(s_l) == 0 or len(s_p) == 0:
            messagebox.showwarning(title='Ошибка', message='Поле заполнения пусто')

        else:
            file = openfile()
            a = file.readline()[:-1].split(' ')

            while True:
                if a != ['']:
                    self.account[a[0]] = a[1]
                    a = file.readline()[:-1].split(' ')
                else:
                    break

            f_reg = False
            f_p = True
            for i in self.account.items():
                l, p = i
                if s_l == l and s_p == p:
                    f_reg = True
                    break
                elif s_l == l and s_p != p:
                    f_p = False

            if f_reg:
                win = Toplevel()
                win.geometry('400x120+760+420')
                win.title('Успех')
                win.grab_set()
                win.protocol('WM_DELETE_WINDOW', lambda: dismiss(win))

                Label(win, text='Вы успешно авторизовались', font='Arial 14 bold').place(x=60, y=20)
                ttk.Button(win, text='Играть', command= lambda: self.play(win)).place(x=160,y=70)

                self.txt.place_forget()
                self.txtl.place_forget()
                self.txtp.place_forget()
                self.login.place_forget()
                self.password.place_forget()
                self.button_avt.place_forget()
                self.button_reg.place_forget()

            elif not f_p:
                messagebox.showwarning(title='Ошибка', message='Неверный пароль')
            else:
                messagebox.showwarning(title='Ошибка', message='Такого аккаунта не существует')

    def regist(self):
        def registrate():
            s_l = login.get()
            s_p = password.get()

            if len(s_l) == 0 or len(s_p) == 0:
                messagebox.showwarning(title='Ошибка', message='Поле заполнения пусто')
            else:
                file = openfile()
                a = file.readline()[:-1].split(' ')

                while True:
                    if a != ['']:
                        self.account[a[0]] = a[1]
                        a = file.readline()[:-1].split(' ')
                    else:
                        break

                f_reg = False

                for i in self.account.items():
                    l, p = i
                    if s_l == l:
                        f_reg = True

                if not f_reg:
                    file = openfile()
                    file.seek(0, os.SEEK_END)
                    file.write(f'{s_l} {s_p}\n')
                    file.close()

                    txt.place_forget()
                    txtl.place_forget()
                    txtp.place_forget()
                    login.place_forget()
                    password.place_forget()
                    button_reg.place_forget()

                    Label(win, text='Вы успешно зарегистрировались', font='Arial 14 bold').place(x=140, y=120)
                    win.after(2000, lambda: (win.destroy(), win.grab_release()))
                else:
                    messagebox.showwarning(title='Ошибка', message='Такой аккаунт уже существует')

        win = Toplevel()
        win.geometry('600x300+660+320')
        win.title('Регистрация')
        win.resizable(False, False)
        win.protocol('WM_DELETE_WINDOW', lambda: dismiss(win))
        win.grab_set()

        login = ttk.Entry(win, width=30, justify='center')
        password = ttk.Entry(win, width=30, justify='center')
        txtl = Label(win, text='Логин', font='Arial 14 bold')
        txtp = Label(win, text='Пароль', font='Arial 14 bold')
        txt = Label(win, text='Введите желаемые логин и пароль', font='Arial 14 bold')
        button_reg = ttk.Button(win, text='Зарегистрироваться', command=lambda: registrate())

        txt.place(x=135, y=70)
        txtl.place(x=170, y=120)
        txtp.place(x=170, y=150)
        login.place(x=250, y=123)
        password.place(x=250, y=153)
        button_reg.place(x=245, y=210)

    def play(self, window):
        window.destroy()
        BRD_ROWS = BRD_COLS = 8
        CELL_SZ = 100

        canvas = Canvas(self.main, width=CELL_SZ * BRD_ROWS, height=CELL_SZ * BRD_COLS)

        cell_colors = ['white', 'black']
        ci = 0  # color index

        for row in range(BRD_ROWS):
            for col in range(BRD_COLS):
                x1, y1 = col * CELL_SZ, row * CELL_SZ
                x2, y2 = col * CELL_SZ + CELL_SZ, row * CELL_SZ + CELL_SZ
                canvas.create_rectangle((x1, y1), (x2, y2), fill=cell_colors[ci])

                ci = not ci

            ci = not ci
        self.main.geometry('800x800+560+100')
        canvas.pack()


root = Tk()
root.title('Авторизация')
root.geometry('720x300+600+320')
root.resizable(False, False)

game(root)

root.mainloop()
