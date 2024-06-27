def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    celsius = int(input())

    c = celsius

    fahrenheit = 9 / 5 * c + 32

    print (f'Fahrenheit: \t {fahrenheit: .2f}')

    return celsius, fahrenheit


if __name__ == '__main__':
    main()
