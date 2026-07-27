class ChatBook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedIn=False
        self.menu()

    def menu(self):
        user_input=input("""Welcome to ChatBook ! how would you like to proceed
                   1. Press 1 to signup
                   2. Press 2 to signin
                   3. Press 3 to write a post
                   4. Press 4 to message a friend
                   5. Press any other key to exit
                    """)
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()

    def signup(self):
        email=input("enter you email here:")
        pswd=input("setup your password here:")
        self.username=email
        self.password=pswd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in main menu")
        else:
            uname=input("enter you email/username here:")
            pswd=input("enter your password:")
            if self.username==uname and self.password==pswd:
                print("You have signed in successfully !!")
                self.loggedIn=True
            else:
                print("Please input correct credentials")
        print("\n")
        self.menu()



obj=ChatBook()
