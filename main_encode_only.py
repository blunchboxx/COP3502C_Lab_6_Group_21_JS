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

    while True:

        print_menu()

        user_input_valid = False

        while user_input_valid is False:

            try:

                menu_selection = int(input("Please enter an option: "))
                user_input_valid = True

            except ValueError as error:

                print('ValueError detected: ', str(error))

                print('Invalid selection. Please enter an integer between 1 and 3.\n')

        if menu_selection == 3:  # Option 3 exit branch

            break

        elif menu_selection == 1:  # Option 1 encode branch

            password_valid = False

            while password_valid is False:

                try:

                    unencrypted_password = input('Please enter your password to encode: ')

                    int(unencrypted_password)

                    password_valid = True

                except ValueError as excpt:

                    print('ValueError detected: ', str(excpt))

                    print('Invalid selection. Please enter a password with numbers only.\n')

            encrypted_password = encode(unencrypted_password)

            print('Your password has been encoded and stored!\n')


if __name__ == '__main__':  # Main Program

    main()
