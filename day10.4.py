from art import logo1
print(logo1)


def calc(operation_choice, x, y):
    if operation_choice == "+":
        return x + y
    elif operation_choice == "-":
        return x - y
    elif operation_choice == "*":
        return x * y
    elif operation_choice == "/":
        return x / y


def run():
    running = True
    while running:
        num = float(input("What's the first number: "))
        print("+\n-\n*\n/")
        operations_prompt = input("Pick an operation: ")
        operations = ["+", "-", "*", "/"]
        num_2 = float(input("What's the next number: "))
        if operations_prompt in operations:
            answer = calc(x=num, y=num_2, operation_choice=operations_prompt)
            print(f"{num} {operations_prompt} {num_2} = {answer}")

            still_on = True
            while still_on:
                storage = answer
                continuation_prompt = input(f"Type 'y' to continue calculating with {answer}, "
                                            f"or type 'n' to start a new calculation. ").lower()
                if continuation_prompt == "y":
                    extra_step = float(input("What's your next number: "))
                    operations_prompt_2 = input("Pick an operation: ")
                    result = calc(x=storage, y=extra_step, operation_choice=operations_prompt_2)
                    print(f"{storage} {operations_prompt_2} {extra_step} = {result}")
                    answer = result

                elif continuation_prompt == "n":
                    break


run()
