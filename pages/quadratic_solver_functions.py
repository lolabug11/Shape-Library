import streamlit as st
from time import *
import numpy as np 
from math import sqrt
from fractions import Fraction
import numpy as np



def get_factors(number,get_negative_nums = True):
    if number < 0:
        number *= -1
        factors = {}
        for posible_factor in range(number):
            posible_factor += 1
            if number % posible_factor == 0:

                factors[posible_factor*-1] = number / posible_factor
                factors[posible_factor] = (number / posible_factor) * -1

        return factors
    elif number == 1:
        return {1:1,-1:-1}
    else:
        factors = {}
        for posible_factor in range(number):
            posible_factor += 1
            if number % posible_factor == 0:

                factors[posible_factor] = number / posible_factor
                if get_negative_nums:
                    factors[-posible_factor] = - (number/posible_factor)
        
        return factors


def factor_standered_form_quadratic(a,b,c):

    if a == 0:
        return False
    a = int(a)
    b = int(b)
    c = int(c)
    a_factors = get_factors(a)
    c_factors = get_factors(c)

    ac = a * c
    ac_factors = get_factors(ac)
    print(f'AC Factors {ac_factors}')
    ac_factor_pair_that_add_to_b = []

    equation  = None
    for factor in ac_factors:
        if factor + ac_factors[factor] == b:
            ac_factor_pair_that_add_to_b = [factor, ac_factors[factor]]
    if ac_factor_pair_that_add_to_b != []:
        if a == 1:
            if  ac_factor_pair_that_add_to_b[0] + ac_factor_pair_that_add_to_b[1] == b:
                if ac_factor_pair_that_add_to_b[0] < 0:
                    sign = '-'
                    ac_factor_pair_that_add_to_b[0] *= -1
                else:
                    sign = '+'

                if ac_factor_pair_that_add_to_b[1] < 0 :
                    sign2 = '-'
                    ac_factor_pair_that_add_to_b[1] *= -1
                else:
                    sign2 = '+'
                equation = f'(x {sign} {ac_factor_pair_that_add_to_b[0]})(x {sign2} {ac_factor_pair_that_add_to_b[1]})'
                return equation

        else:
            for a1 in a_factors:
                for c1 in c_factors:
                    c2 = c_factors[c1]
                    a2 = a_factors[a1]

                    if a1*c2 + a2*c1 == b and a1*a2==a and c1*c2 == c:
                        if c2 < 0:
                            sign = '-'
                            c2 *= -1
                        else:
                            sign = '+'
                        
                        if c1 < 0 :
                            sign2 = '-'
                            c1 *= -1
                        else:
                            sign2 = '+'
                        equation = f'({a1}x {sign2} {c1})({a2}x {sign} {c2})'

                        return equation
    else:
        return False
    



def find_roots_with_discriminant_greater_than_0(a:float,b:float,c:float,discriminant:float):
    r1 = (-b + sqrt(discriminant))/(2*a)
    r2 = (-b - sqrt(discriminant))/(2*a)
    if '.' in str((-b + sqrt(discriminant))/(2*a)):
        fraction_r1 = Fraction(str((-b + sqrt(discriminant))/(2*a)))
        fraction_r1 = fraction_r1.limit_denominator(1000)
    if '.' in str((-b - sqrt(discriminant))/(2*a)):
        fraction_r2 = Fraction(str((-b - sqrt(discriminant))/(2*a)))
        fraction_r2 = fraction_r2.limit_denominator(1000)
    vertex_x = (r1+r2)/2
    x = vertex_x
    vertex_y = ((a) * (vertex_x**2)) + (vertex_x * b) + c
    if '.' in str(vertex_y):
        vertex_y = Fraction(str(vertex_y))
        vertex_y = vertex_y.limit_denominator(1000)
    print(f'r1 = {r1} r2 = {r2}')
    if b >= 0:
        return [f'({fraction_r1},0)', f'({fraction_r2}, 0)', f'({vertex_x}, {vertex_y})', f'(-{b} + \N{SQUARE ROOT}{discriminant})/{2*a}', f'(-{b} - \N{SQUARE ROOT}{discriminant})/{2*a}', r1, r2]
    else:
        return [f'({fraction_r1},0)', f'({fraction_r2}, 0)', f'({vertex_x}, {vertex_y})', f'({-b} + \N{SQUARE ROOT}{discriminant})/{2*a}', f'({-b} - \N{SQUARE ROOT}{discriminant})/{2*a}', r1,r2]
