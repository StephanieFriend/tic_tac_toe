import user_input

def restart():
    restart = input("Do want to play Again?(y/n)")
    if restart.lower() == "y": 
        user_input.game()
    else:
        print("Goodbye")
        exit()
    