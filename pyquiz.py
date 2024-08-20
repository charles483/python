class QuizApp:
    def __init__(self) :
        self.username=""
    def startup(self):
        self.greeting()

        #TODO:ask the suer fro their name
        self.username = input("what is your name")
        print(f"welcome, {self.username}!")
        print()

    def greeting(self):
                print("__+==___===___+===___====___====_____==_++_+_==-+=--")
                print("__==__==__==__==Welcomee to my quiz app__===__==__==__==")
                print("__++__++__++__++__==__++__++__++====__++-")    
                print()

    def menu_header(self):
             print("------------------------------------------")
             print("Please make a selection")
             print("(m): Repeat this menu")
             print("(L): List quizes")
             print("(T):m Take quizes")
             print("(E:) Exit program")

    def menu_error(self):
           print("that is not a valid selection")
    def goodby(self):
        print("___++___+++=====____====_____====-__===___+++__++")
        print(f"Thanks for using my quiz ap, {self.username}")
        print("__++__++__++===---===___+++___===___===___===___+++_--+++---++")
    def menu(self):
           self.menu_header()

           selection=""
           while(True):
                 selection=input("selection?")

                 if len(selection)==0:
                       self.menu_error()
                       continue
                 selection=selection.capitalize()

                 if selection[0]=='E':
                       self.goodby()
                       break
                 elif selection[0]=='M':
                        self.menu_header()
                        continue
                 elif selection=='L':
                       print("\n Available quizes are:")
                       #TODO list the quizes
                       print("------------------------------------------------")
                       

                    
           
                  

    def run(self):
          self.startup()
          self.menu()

if  __name__ == "__main__":
      app=QuizApp()
      app.run()               
             
