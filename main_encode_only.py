def print_menu():  # Function to print menu

    # Menu options
    print('Menu\n'
          '--------\n'
          '1. Encode\n'
          '2. Decode\n'
          '3. Quit\n')


def encode(original_password):  # Function to take user input password and encode it

    encoded_password = ''

    for char in original_password:

        char = int(char)

        new_char = char + 3

        encoded_password += str(new_char)

    return encoded_password


def main():  # Main program function definition

    while True:

        print_menu()

        try:

            menu_selection = int(input("Please enter an option: "))

        except:

            print('Invalid selection. Please enter an integer between 1 and 3.\n')

        if menu_selection == 3:  # Option 3 exit branch

            break

        elif menu_selection == 1:  # Option 1 encode branch

            unencrypted_password = input('Please enter your password to encode: ')

            encrypted_password = encode(unencrypted_password)

            print(encrypted_password)

            print('Your password has been encoded and stored!\n')

        elif menu_selection == 2:  # Option 2 decode branch

            unencrypted_password = decode(encrypted_password)

            print(f'The encoded password is {encrypted_password}, and the original password is {unencrypted_password}.\n')


if __name__ == '__main__':  # Main Program

    main()
