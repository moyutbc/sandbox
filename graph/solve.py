import sys
import csv
from sympy import Matrix, Symbol, S, Rational
from sympy.solvers import solve

def load_variable_matrix(filename):
    l = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            l.extend(row)
    for i in range(len(l)):
        l[i] = l[i].strip()
    return l

def load_num_matrix(filename):
    l = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            l.extend([int(x) for x in row])
    return Matrix(l)

def get_variable_list(matx):
    variable = []
    for v in matx:
        if not v.isdigit() :
            variable.append(v)
    variable = list(set(variable))
    variable.sort()
    return variable

def init(fnns):

    li = []
    for fnn in fnns:
        f = load_num_matrix(fnn)
        li.append(f)

    return li

def make_formula_f0(f0_file, matx):

    f0 = load_num_matrix(f0_file)
    formula = f0.dot(matx)
    
    if '@' in f0_file:
        pass
    elif 'case5/03' in f0_file:
        formula = formula - Rational(15, 11)
    elif 'case5/04' in f0_file:
        formula = formula - Rational((2*(Rational(7,3)**(1/2)) - 2) **2)
    elif 'case5/10' in f0_file:
        formula = formula - Rational(16, 15)
    elif 'case5/13' in f0_file:
        formula = formula - Rational(12, 11)
    elif 'case5/14' in f0_file:
        formula = formula - (5-2*(5)**(1/2))**(1/2)
    elif 'case5/16' in f0_file:
        formula = formula - Rational(4, 3)
#    elif '17' in f0_file:
#        formula = formula - Rational(79, 60)
#    elif '18' in f0_file:
#        formula = formula - Rational(31, 15)
    else:
        formula = 0
        
    return [formula]

def make_formula_fc(fc_file, matx):

    fc = load_num_matrix(fc_file)
    formula = fc.dot(matx)
    formula = formula + 1
    return [formula]

def make_formula_fnns(fnn_list, matx):

    polynomial = []
    for fnn in fnn_list:
        formula = fnn.dot(matx)
        polynomial.append(formula)
    return polynomial

def make_formula_special(f0, variable):

    polynomial = []

    # 0: a, 1: b, 2: c, 3: d, 4: e,
    # 5: f, 6: g, 7: h, 8: i, 9: j

    if '@' in f0:
        pass
    elif 'case5/03' in f0:
        polynomial.append(variable[3] + Rational(2, 11))
    elif 'case5/04' in f0:
        polynomial.append(variable[2] + variable[7])
        polynomial.append(variable[5] + variable[8])
    elif 'case5/10' in f0:
        polynomial.append(variable[0] + Rational(16, 225))
        polynomial.append(variable[1] + Rational(28, 225))
    elif 'case5/13' in f0:
        polynomial.append(variable[4] + Rational(5, 11))
    elif 'case5/14' in f0:
        polynomial.append(variable[0] + Rational(19**(1/2), 18))
        polynomial.append(variable[2] + variable[8])
        polynomial.append(variable[3] + variable[9])
    elif 'case5/16' in f0:
        polynomial.append(variable[0] + Rational(1, 3))
        polynomial.append(variable[5] + variable[7])
    elif 'case5/17' in f0:
#        polynomial.append(variable[2] + Rational(-2, 15))
#        polynomial.append(variable[4] + Rational(-7, 30))
#        polynomial.append(variable[5] + Rational(1, 4))
        polynomial.append(variable[2] + variable[6])
        polynomial.append(variable[3] + variable[7])
    elif 'case5/18' in f0:
#        polynomial.append(variable[0] + Rational(1, 4))
#        polynomial.append(variable[1] + Rational(-2, 15))
#        polynomial.append(variable[2] + Rational(-7, 30))
        polynomial.append(variable[1] + variable[5])
        polynomial.append(variable[2] + variable[6])

    return polynomial

