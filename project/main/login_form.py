from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pyodbc
from management_form import Plant

class LoginForm:
    def __init__(self, master):
        self.master = master
        master.title("Login")
        master.geometry("925x500+300+200")
        master.configure(bg="#fff")
        master.resizable(False, False)

        self.img = PhotoImage(file='project/img/login/login.png')
        self.hiden_icon = "project/img/login/hiden_icon.png"
        self.show_icon = "project/img/login/show_icon.png"
        self.custom_width = 25
        self.custom_height = 25

        Label(master, image=self.img, bg="white").place(x=50, y=50)

        self.frame = Frame(master, width=350, height=350, bg="white")
        self.frame.place(x=480, y=70)

        self.heading = Label(self.frame, text="Đăng Nhập", fg="#57a1f8", bg="white", font=("Roboto", 20, 'bold'))
        self.heading.place(x=100, y=5)

        self.user = Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Roboto", 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, "Username")
        self.user.bind("<FocusIn>", self.on_enter)
        self.user.bind("<FocusOut>", self.on_leave)

        Frame(self.frame, width=295, height=2, bg="black").place(x=25, y=107)

        self.hiden = self.resize_image(self.hiden_icon, self.custom_width, self.custom_height)
        self.show = self.resize_image(self.show_icon, self.custom_width, self.custom_height)

        self.psw = Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Roboto", 11))
        self.psw.place(x=30, y=150)
        self.psw.insert(0, "Passwork")
        self.psw.bind("<FocusIn>", self.on_enter_psw)
        self.psw.bind("<FocusOut>", self.on_leave_psw)

        self.show_hide_btn = Button(self.frame, image=self.hiden, bd=0, command=self.show_hide_pass, bg="white")
        self.show_hide_btn.place(x=295, y=145)

        Frame(self.frame, width=295, height=2, bg="black").place(x=25, y=177)

        Button(self.frame, width=39, pady=7, text="Đăng nhập", bg="#57a1f8", fg="white", border=0,command=self.login).place(x=35, y=204)

    def on_enter(self, e):
        self.user.delete(0, "end")

    def on_leave(self, e):
        name = self.user.get()
        if name == "":
            self.user.insert(0, 'Username')

    def on_enter_psw(self, e):
        self.psw.delete(0, "end")
        self.psw.config(show="*")

    def on_leave_psw(self, e):
        name = self.psw.get()
        if name == "":
            self.psw.insert(0, 'Passwork')
            self.psw.config(show="")

    def resize_image(self, image_path, width, height):
        original_image = Image.open(image_path)
        resized_image = original_image.resize((width, height))
        return ImageTk.PhotoImage(resized_image)

    def show_hide_pass(self):
        if self.psw["show"] == "":
            self.show_hide_btn.config(image=self.hiden)
            self.psw.config(show="*")
        else:
            self.show_hide_btn.config(image=self.show)
            self.psw.config(show="")
    def login(self):
        # Hàm đăng nhập
        username = self.user.get() 
        password = self.psw.get()

        # Kết nối cơ sở dữ liệu SQL Server
        try:
            conn = pyodbc.connect('DRIVER={SQL SERVER};'
                                  'SERVER=KASHI\KASHI;'
                                  'DATABASE=QuanLyTruyXuat;'
                                  )

            cursor = conn.cursor()

            # Kiểm tra đăng nhập
            cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
            row = cursor.fetchone()

            if row is not None:
                messagebox.showinfo("Thông báo", "Đăng nhập thành công!")               
                self.master.destroy()
                
                Plant.main()
            else:
                messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu.")

        except pyodbc.Error as e:
            messagebox.showerror("Lỗi", f"Lỗi kết nối cơ sở dữ liệu: {str(e)}")
    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = LoginForm(root)
    app.run()