def find_roots_with_discriminant_less_than_0(a:float,b:float,c:float,discriminant:float):
    r1 = round((-b + sqrt(-discriminant))/(2*a), 4)
    r2 = round((-b - sqrt(-discriminant))/(2*a), 4)
    return [(f'{r1}i,0'),str(f'{r2}i,0')]
    
def solve_standered_form(a=1,b=1,c=1) -> tuple:
    """Solves a quadratic equation givin a term b term and c term
    Args:
        a: the a term of the quadratic
        b: the b term of the quadratic
        c: the c term of the quadratic  
    Returns:
        Tuple: a tuple contaning
            - cords (list): returns a list of tuples that contains the cords of the [first_root,second_root (if applicable),vertex (if applicable)]
            - identifyer (int): returns a number to help identify how many roots the equation has. If the equation has one solution the identifyer will equal 1, if the equation has 2 real solutions the identifyer will equal 2, if the equation has 2 imaginary solutions the identifyer will equal 3
    """
    discriminant = (b**2) - (4 * a * c)
    # print(f'discriminant = {discriminant}')
    if discriminant == 0:
        r = (b*-1)/(2*a)
        return str(r),1
    elif discriminant > 0:
        return find_roots_with_discriminant_greater_than_0(a=a,b=b,c=c,discriminant= discriminant), 2
    else:
        return find_roots_with_discriminant_less_than_0(a = a, b = b, c = c, discriminant=discriminant), 3
    
def parse_factored_form_quadratic(quadratic:str):
    before_first_x = True
    before_first_parenthacys = True
    before_second_x = True
    a = ''
    b = ''
    c = ''
    d = ''
    # print(quadratic)
    for char in quadratic:     

        if char == '-' or char == '.':

            if before_first_x:

                a += char

            elif not before_first_x and before_first_parenthacys:

                b += char

            elif not before_first_x and not before_first_parenthacys and before_second_x:

                c += char

            else:

                d += char

        elif char.isnumeric():

            if before_first_x:

                a += char

            elif not before_first_x and before_first_parenthacys:

                b += char

            elif not before_first_x and not before_first_parenthacys and before_second_x:
                
                c += char

            else:

                d += char

        else:

            if char != '(':

                if char != '+':

                    if char != ' ':

                        if before_first_x:

                            before_first_x = False

                        elif not before_first_x and before_first_parenthacys:

                            before_first_parenthacys = False

                        elif not before_first_parenthacys and not before_first_x and before_second_x:

                            before_second_x = False

        # print(f'-------\nchar = {char}\nbefore_first_x = {before_first_x}\nbefore first perenthacys = {before_first_parenthacys}\n before second x = {before_second_x}\n a = {a}\n b = {b} \nc = {c}\nd = {d}\n-------')

    if a == '':

        a = 1.0

    else:

        a = float(a)
        a = round(a,4)

    if b == '':

        b = 1.0

    else:

        b = float(b)
        b = round(b,4)

    if c == '':

        c = 1.0

    else:

        c = float(c)
        c = round(c,4)

    if d == '':

        d = 1.0

    else:

        d = float(d)
        d = round(d,4)
    # print(f'A = {a} B = {b} C = {c} D = {d}')
    org_a = a
    org_b = b
    org_c = c
    a = org_a * org_c
    b = (org_a * d) + (org_c * b)
    c = org_b * d
    if b < 0 and c < 0:
        equation = f'{a}x^2 - {-b}x - {-c}'
    elif b < 0:
        equation = f'{a}x^2 - {-b}x + {c}'
    elif c < 0:
        equation = f'{a}x^2 + {b}x - {-c}'
    else:
        equation = f'{a}x^2 + {b}x + {c}'
    return equation,a,b,c




def GCD(a,b):
    if a < 0 :
        a *= -1
    if b < 0:
        b *= -1
    a_factor_pairs = {}
    b_factor_pairs = {}
    for number in range(int(a)):
        number += 1
        if a % number == 0:
            a_factor_pairs[number] = a/number
    for number in range(int(b)):
        number += 1
        if b % number == 0:
            b_factor_pairs[number] = b/number
    gcf = {}
    for key in a_factor_pairs:
        if key in b_factor_pairs and key :
            gcf[a] = [key,a_factor_pairs[key]]
            gcf[b] = [key,b_factor_pairs[key]]
    gcf = gcf[a][0]
    return gcf



def standered_form_inputs_input_on_change():
    st.session_state["last_tab_with_data_entered"] = "standered_form_inputs"
def factored_form_inputs_on_change():
    st.session_state["last_tab_with_data_entered"] = "factored_form_inputs"