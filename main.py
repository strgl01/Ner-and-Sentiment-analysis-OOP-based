class NLPApp:
    __database = {}
    def __init__(self):
       self.__first_menu()

    def __first_menu(self):
        self.__first_input = input('''
         Hi! how would you like to proceed?
         1. Not a member? Register
         2. Already a member? Login
         3. By mistake? Exit
         ''')
        if self.__first_input=='1':
            self.__register()
        if self.__first_input=='2':
            self.__login()
        else:
            exit()

    def __second_menu(self):
        pass
            
    def __register(self):
        name=input('Enter name')
        email=input('Enter email')
        password=input('Enter password')
        if email in NLPApp.__database:
            print('email exist')
        else:
            NLPApp.__database[email]=[name,password]
            print('registration done.')
            print(NLPApp.__database)
            self.__login()

    def __login(self):
        email=input('enter email')
        password=input('enter password')
        if email in NLPApp.__database:
            if NLPApp.__database[email][1]==password:
                print('login successful')
                self.__second_menu()
            else:
                print('wrong password.Try again')
                self.__login()
        else:
            print('Not registered')


obj=NLPApp()


        
    
