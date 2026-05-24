from main import *

triangle_1 = {
    "a": 3.0,
    "b": 4.0,
    "c": 5.0,
    "mA": 36.8698976458,
    "mB": 53.1301023542,
    "mC": 90.0,
    "area": 6.0
}

triangle_2 = {
    "a": 7.0,
    "b": 10.0,
    "c": 13.0,
    "mA": 32.2042277855,
    "mB": 49.5825625847,
    "mC": 98.2132096298,
    "area": 34.6410161514
}

def test_sas(triangle:dict):
    return f"""{solve_sas(triangle["a"], triangle["mB"], triangle["c"])}
{triangle}"""
    
def test_ass(triangle:dict):
    return f"""{solve_ass(triangle["mA"], triangle["a"], triangle["b"])}
{triangle}"""

def test_asa(triangle:dict):
    return f"""{solve_asa(triangle["mA"], triangle["b"], triangle["mC"])}
{triangle}"""

def test_aas(triangle:dict):
    return f"""{solve_aas(triangle["mA"], triangle["mB"], triangle["a"])}
{triangle}"""

def test_sss(triangle:dict):
    return f"""{solve_sss(triangle["a"], triangle["b"], triangle["c"])}
{triangle}"""

def full_test():
    current = 1
    for triangle in [triangle_1, triangle_2]:
        print(f"""
Trianle {current}
sas:
{test_sas(triangle)}
ass:
{test_ass(triangle)}
asa
{test_asa(triangle)}
aas
{test_aas(triangle)}
sss
{test_sss(triangle)}
"""
        )
        current += 1

full_test()
