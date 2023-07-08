# name=input("whats your name?")
# if name=="Harry":
    # print("Gryfindor")
# elif name=="Hermione":
    # print("Gryffindor")
# elif name=="Ron":
    # print("Gryfindor")
# elif name=="Draco":
    # print("who?")         

    #other approach to print
# name=input("whats your name?")
# if name=="Harry"or name=="Hermione" or name=="Ron":
#   print("Gryfindor")
# elif name=="Draco":
    # print("slytherin")
# else:
    # print("who?")     

    # other match case to print this statement
name=input("whats your name?")
match name: 
    case "Harry":
        print("gryflindor")
    case "Hermone":   
        print("gryffindor")
    case"Ron":
        print("gryffindor")
    case"Draco":
        print("slytherin") 
    case _:
        print("who?")     
        
      
    
         
