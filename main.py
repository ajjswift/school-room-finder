#School Room Finder - www.101computing.net/school-room-finder
print("+-------------------------+")
print("|                         |")
print("|    Room Finder v1.0     |")
print("|                         |")
print("+-------------------------+")
print()
code = input("Enter a room code:").title()

allowedRoomCodes = ['A', 'B', 'C', 'S']

if len(code)<=4:
    letter = code[0]
    if letter in allowedRoomCodes:
        number = int(code[1:])
        if letter == "S":
            print("This room is located in the 6th Form block.")

            if number < 20:
                print("It is on the ground floor.")
            else:
                print("It is on the first floor")
        else:
            print("This room is located in the " + letter + " block.")
            if number<100:
                print("It is on the ground floor.")
            elif number>=100 and number<200:
                print("It is on the first floor.")
            elif number>=200:
                print("It is on the second floor.")
    else:
        print("Invalid room code.")

                
else:
    rooms = {"Main Reception":"at the main entrance of the A block",
                "Staffroom":"on the top floor of the B block",
                "Sports Hall":"on the side of the B Block",
                "Dance Studio":"on the ground floor in the A Block",
                "Activity Studio":"on the ground floor in the A Block",
                "Coffee Bar": 'on the first floor of the C Block.'
                }

    if code in rooms:
        print("This room is located " + rooms[code])
    else:
        print("We cannot locate this room! Are you sure this is a valid room?")
