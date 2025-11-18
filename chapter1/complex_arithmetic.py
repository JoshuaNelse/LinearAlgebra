from functools import reduce

def get_next_number(expression):
    number_string = ""
    return_expression = expression

    for char in expression:
        if len(number_string) > 0 and  char in ["-", "+", ")"]:
            if char != "-":
                return_expression = return_expression[1:]
            break
        if char in ["-", "i", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            number_string += char
        return_expression = return_expression[1:]

    return number_string, return_expression

def complex_add(exp: str):
    # expect format like (a+bi)+(c+di)
    clean_expression = (exp.replace("(", " ")
           .replace(")", "")
           .replace(" ", ""))

    real_numbers = []
    complex_numbers = []

    while len(clean_expression) > 0:
        next_number, new_expression = get_next_number(clean_expression)
        if "i" in next_number:
            next_number = next_number.replace("i", "")
            num = int(next_number) if "-" not in next_number else int(next_number.replace("-", ""))*-1
            complex_numbers.append(num)
        else:
            num = int(next_number) if "-" not in next_number else int(next_number.replace("-", ""))*-1
            real_numbers.append(num)
        clean_expression = new_expression

    real_part = reduce(lambda x, y: int(x) + int(y), real_numbers)
    imaginary_part = reduce(lambda x, y: int(x) + int(y), complex_numbers)

    sign = "+" if imaginary_part >= 0 else "" # imaginary's negative sign overrides the "+"
    return f"{real_part}{sign}{imaginary_part}i"

def complex_multiply(exp: str):
    # expect format like (a+bi)*(c+di)
    part1, part2 = exp.split("*")

    part1 = part1.replace("(", "").replace(")", "")
    part2 = part2.replace("(", "").replace(")", "")

    # so now we have part1 a+bi and part2 c+di
    # time to parse it further so we can create ac + adi + cbi + dbi^2
    # which shortens to ac-db+(ad+cb)i
    a, new_expression = get_next_number(part1)
    b, _ = get_next_number(new_expression)
    c, new_expression = get_next_number(part2)
    d, _ = get_next_number(new_expression)

    b = b.replace("i", "")
    d = d.replace("i", "")

    a = int(a) if "-" not in a else int(a.replace("-", ""))*-1
    b = int(b) if "-" not in b else int(b.replace("-", ""))*-1
    c = int(c) if "-" not in c else int(c.replace("-", ""))*-1
    d = int(d) if "-" not in d else int(d.replace("-", ""))*-1

    real = (a*c)-(d*b)
    imaginary = (a*d)+(c*b)
    sign = "+" if imaginary >= 0 else ""
    return f"{real}{sign}{imaginary}i"

