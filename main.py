import nlpcloud

class NLPApp:
    __database = {}
    def __init__(self):
       self.__first_menu()

    def __first_menu(self):
        __first_input = input('''
         Hi! how would you like to proceed?
         1. Not a member? Register
         2. Already a member? Login
         3. By mistake? Exit
         ''')
        if __first_input=='1':
            self.__register()
        if __first_input=='2':
            self.__login()
        else:
            exit()

    def __second_menu(self):
        __second_input = input('''
         Hi! how would you like to proceed?
         1. NER
         2. Language Detection
         3. Sentiment Analysis
         4. Log Out
         ''')
        if __second_input=='1':
            self.__ner()
        if __second_input=='2':
            self.__language_detection()
        if __second_input=='3':
            self.__sentiment_analysis()
        else:
            self.__first_menu()
            
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
   
    def __ner(self):
        para=input('Enter paragraph')
        search_term=input('what would you like to search')
        client = nlpcloud.Client("finetuned-gpt-neox-20b", "2b58d7fb9af09e617ee525e78c7766b6d8c5bb61", gpu=True, lang="en")
        response=client.entities(para, searched_entity=search_term)
        print(response)
    
    def __sentiment_analysis(self):
        para=input('Enter paragraph')
        client = nlpcloud.Client("distilbert-base-uncased-emotion", "2b58d7fb9af09e617ee525e78c7766b6d8c5bb61", gpu=False, lang="en")
        response=client.sentiment(para)

    def __language_detection(self):
        pass
        
        
        


obj=NLPApp()


        
    
