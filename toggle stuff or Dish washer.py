#################
#Basic toggles and for loops
#J SANDERSON
#FEB 29 2024
#
#################

# Basic formant for a toggle switch and for loop


#function returns toggle state to console/shell
Chewy_hamburger = True

def toggle_state():
    if Chewy_hamburger: 
        print("THE BURGER IS TRUE!")
    else:
        print("THE BURGER IS FALSE!")
#Loop returns toggle state 60 times before exiting 
for x in range(60):
    print("Current loop: ", x)
    toggle_state()
    
#boolean toggle switch of current stale
Chewy_hamburger = not Chewy_hamburger
#final value of toggle state
toggle_state()