from tkinter import * #importing tkinter
import mysql.connector #importing connector


class Tinder:
    def __init__(self):
        #connecting to the database
        self.conn = mysql.connector.connect(host="localhost", user="root", password='', database="tinderb1")
        self.mycursor = self.conn.cursor()
        self.current_user_id = 0
        self.rowno = 3

    def login(self):
        self.root = Tk()
        self.result = Label(self.root)
        self.result.grid(row=5, column=1)
        self.root.title("Tinder Login")
        self.root.minsize(500, 500)
        #taking user inputs
        Label(self.root, text="WELCOME TO TINDER!",justify=LEFT,  font=('lato',15)).grid(row=0, column=0)
        Label(self.root, text="Enter Email: ", font=('lato',12)).grid(row=1, column=0)
        self.emailInput = Entry(self.root)
        self.emailInput.grid(row=1, column=1)
        Label(self.root, text="Enter Password: ", font=('lato',12)).grid(row=2, column=0)
        self.passwordInput = Entry(self.root)
        self.passwordInput.grid(row=2, column=1)
        Button(self.root, text="Login Here",font=('lato',12), command=lambda: self.validate()).grid(row=3, column=1)
        #for new users
        Label(self.root, text="Not a user? ",font=('lato',12)).grid(row=4, column=0)
        Button(self.root, text="Sign Up",font=('lato',12), command=lambda: self.reg_window()).grid(row=4, column=1)
        self.root.mainloop()  # for creating the window

    def validate(self):

        emailInput = self.emailInput.get()
        passwordInput = self.passwordInput.get()
        #checking if the user already exists
        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'
        AND `password` LIKE '{}' """.format(emailInput, passwordInput))
        user_info = self.mycursor.fetchall()
        if len(user_info) > 0:
            self.result.configure(text="Welcome, {}!".format(user_info[0][1]))
            print("Welcome")
            #sstoring the current user id for future use
            self.current_user_id=user_info[0][0]
            self.main_app()
        else:
            #checking if the user input is inncorrect
            self.result.configure(text="Incorrect Email/Password")
            print("Incorrect")

    def reg_window(self):

        self.root = Tk()
        self.root.title("Sign up")
        self.root.minsize(500,500)

        #asking for user details
        Label(self.root, text="FILL IN YOUR DETAILS", font=('lato', 15, 'bold')).grid(row=0, column=0)
        Label(self.root, text="Enter Email: ",font=('lato',12)).grid(row=1, column=0)
        self.email = Entry(self.root)
        self.email.grid(row=1, column=1)
        Label(self.root, text="Enter Name: ",font=('lato',12)).grid(row=2, column=0)
        self.name = Entry(self.root)
        self.name.grid(row=2, column=1)
        Label(self.root, text="Enter Password: ",font=('lato',12)).grid(row=3, column=0)
        self.password = Entry(self.root)
        self.password.grid(row=3, column=1)
        Label(self.root, text="Enter Age: ",font=('lato',12)).grid(row=4, column=0)
        self.age = Entry(self.root)
        self.age.grid(row=4, column=1)
        Label(self.root, text="Enter Gender: ",font=('lato',12)).grid(row=5, column=0)
        self.gender = Entry(self.root)
        self.gender.grid(row=5, column=1)
        Label(self.root, text="Enter City: ",font=('lato',12)).grid(row=6, column=0)
        self.city = Entry(self.root)
        self.city.grid(row=6, column=1)
        Button(self.root, text="Register",font=('lato',12), command=lambda: self.register()).grid(row=7, column=1)
        self.root.mainloop()

    def register(self):
        self.resultr = Label(self.root)
        self.resultr.grid(row=8, column=1)
        email =self.email.get()
        password = self.password.get()
        name = self.name.get()
        age = self.age.get()
        city = self.city.get()
        gender= self.gender.get()
        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'
                """.format(email))
        user_info = self.mycursor.fetchall()
        #checking if the user exists
        if len(user_info) > 0:
            self.resultr.configure(text="You're already registered please log in")
            print("Already Registered")
            self.current_user_id = user_info[0][0]
        else:
            # entering the data in the database
            self.mycursor.execute("""INSERT INTO `users` (`user_id`, `name`, `email`, 
                 `password`, `age`, `gender`, `city`) VALUES
                (NULL, '{}','{}', '{}', '{}', '{}','{}')""".format(name, email, password, age, gender, city))
            self.resultr.configure(text="Registration Successful!")
            print("Registration successful!")
            self.conn.commit()
        self.login()

    def main_app(self):

        self.root = Tk()
        self.resultd=Label(self.root)
        self.resultd.grid(row=0,column=0)
        #displaying the options the user has
        self.resultd.configure(text="YOUR OPTIONS",font=('lato',15,'bold'))
        self.result1 = Label(self.root)
        self.result1.grid(row=1, column=0)
        self.result2 = Label(self.root)
        self.result2.grid(row=2, column=0)
        self.result3 = Label(self.root)
        self.result3.grid(row=3, column=0)
        self.result4 = Label(self.root)
        self.result4.grid(row=4, column=0)
        self.root.title("Tinder")
        self.root.minsize(150, 300)
        self.root.maxsize(300, 300)
        self.result1.configure(text="Want to propose someone?",font=('lato',12))
        self.result2.configure(text="View your proposals",font=('lato',12))
        self.result3.configure(text="View who proposed you",font=('lato',12))
        self.result4.configure(text="View your matches!",font=('lato',12))
        Button(self.root, text="Yes",font=('lato',12), command=lambda: self.view_all_users()).grid(row=1, column=1)
        Button(self.root, text="Sure",font=('lato',12), command=lambda: self.view_proposals()).grid(row=2, column=1)
        Button(self.root, text="Definitely",font=('lato',12), command=lambda: self.view_proposed()).grid(row=3, column=1)
        Button(self.root, text="Excited? XD",font=('lato',12), command=lambda: self.view_matches()).grid(row=4, column=1)
        Button(self.root, text="Log out", font=('lato', 12), command=lambda: self.logout()).grid(row=6, column=0)
        Button(self.root, text="Browse", font=('lato', 12), command=lambda: self.main_app()).grid(row=6, column=1)
        self.root.mainloop()

    def view_all_users(self):

        self.root = Tk()
        self.root.title("All users")
        self.root.minsize(300, 300)
        self.result6 = Label(self.root)
        self.result6.grid(row=0,column=0)
        self.result6.configure(text="PEOPLE AROUND YOU",justify=LEFT, font=('lato',14,'bold'))
        #fetchinf all users details
        self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` NOT LIKE '{}'
                """.format(self.current_user_id))
        all_users = self.mycursor.fetchall()
        #displaying the details
        self.display(all_users,0,1,4,5,6)
        self.result8 = Label(self.root)
        self.result8.grid(row= self.rowno, column=1)
        self.result8.configure(text="Enter the person's user id whom you want to propose: ",font=('lato',12))
        self.juliet_id = Entry(self.root)
        self.juliet_id.grid(row= self.rowno, column=2)
        Button(self.root, text="Propose",font=('lato',12), command=lambda: self.propose()).grid(row= self.rowno, column=3)
        self.root.mainloop()


    def propose(self):
        juliet_id=self.juliet_id.get()
        self.mycursor.execute("""SELECT * FROM `proposals` p 
                        JOIN `users` u ON u.`user_id`=p.`juliet_id`
                         WHERE p.`romeo_id`='{}' AND u.`user_id`='{}'""".format(self.current_user_id, juliet_id))
        who_proposed = self.mycursor.fetchall()
        self.result7 = Label(self.root)
        self.result7.grid(row=self.rowno+1, column=2)
        #checking if already proposed the same person
        if len(who_proposed) == 0:
            self.mycursor.execute(
                """INSERT INTO `proposals` (`proposal_id`, `romeo_id`, `juliet_id`) VALUES (NULL, '{}', '{}')"""
                    .format(self.current_user_id, juliet_id))
            self.conn.commit()
            self.result7.configure(text="Proposal sent successfully! Fingers crossed!",font=('lato',12))
        else:
            self.result7.configure(text="You've sent a proposal already!",font=('lato',12))


    def view_proposals(self):

        self.root = Tk()
        self.root.title("Proposals Received")
        self.root.minsize(300, 300)
        #fetching details pf proposals
        self.mycursor.execute("""SELECT * FROM `proposals` p 
        JOIN `users` u ON u.`user_id`=p.`romeo_id`
        WHERE p.`juliet_id`='{}'""".format(self.current_user_id))
        who_proposed = self.mycursor.fetchall()
        self.result9=Label(self.root)
        self.result9.grid(row=0, column=0)
        if len(who_proposed)==0:
            self.result9.configure(text="Sorry, no one has proposed you yet :(",font=('lato',12))
            Button(self.root, text="Log out", font=('lato', 12), command=lambda: self.logout()).grid(row=2,
                                                                                                     column=0)
            Button(self.root, text="Browse", font=('lato', 12), command=lambda: self.main_app()).grid(
                row=2, column=1)
        else:
            self.result9.configure(text="PEOPLE WHO HAVE PROPOSED YOU",font=('lato',15,'bold'))
            self.display(who_proposed, 3, 4, 7, 8, 9)


    def view_proposed(self):
        self.root = Tk()
        self.root.title("Proposals Sent")
        self.root.minsize(300, 300)
        self.mycursor.execute("""SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p.`juliet_id`
                                 WHERE p.`romeo_id`='{}'""".format(self.current_user_id))
        #storing the details returned
        who_proposed = self.mycursor.fetchall()
        self.result10 = Label(self.root)
        self.result10.grid(row=0, column=0)
        if len(who_proposed) == 0:
            self.result10.configure(text="You haven't proposed anyone yet!",font=('lato',12))
            Button(self.root, text="Log out", font=('lato', 12), command=lambda: self.logout()).grid(row=2,
                                                                                                     column=0)
            Button(self.root, text="Browse", font=('lato', 12), command=lambda: self.main_app()).grid(
                row=2, column=1)
        else:
            self.result10.configure(text="PEOPLE WHOM YOU HAVE PROPOSED", font=('lato',15,'bold'))
            self.display(who_proposed, 3, 4, 7, 8, 9)

    def view_matches(self):

        self.root = Tk()
        self.root.title("MATCHES")
        self.root.minsize(300, 300)
        #fetching the matches
        self.mycursor.execute("""SELECT * FROM `proposals` p
         JOIN `users` u ON u.`user_id`=p.`juliet_id` WHERE p.`juliet_id` IN(SELECT `romeo_id` FROM `proposals` 
         WHERE `juliet_id` LIKE '{}') AND p.`romeo_id` LIKE '{}'""".format(self.current_user_id, self.current_user_id))
        who_proposed = self.mycursor.fetchall()
        self.result10 = Label(self.root)
        self.result10.grid(row=0, column=0)
        #checking if matches exist or not
        if len(who_proposed) == 0:
            self.result10.configure(text="Sorry, you haven't been matched with anyone yet :(", font=('lato',12))
            Button(self.root, text="Log out", font=('lato', 12), command=lambda: self.logout()).grid(row= 2,
                                                                                                     column=0)
            Button(self.root, text="Browse", font=('lato', 12), command=lambda: self.main_app()).grid(
                row=2, column=1)
        else:
            self.result10.configure(text="PEOPLE WHO HAVE GOT MATCHED WITH!", font=('lato',16,'bold'))
            self.display(who_proposed,3,4,7,8,9)

    def display(self, user_list,a,b,c,d,e):
        Label(self.root, text="USER_ID",font=('lato',14)).grid(row=2, column=1)
        Label(self.root, text="NAME",font=('lato',14)).grid(row=2, column=0)
        Label(self.root, text="AGE",font=('lato',14)).grid(row=2, column=2)
        Label(self.root, text="GENDER",font=('lato',14)).grid(row=2, column=3)
        Label(self.root, text="CITY",font=('lato',14)).grid(row=2, column=4)
        for i in user_list:
            Label(self.root, text=("|", i[a], "|"),font=('lato',12)).grid(row=self.rowno, column=1)
            Label(self.root, text=("|", i[b], "|"),font=('lato',12)).grid(row=self.rowno, column=0)
            Label(self.root, text=("|", i[c], "|"),font=('lato',12)).grid(row=self.rowno, column=2)
            Label(self.root, text=("|", i[d], "|"),font=('lato',12)).grid(row=self.rowno, column=3)
            Label(self.root, text=("|", i[e], "|"),font=('lato',12)).grid(row=self.rowno, column=4)
            self.rowno = self.rowno + 1
        Button(self.root, text="Log out",font=('lato',12), command=lambda: self.logout()).grid(row=self.rowno+2, column=0)
        Button(self.root, text="Browse",font=('lato',12), command=lambda: self.main_app()).grid(row=self.rowno+2, column=1)

    def logout(self):
        print("Logged out successfully")
        self.current_user_id=0;
        #maintaining continuity
        self.login()


obj = Tinder()
obj.login()

