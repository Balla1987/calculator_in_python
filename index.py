def controller():
    user_action = raw_input("Please enter a sign: + * - / !")
    first_number = int(raw_input("Please enter the first number!"))
    second_number = int(raw_input("Please enter the second number!"))

    if user_action == "+":
        result_1 = int(first_number) + int(second_number)
        print result_1
    elif user_action == "*":
        result_2 = int(first_number) * int(second_number)
        print result_2
    elif user_action == "-":
        result_3 = int(first_number) - int(second_number)
        print result_3
    elif user_action == "/":
        result_4 = int(first_number) % int(second_number)
        print result_4
    else:
        print "Not correct symbol!"

    while True:
        break_input = "no"
        user_answer = raw_input("Would you like an another action? Just press enter to continue or type no!")
        if user_answer.lower() == break_input:
            break
        else:
            controller()

controller()