def _solve(fnns, f0, fc, x):

    print('-' * 10)
    print('case: %s' % f0)

    matx = load_variable_matrix(x)
    variable  = get_variable_list(matx)
    for i in range(len(variable)):
        variable[i] = Symbol(variable[i])
    matx = Matrix(matx)
    print('var: %s' % variable)

    polynomial = []
    polynomial.extend(make_formula_f0(f0, matx))
    polynomial.extend(make_formula_fc(fc, matx))
    polynomial.extend(make_formula_fnns(fnns, matx))
    polynomial.extend(make_formula_special(f0, variable))
    print('pol: %s' % polynomial)

    ans = solve(polynomial, variable)
    print('ans: %s' % ans)

    print('')

def _case4():
    file_common = ['case4/f22.csv',
            'case4/f23.csv',
            'case4/f24.csv',
            'case4/f33.csv',
            'case4/f34.csv',
            'case4/f44.csv']

    file_special = [['case4/', 'f0_01.csv', 'fc_01.csv', 'x_01.csv'],
            ['case4/', 'f0_04.csv', 'fc_04.csv', 'x_04.csv'],
            ['case4/', 'f0_05.csv', 'fc_05.csv', 'x_05.csv']]

    fnns = init(file_common)

    for li in file_special:
        _solve(fnns, li[0] + li[1], li[0] + li[2], li[0] + li[3])


def _case5():

    file_common = ['case5/common/f22.csv',
            'case5/common/f23.csv',
            'case5/common/f24.csv',
            'case5/common/f25.csv',
            'case5/common/f33.csv',
            'case5/common/f34.csv',
            'case5/common/f35.csv',
            'case5/common/f44.csv',
            'case5/common/f45.csv',
            'case5/common/f55.csv']
    file_special = [
            ['case5/01/', 'f0_01.csv', 'fc_01.csv', 'x_01.csv'],
            ['case5/02/', 'f0_02.csv', 'fc_02.csv', 'x_02.csv'],
            ['case5/03/', 'f0_03.csv', 'fc_03.csv', 'x_03.csv'],
            ['case5/04/', 'f0_04.csv', 'fc_04.csv', 'x_04.csv'],
            ['case5/05/', 'f0_05.csv', 'fc_05.csv', 'x_05.csv'],
            ['case5/06/', 'f0_06.csv', 'fc_06.csv', 'x_06.csv'],
            ['case5/07/', 'f0_07.csv', 'fc_07.csv', 'x_07.csv'],
            ['case5/08/', 'f0_08.csv', 'fc_08.csv', 'x_08.csv'],
            ['case5/09/', 'f0_09.csv', 'fc_09.csv', 'x_09.csv'],
            ['case5/10/', 'f0_10.csv', 'fc_10.csv', 'x_10.csv'],
            ['case5/11/', 'f0_11.csv', 'fc_11.csv', 'x_11.csv'],
            ['case5/12/', 'f0_12.csv', 'fc_12.csv', 'x_12.csv'],
            ['case5/13/', 'f0_13.csv', 'fc_13.csv', 'x_13.csv'],
            ['case5/14/', 'f0_14.csv', 'fc_14.csv', 'x_14.csv'],
            ['case5/15/', 'f0_15.csv', 'fc_15.csv', 'x_15.csv'],
            ['case5/16/', 'f0_16.csv', 'fc_16.csv', 'x_16.csv'],
            ['case5/17/', 'f0_17.csv', 'fc_17.csv', 'x_17.csv'],
            ['case5/18/', 'f0_18.csv', 'fc_18.csv', 'x_18.csv'],
            ['case5/19/', 'f0_19.csv', 'fc_19.csv', 'x_19.csv'],
            ['case5/20/', 'f0_20.csv', 'fc_20.csv', 'x_20.csv'],
            ]

    fnns = init(file_common)

    for li in file_special:
        _solve(fnns, li[0] + li[1], li[0] + li[2], li[0] + li[3])


if __name__ == '__main__':

    param = sys.argv[1]

    if param == 'all':
        _case4()
        _case5()
    elif param == '4':
        _case4()
    elif param == '5':
        _case5()

