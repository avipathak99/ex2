import arithmetic

operator_dict = {
    "+" : arithmetic.add,
    "-" : arithmetic.subtract,
    "*" : arithmetic.multiply,
    "/" : arithmetic.divide,
    "square": arithmetic.square,
    "cube": arithmetic.cube,
    "pow": arithmetic.power,
    "mod": arithmetic.mod
}


def check_input(tokens, token_len):
    if len(tokens) != token_len:
        print "Wrong number of tokens. Try again."
        return False
    else:
        for i in range(1, token_len):
            token = tokens[i]
            for char in token:
                if char not in "0123456789":
                    print "Please enter an operator followed by integer(s)."
                    return False
        return True

def main():
    while True:
        user_input = raw_input("> ")

        token = user_input.split(" ")

        if token[0] == "q":
            exit(0)
        elif token[0] in ("+", "-", "*", "/", "pow", "mod"):
            if check_input(token, 3):
                # try to convert strings to ints or floats if dividing

                # then run appropriate function
                function_to_run = operator_dict[token[0]] #this will be a function in arithmetic

                if token[0] == "/":
                    print function_to_run(float(token[1]), float(token[2]))
                else:
                    print function_to_run(int(token[1]), int(token[2]))

        elif token[0] in ("square", "cube"):
            if check_input(token, 2):
                function_to_run = operator_dict[token[0]] #this will be a function in arithmetic
                print function_to_run(int(token[1]))
        else:
            print "Something is wrong"

main()