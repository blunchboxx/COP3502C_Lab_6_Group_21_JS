# Jason Schinis COP3502C Lab 06 Encode Function File

def print_menu():  # Function to print menu

    # Menu options
    print('Menu\n'
          '--------\n'
          '1. Encode\n'
          '2. Decode\n'
          '3. Quit\n')


def encode(original_password):  # Function to take user input password and encode it

    encoded_password = ''

    for char in original_password:  # Iterate through each character in input password

        char = int(char)  # Convert string user input character to integer

        new_char = char + 3  # Encode each character in password per assignment formula

        encoded_password += str(new_char)  # Add encoded character to new encoded password string

    return encoded_password


def main():  # Main program function definition

    while True:  # Loop to keep requesting user input until quit is selected

        print_menu()

        user_input_valid = False  # Set sentinel value for input validation loop to False

        while user_input_valid is False:  # Loop to check if user menu selection input is valid

            try:

                menu_selection = int(input("Please enter an option: "))
                user_input_valid = True  # If no error from user input, exit loop and continue program execution

            except ValueError as error:  # If input error occurs, display error message and request input again

                print('ValueError detected: ', str(error))

                print('Invalid selection. Please enter an integer between 1 and 3.\n')

        if menu_selection == 3:  # Option 3 exit branch

            break

        elif menu_selection == 1:  # Option 1 encode branch

            password_valid = False  # Set sentinel value for password input validation loop

            while password_valid is False:  # Loop to validate password input

                try:

                    unencrypted_password = input('Please enter your password to encode: ')

                    int(unencrypted_password)

                    password_valid = True  # If input password returns no errors, exit loop and continue program exec.

                except ValueError as excpt:  # If error occurs, display error message and request input again

                    print('ValueError detected: ', str(excpt))

                    print('Invalid selection. Please enter a password with numbers only.\n')

            encrypted_password = encode(unencrypted_password)  # Call encode function, pass user input and store result

            print('Your password has been encoded and stored!\n')

        elif menu_selection == 2:  # Menu option 2 - Decode function - FIXME - Lewis, implement Decode here

            try:

                raise NotImplementedError

            except NotImplementedError as error:

                print("Decode function not implemented yet.\n")


if __name__ == '__main__':  # Main Program

    main()
