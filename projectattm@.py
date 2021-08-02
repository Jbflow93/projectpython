import random #any time i use random have to import first
def about_me():
    print("Hi, My name is Jabari\n Im from Chicago\n My favorite team are the Denver Nuggets") # \n helps space out your strings
    
def q():
    question1 = ["what state you live in?","How old are you?", "What is your favorite animal?"] #[] when making a list
    n = random.randrange(0,len(question1)) #--> random function 
    print(n) 
q()
    
    
ex_dict={} #{} when dealing with the dict

def Guestbook(ex_dict):ßå
    fname = (input("what is your first name"))
    lname = (input("what is your last name?"))
    Note2me =(input("Leave a Note"))
    ex_d={fname + lname:Note2me} #taking user input to put into a place holder dict. holds the value for the dict.
    print(ex_dict)
    ex_dict.update(ex_d) #.update is the function to update to dict
    # print(fname + lname)
    # ex_d = {fname}


# i=0
# while i < 2:
#     Guestbook(ex_dict)
#     i+=1

def ran(): 
    

    n =random.randrange(0,2)
    if n == 0: # ==  comparing variables while = assigns the variable
        print("I believe i can Fly")
    if n == 1: 
        print("You Can Do It")
    if n == 2:
        print("Having fun isnt hard when you got a library card")
ran()

i=""
while i != "goodbye": 
    i = input("""Hi my name is ___ ,\n
Enter "about" to learn more about me\n
Enter "q&a" to ask me a question\n
Enter "guestbook" to get added to my guestbook\n
Enter "random" for something random\n
Enter "goodbye" to say goodbye!""")




    

    
