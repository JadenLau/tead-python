from fractions import Fraction

def isRational(number_str):
    try:
        Fraction(number_str)
        return True # rational
    except ValueError:
        return False # irrational

print(isRational("1/3"))