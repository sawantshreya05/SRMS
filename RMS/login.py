from  tkinter import *
from  PIL import ImageTk
from  tkinter import messagebox
import  sqlite3
import os
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        self.bg=ImageTk.PhotoImage(file="images/login.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0, y=0,relwidth=1, relheight=1)

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150, y=150, height=340, width=500)

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc = Label(Frame_login, text="Student Login Area", font=("goudy old style", 15, "bold"), fg="#d25d17", bg="white").place(x=90,y=100)

        lbl_email = Label(Frame_login, text="EMAIL ADDRESS", font=("goudy old style", 15, "bold"), fg="gray", bg="white").place(x=90, y=140)
        self.txt_email=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=90,y=170,width=350,height=35)

        lbl_pass = Label(Frame_login, text="PASSWORD", font=("goudy old style", 15, "bold"), fg="gray", bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        btn_reg=Button(Frame_login,text="Register new Account?",bd=0,bg="white",fg="#d77337",font=("times new roman",13),cursor="hand2",command=self.register_window).place(x=280,y=280)

        forget_btn=Button(Frame_login,text="Forget Password?",bg="white",fg="#d77337",cursor="hand2",bd=0,font=("times new roman",13)).place(x=90,y=280)
        Login_btn = Button(self.root,command=self.login_function, text="Login", fg="white", bg="#d77337", font=("times new roman", 20),cursor="hand2").place(x=300, y=470,width=180, height=40)

    def register_window(self):
        self.root.destroy()
        import register

    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_email.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_pass.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid UserName/Password",parent=self.root )

                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
root=Tk()
obj=Login(root)
root.mainloop()