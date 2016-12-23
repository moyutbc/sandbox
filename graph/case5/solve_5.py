import csv
from sympy import Matrix, Symbol, S
from sympy.solvers import solve

def load_matrix_sym(filename):
    l = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            l.extend(row)
    for i in range(len(l)):
        l[i] = l[i].strip()
    return l


def load_matrix_int(filename):
    l = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
             l.extend([int(x) for x in row])
    return Matrix(l)


def solve_case(f00, fc, file_in, x_in):

    # ini
    file_f = file_in
    file_x = x_in

    #print
    print('### case: ' + f00 + ' ###')

    # append
    file_f.append(fc)

    # load x-matrix
    x = load_matrix_sym(file_x)

    # get variable list
    variable = []
    for v in x:
        if not v.isdigit() :
            variable.append(v)
    variable = list(set(variable))
    variable.sort()

    # define symbol
    for i in range(len(variable)):
        variable[i] = Symbol(variable[i])

    x = Matrix(x)
 
    print('--- variable ---')
    print(variable)

    # get polynomial list
    print('--- input ---')
    polynomial = []
    for f_in in file_f:
        # load f-matrix
        f = load_matrix_int(f_in)
    
        formula = f.dot(x)
        if(f_in == fc):
            formula = formula + 1
        polynomial.append(formula)

        # print 
        print(f_in + ': ', end="")
        print(formula)
    
    ## special logic ##
    if file_f == 'case5-07/f0_07.csv':
        tmp = [b + d]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
    if file_f == 'case5-12/f0_12.csv':
        tmp = [a + Rational(1,4)]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
        tmp = [b + Rational(-1,4)]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
    if file_f == 'case5-14/f0_14.csv':
        tmp = [c + i]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
        tmp = [d + j]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
    if file_f == 'case5-15/f0_15.csv':
        tmp = [a + Rational(1,4)]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
        tmp = [b + Rational(-1,4)]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
    if file_f == 'case5-16/f0_16.csv':
        tmp = [a + Rational(1,3)]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
        tmp = [a + d]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
        tmp = [b + Rational(1,6)]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
        tmp = [b + c]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
        tmp = [f + i]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
    if file_f == 'case5-17/f0_17.csv':
        tmp = [f + Rational(1,4)]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
        tmp = [c + g]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
        tmp = [e + h]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
    if file_f == 'case5-18/f0_18.csv':
        tmp = [a + Rational(1,4)]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
        tmp = [b + f]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
        tmp = [c + g]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
#    if file_f == 'case5-18/f0_18.csv':
#        tmp = [a + Rational(1,4)]
#        print(file_f + ': ', end="")
#        print(tmp)
#        polynomial.append(tmp)
#        tmp = [b + d]
#        print(file_f + ': ', end="")
#        print(tmp)
#        polynomial.append(tmp)
    if file_f == 'case5-19/f0_19.csv':
        tmp = [a + Rational(1,4)]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
        tmp = [b + Rational(-1,4)]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
    if file_f == 'case5-20/f0_20.csv':
        tmp = [a + Rational(1,4)]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)
        tmp = [b + d]
        print(file_f + ': ', end="")
        print(tmp)
        polynomial.append(tmp)

    # solve
    ans = solve(polynomial, variable)
    print('--- ans ---')
    print(ans)
    print('')

    # fini
    file_f.pop()


if __name__ == '__main__':
    
    file_special = [['case5-01/', 'f0_01.csv', 'fc_01.csv', 'x_01.csv'],
                    ['case5-02/', 'f0_02.csv', 'fc_02.csv', 'x_02.csv'],
                    ['case5-03/', 'f0_03.csv', 'fc_03.csv', 'x_03.csv'],
                    ['case5-04/', 'f0_04.csv', 'fc_04.csv', 'x_04.csv'],
                    ['case5-05/', 'f0_05.csv', 'fc_05.csv', 'x_05.csv'],
                    ['case5-06/', 'f0_06.csv', 'fc_06.csv', 'x_06.csv'],
                    ['case5-07/', 'f0_07.csv', 'fc_07.csv', 'x_07.csv'],
                    ['case5-08/', 'f0_08.csv', 'fc_08.csv', 'x_08.csv'],
                    ['case5-09/', 'f0_09.csv', 'fc_09.csv', 'x_09.csv'],
                    ['case5-10/', 'f0_10.csv', 'fc_10.csv', 'x_10.csv'],
                    ['case5-11/', 'f0_11.csv', 'fc_11.csv', 'x_11.csv'],
                    ['case5-12/', 'f0_12.csv', 'fc_12.csv', 'x_12.csv'],
                    ['case5-13/', 'f0_13.csv', 'fc_13.csv', 'x_13.csv'],
                    ['case5-14/', 'f0_14.csv', 'fc_14.csv', 'x_14.csv'],
                    ['case5-15/', 'f0_15.csv', 'fc_15.csv', 'x_15.csv'],
                    ['case5-16/', 'f0_16.csv', 'fc_16.csv', 'x_16.csv'],
                    ['case5-17/', 'f0_17.csv', 'fc_17.csv', 'x_17.csv'],
                    ['case5-18/', 'f0_18.csv', 'fc_18.csv', 'x_18.csv'],
                    ['case5-19/', 'f0_19.csv', 'fc_19.csv', 'x_19.csv'],
                    ['case5-20/', 'f0_20.csv', 'fc_20.csv', 'x_20.csv'],
                    ['case5-21/', 'f0_21.csv', 'fc_21.csv', 'x_21.csv']]

    file_common = ['common/f22.csv',
                   'common/f23.csv',
                   'common/f24.csv',
                   'common/f25.csv',
                   'common/f34.csv',
                   'common/f34.csv',
                   'common/f35.csv',
                   'common/f44.csv',
                   'common/f45.csv',
                   'common/f55.csv']

    for li in file_special:
        solve_case(li[0] + li[1], li[0] + li[2], file_common, li[0] + li[3])
