def print_menu(menu_choice_number, message_string):
    choice_is_valid = menu_choice_number in [1, 2, 3, 4]
    if not choice_is_valid:
        print("Invalid menu choice number.")
        return  
    print(f"You have selected option, {menu_choice_number}. {message_string}")


menu_is_running = True

volume = 5

while menu_is_running:
    menu_choice = input("Enter a choice (1-3, 4 to quit): ")

    message_string = "You have selected option "

    if menu_choice == '1':
        print_menu(int(menu_choice), "Settings")
    elif menu_choice == '2':
        print_menu(int(menu_choice), "Choose channel")
    elif menu_choice == '3':
        valid_volume = False
        while not valid_volume:
            print(f"Volume is {volume}")
            print_menu(int(menu_choice), "Change volume")
            new_volume = int(input("Enter new volume (0-100): "))
            if 0 <= new_volume <= 100:
                volume = new_volume
                print(f"Volume set to {volume}")
                valid_volume = True
            else:
                print("Volume must be between 0 and 100.")
                continue
    elif menu_choice == '4':
        print_menu(int(menu_choice), "Turning off TV")
        break
    else:
        print("Invalid choice, please try again.")
        continue
    
print("Exiting menu.")
