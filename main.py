import math
import json
import os

def rad_to_deg(rad):
    return (180 * rad) / math.pi

def deg_to_rad(deg):
    return (deg * math.pi) / 180


def asin_law(a, b, mA):
    """Solves for angle B given sides a and b, and angle A."""
    value = (b * math.sin(deg_to_rad(mA))) / a
    value = max(-1, min(1, value))
    return rad_to_deg(math.asin(value))

def sin_law(a, mA, mB):
    """Solves for side b given side a, and angles A and B."""
    return (a * math.sin(deg_to_rad(mB))) / math.sin(deg_to_rad(mA))

def cos_law(b, c, mA):
    """Solves for side a given sides b and c, and angle A."""
    return math.sqrt(b**2 + c**2 - 2 * b * c * math.cos(deg_to_rad(mA)))

def acos_law(a, b, c):
    """Solves for angle C given sides a, b, and c."""
    return rad_to_deg(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))

def heron(a, b, c):
    """Finds the Area of the triangle given sides a, b, and c."""
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def solve_sas(a, b, mC):
    c = cos_law(a, b, mC)
    mA = asin_law(c, a, mC)
    mB = asin_law(c, b, mC)
    area = heron(c, b, a)

    return {"a":a, "b":b, "c":c, "mA":mA, "mB":mB, "mC":mC, "area":area}

def solve_ass(mA, a, b):
    mB = asin_law(a, b, mA)
    mC = 180 - (mA + mB)
    c = sin_law(a, mA, mC)
    area = heron(a, b, c)
    return {"a":a, "b":b, "c":c, "mA":mA, "mB":mB, "mC":mC, "area":area}

def solve_asa(mA, b, mC):
    mB = 180 - (mA + mC)
    a = sin_law(b, mB, mA)
    c = sin_law(b, mB, mC)
    area = heron(a, b, c)
    return {"a":a, "b":b, "c":c, "mA":mA, "mB":mB, "mC":mC, "area":area}

def solve_aas(a, mA, mB):
    mC = 180 - (mA + mB)
    b = sin_law(a, mA, mB)
    c = sin_law(a, mA, mC)
    area = heron(a, b, c)
    return {"a":a, "b":b, "c":c, "mA":mA, "mB":mB, "mC":mC, "area":area}

def solve_sss(a, b, c):
    mA = acos_law(c, b, a)
    mB = acos_law(c, a, b)
    mC = 180 - (mA + mB)
    area = heron(a, b, c)
    return {"a":a, "b":b, "c":c, "mA":mA, "mB":mB, "mC":mC, "area":area}


def set_len_num_str(num: int | float) -> str:
    # Try progressively fewer significant digits until it fits in 5 chars
    for precision in range(5, 0, -1):
        s = f"{num:.{precision}g}"
        if len(s) <= 5:
            return s.rjust(5)
    # If still too long, fall back to integer rounding
    s = str(round(num))
    if len(s) <= 5:
        return s.rjust(5)
    # Absolute last resort: scientific notation trimmed to 5 chars
    s = f"{num:.1e}"
    if len(s) > 5:
        s = s[:5]

    return s.rjust(5)

def ascii_triangle(triangle:dict):
    with open("./triangle.json", "r") as file:
        art:str = json.load(file)
    return art.format(
        mA=set_len_num_str(triangle['mA']), 
        b=set_len_num_str(triangle['b']), 
        c=set_len_num_str(triangle['c']), 
        area=set_len_num_str(triangle['area']), 
        mB=set_len_num_str(triangle["mB"]),
        a=set_len_num_str(triangle['a']), 
        mC=set_len_num_str(triangle['mC'])
    )


def solve_input_sas(a, b, mC):
    triangle = solve_sas(a, b, mC)
    print(ascii_triangle(triangle))
    for key in triangle:
        print(f"{key} = {triangle[key]}")

def solve_input_ass(mA, b, a):
    triangle = solve_ass(mA, a, b)
    print(ascii_triangle(triangle))
    for key in triangle:
        print(f"{key} = {triangle[key]}")

def solve_input_asa(mA, b, mC):
    triangle = solve_asa(mA, b, mC)
    print(ascii_triangle(triangle))
    for key in triangle:
        print(f"{key} = {triangle[key]}")

def solve_input_aas(mA, mB, a):
    triangle = solve_aas(a, mA, mB)
    print(ascii_triangle(triangle))
    for key in triangle:
        print(f"{key} = {triangle[key]}")

def solve_input_sss(a, b, c):
    triangle = solve_sss(a, b, c)
    print(ascii_triangle(triangle))
    for key in triangle:
        print(f"{key} = {triangle[key]}")


def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nWhat kind of triangle do you want to solve?")
        triangle_types = ["SAS", "ASS", "ASA", "AAS", "SSS"]
        current = 1
        for triangle_type in triangle_types:
            print(f"{current}.) {triangle_type}")
            current += 1
        print("type the number here:")
        type_input = input(">>> ")
        try:
            type_input = int(type_input)
            if type_input == 1:
                a = float(input("input side a: "))
                b = float(input("input side b: "))
                mC = float(input("input angle C in degrees: "))
                solve_input_sas(a, b, mC)
                new = input("press enter to reset")
            elif type_input == 2:
                mA = float(input("input angle A in degrees: "))
                b = float(input("input side b:"))
                a = float(input("input side a: "))
                solve_input_ass(mA, b, a)
                new = input("press enter to reset")
            elif type_input == 3:
                mA = float(input("input angle A in degrees: "))
                b = float(input("input side b: "))
                mC = float(input("input angle C in degrees: "))
                solve_input_asa(mA, b, mC)
                new = input("press enter to reset")
            elif type_input == 4:
                mA = float(input("input angle A in degrees: "))
                b = float(input("input side b: "))
                a = float(input("input side a: "))
                solve_input_aas(mA, b, a)
                new = input("press enter to reset")
            elif type_input == 5:
                a = float(input("input side a: "))
                b = float(input("input side b: "))
                c = float(input("input side c: "))
                solve_input_sss(a, b, c)
                new = input("press enter to reset")
            else:
                print("Not a valid input.\n")
        except ValueError:
            print("Not a valid input\n")


if __name__ == "__main__":
    main()
