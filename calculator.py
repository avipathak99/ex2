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


def check_number_of_tokens(tokens, token_len):
    if len(tokens) != token_len:
        print "Wrong number of tokens. Try again."
        return False
    return True

def check_integers(tokens):
    for i in range(1, len(tokens)):
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
        elif token[0] in ("+", "-", "*", "/"):
            if check_integers(token):
                function_to_run = operator_dict[token[0]] 

                # this should be the first number
                result = token[1]

                #starting at 2 since result is index 1. this lets us input more than just 2 integers, ex. + 2 2 2 
                for i in range(2, len(token)):
                    if token[0] == "/":
                        result = float(result)
                        result = function_to_run(result, float(token[i]))
                        
                    else:
                        result = int(result)
                        result = function_to_run(result, int(token[i]))
                
                print result

        elif token[0] in ("pow", "mod"):
            if check_number_of_tokens(token, 3):
                # try to convert strings to ints or floats if dividing
                if check_integers(token):
                # then run appropriate function
                    function_to_run = operator_dict[token[0]] #this will be a function in arithmetic
                    print function_to_run(int(token[1]), int(token[2]))

        elif token[0] in ("square", "cube"):
            if check_number_of_tokens(token, 2):
                if check_integers(token):
                    function_to_run = operator_dict[token[0]] #this will be a function in arithmetic
                    print function_to_run(int(token[1]))
        else:
            print "Something is wrong"

main()