def fizz_buzz(number):
    if number % 5==0 and number % 3==0:
        print("fizz_buzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)


fizz_buzz(5)