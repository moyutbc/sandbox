import csv
from sympy import Matrix, Symbol, S, Rational
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
    if f00 == 'f0_04.csv':

        tmp = [variable[1] + Rational(4,15)]
        polynomial.append(tmp)
        tmp = [variable[4] + Rational(7,15)]
        polynomial.append(tmp)

        polynomial.extend([variable[0] + 1])
        print(polynomial[-1])
        polynomial.extend([variable[1] + variable[-1]])
        print(polynomial[-1])
    if f00 == 'f0_05.csv':
        polynomial.extend([variable[0] + variable[-1]])
        print(polynomial[-1])

        # print
        print(polynomial)

    # solve
    ans = solve(polynomial, variable)
    print('--- ans ---')
    print(ans)
    print('')

    # fini
    file_f.pop()


if __name__ == '__main__':
    
    file_f = ['f22.csv', 'f23.csv', 'f24.csv',
              'f33.csv', 'f34.csv',
              'f44.csv']
    
    solve_case('f0_01.csv', 'fc_01.csv', file_f, 'x_01.csv')
    solve_case('f0_04.csv', 'fc_04.csv', file_f, 'x_04.csv')
    solve_case('f0_05.csv', 'fc_05.csv', file_f, 'x_05.csv')


