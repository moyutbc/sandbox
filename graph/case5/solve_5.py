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
    if file_f == 'f0_07.csv':
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
    
    file_f = ['f22.csv', 'f23.csv', 'f24.csv', 'f25.csv',
              'f34.csv', 'f34.csv', 'f35.csv',
              'f44.csv', 'f45.csv',
              'f55.csv']
    
    solve_case('f0_01.csv', 'fc_01.csv', file_f, 'x_01.csv')
    solve_case('f0_02.csv', 'fc_02.csv', file_f, 'x_02.csv')
    solve_case('f0_03.csv', 'fc_03.csv', file_f, 'x_03.csv')
    solve_case('f0_04.csv', 'fc_04.csv', file_f, 'x_04.csv')
    solve_case('f0_05.csv', 'fc_05.csv', file_f, 'x_05.csv')
    solve_case('f0_06.csv', 'fc_06.csv', file_f, 'x_06.csv')
    solve_case('f0_07.csv', 'fc_07.csv', file_f, 'x_07.csv')
    solve_case('f0_08.csv', 'fc_08.csv', file_f, 'x_08.csv')
    solve_case('f0_09.csv', 'fc_09.csv', file_f, 'x_09.csv')
    solve_case('f0_10.csv', 'fc_10.csv', file_f, 'x_10.csv')


