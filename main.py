class NLPApp:
    
    def __init__(self):
       self.__database = {}
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
            
    def __register(self):
        print('register')


    def __login(self):
        print('login')


obj=NLPApp()


        
    