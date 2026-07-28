class ChatBook:

    __user_id=0

    def __init__(self):
        self.id=ChatBook.__user_id
        ChatBook.__user_id+=1
        self.__name="Default User"
        self.user_id=0
        self.user_id+=1
        self.username=''
        self.password=''
        self.loggedIn=False
        # self.menu()
    @staticmethod
    def get_id():
        return ChatBook.__user_id

    @staticmethod
    def set_id(val):
        ChatBook.__user_id=val

    def get_name(self):
        return self.__name

    def set_name(self,value):
        self.__name=value


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
             self.my_post()
        elif user_input=="4":
            self.send_msg()
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

    def my_post(self):
        if self.loggedIn==True:
            txt=input("Write your post here:")
            print(f"Following post written here-> {txt}")
        else:
            print("You need to signin first for writing post")
        print("\n")
        self.menu()

    def send_msg(self):
        if self.loggedIn==True:
            msg=input("Enter your msg here:")
            frnd=input("Whom to send you msg")
            print(F"Your message sent to your {frnd}")
        else:
            print("You need to signin first to send message to your friend")
        print("\n")
        self.menu()

# obj=ChatBook()
