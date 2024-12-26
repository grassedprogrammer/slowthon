import shelve

a = input()
#with shelve.open("slowthon") as db:
#       db["files"] = [a]  
        
slowthon_run = False
#global vars
#gram stands for global ram / global random-access memory

gram = ""

#gint stands for global int / global integer

gint = 0

#gfloat stands for global float / global floating point

gfloat = 0.00

#gbool stands for global bool / global boolean

gbool = False

#glist stands for global list

glist = [] 

#mainloop

while True:
    #if statement that gatheres input from the user
    
    if slowthon_run == False:       
        gram = input(gint)
        if gram.lower == 'run':
            slowthon_run = True 
            continue
        else:
            glist.insert(-1, gram)


        
    #else statement that executes the code
    
    else:
        #execution loop
        while slowthon_run == True:
            #the code that executes the slowthon code
            print("bro")