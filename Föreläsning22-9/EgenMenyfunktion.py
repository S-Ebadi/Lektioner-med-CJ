def print_menu(menu_choice_number, message_string):
    choice_is_valid = menu_choice_number in [1, 2, 3, 4]
    if not choice_is_valid:
        print("Invalid menu choice number.")
        return
    print(f"You have selected option {menu_choice_number}. {message_string}")

menu_is_running = True
volume = 5

while menu_is_running:
    menu_choice = input("Enter a choice (1-3, 4 to quit): ")

    if menu_choice == '1':
        print_menu(1, "Settings")
        user_input = input("Type 'exit' to return to main menu: ").lower()
        if user_input == 'exit':
            print("Returning to main menu...")
            continue

    elif menu_choice == '2':
        print_menu(2, "Choose channel")
        user_input = input("Type 'exit' to return to main menu: ").lower()
        if user_input == 'exit':
            print("Returning to main menu...")
            continue

    elif menu_choice == '3':
        print_menu(3, "Change volume")
        while True:
            print(f"Volume is {volume}")
            new_input = input("Enter new volume (0-100) or 'exit' to return: ").lower()
            if new_input == 'exit':
                print("Returning to main menu...")
                break
            try:
                new_volume = int(new_input)
                if 0 <= new_volume <= 100:
                    volume = new_volume
                    print(f"Volume set to {volume}")
                else:
                    print("Volume must be between 0 and 100.")
            except ValueError:
                print("Invalid input.")
                continue

    elif menu_choice == '4':
        print_menu(4, "Turning off TV")
        break

    else:
        print("Invalid choice, please try again.")

print("Exiting menu.")
