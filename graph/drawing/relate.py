import json
import csv
import sys
from pprint import pprint
from sympy import solve, symbols, Rational, sqrt
import numpy as np

def load_length(csvfilename):
    arr = np.empty((0,5), float)
    with open(csvfilename) as f:
        str_list = csv.reader(f)
        for row in str_list:
            tmp = [eval(n) for n in row]
            arr = np.append(arr, np.array([tmp]), axis=0)
    return arr

def is_valid_length(l):
    return True
    rtn = False
    if l % 0.25 == 0:
        rtn = True
    return rtn

def get_formula_with_zero(co_list):
    f = []
    index = [[0,0], [0,1], [0,2], [1,1], [1,2],[2,2]]
    for i in index:
        f.append(co_list[i[0]][i[1]])
    return f


def get_formula_with_length(co_list, len_arr):
    f = []
    index = [[0,1], [0,2], [0,3], [0,4], [1,2],
             [1,3], [1,4], [2,3], [2,4], [3,4]]
    for i in index:
        if is_valid_length(len_arr[i[0], i[1]]):
            s = co_list[i[0]]
            d = co_list[i[1]]
            tmp = (s[0] - d[0])**2 + (s[1] - d[1])**2 + (s[2] - d[2])**2 \
                - (len_arr[i[0], i[1]])**2
            f.append(tmp)
    return f

def get_formula_with_inner_product(co_list, ip_list):
    ax, ay, az = co_list[0] 
    bx, by, bz = co_list[1]
    cx, cy, cz = co_list[2]
    dx, dy, dz = co_list[3]
    ex, ey, ez = co_list[4]
    f = []

    N = 0.025
    if ip_list['ip22'] % N == 0:
        f.append(bx * bx + by * by + bz * bz - ip_list['ip22'])
    if ip_list['ip23'] % N == 0:
        f.append(bx * cx + by * cy + bz * cz - ip_list['ip23'])
    if ip_list['ip24'] % N == 0:
        f.append(bx * dx + by * dy + bz * dz - ip_list['ip24'])
    if ip_list['ip25'] % N == 0:
        f.append(bx * ex + by * ey + bz * ez - ip_list['ip25'])
    if ip_list['ip33'] % N == 0:
        f.append(cx * cx + cy * cy + cz * cz - ip_list['ip33'])
    if ip_list['ip34'] % N == 0:
        f.append(cx * dx + cy * dy + cz * dz - ip_list['ip34'])
    if ip_list['ip35'] % N == 0:
        f.append(cx * ex + cy * ey + cz * ez - ip_list['ip35'])
    if ip_list['ip44'] % N == 0:
        f.append(dx * dx + dy * dy + dz * dz - ip_list['ip44'])
    if ip_list['ip45'] % N == 0:
        f.append(dx * ex + dy * ey + dz * ez - ip_list['ip45'])
    if ip_list['ip55'] % N == 0:
        f.append(ex * ex + ey * ey + ez * ez - ip_list['ip55'])

    return f


def load_inner_product(filename):
    ip = []
    with open(filename) as f:
        ip = json.load(f)
    return ip

def assume_coordinates():
    ax, ay, az = symbols('ax ay az', negative=False)
    bx, by, bz = symbols('bx by bz', negative=False)
    cx, cy, cz = symbols('cx cy cz')
    dx, dy, dz = symbols('dx dy dz')
    ex, ey, ez = symbols('ex ey ez')
    co_list = [[ax, ay, az],
               [bx, by, bz],
               [cx, cy, cz],
               [dx, dy, dz],
               [ex, ey, ez]]
    return co_list

def make_formulas(valist, iplist):
    ax, ay, az = valist[0:3]
    bx, by, bz = vblist[3:6]
    cx, cy, cz = vclist[6:9]
    dx, dy, dz = vdlist[9:12]
    ex, ey, ez = velist[12:15]

    formulas = []
    formulas.append(ax)
    formulas.append(ay)
    formulas.append(az)
    formulas.append(by)
    formulas.append(bz)
    formulas.append(cz)
    formulas.append(bx**2 + by**2 + bz**2 - iplist['ip22'])
    formulas.append(cx**2 + cy**2 + cz**2 - iplist['ip33'])
    formulas.append(dx**2 + dy**2 + dz**2 - iplist['ip44'])
    formulas.append(ex * ex + ey * ey + ez * ez - iplist['ip55'])

    formulas.append(bx * cx                     - iplist['ip23'])
    formulas.append(bx * dx                     - iplist['ip24'])
    formulas.append(bx * ex                     - iplist['ip25'])
    formulas.append(cx * dx + cy * dy           - iplist['ip34'])
    formulas.append(cx * ex + cy * ey           - iplist['ip35'])
    formulas.append(dx * ex + dy * ey + dz * ez - iplist['ip45'])
    return formulas

def _solve(jsonfilename):
    
    print(jsonfilename)
    inner_products = load_inner_product(jsonfilename)
    va_list = define_variables()
    formulas = make_formulas(va_list, inner_products)
    print(formulas)
    ans = solve(formulas, va_list)
    if len(ans) != 0:
        print('len(and): %s' % len(ans))
        ans = list(ans[0])
        print('%s, %s, %s, 3' % (ans[0], ans[1], ans[2]))
        print('%s, %s, %s, 3' % (ans[3], ans[4], ans[5]))
        print('%s, %s, %s, 3' % (ans[6], ans[7], ans[8]))
        print('%s, %s, %s, 3' % (ans[9], ans[10], ans[11]))
        print('%s, %s, %s, 3' % (ans[12], ans[13], ans[14]))

def _main(argv):

    formulas = []
    co_list = assume_coordinates()
    # print('co_list: %s' % co_list)

    f0 = get_formula_with_zero(co_list)
    formulas.extend(f0)
    # print('formula_zero: %s' % f0)

    len_arr = load_length(argv[1])
    f1 = get_formula_with_length(co_list, len_arr)
    formulas.extend(f1)
    # print('formula_length: %s' % f1)

    ip_list = load_inner_product(argv[2])
    f2 = get_formula_with_inner_product(co_list, ip_list)
    formulas.extend(f2)
    # print('formula_inner_product: %s ' % f2)
    
    va_list = [e2 for e1 in co_list for e2 in e1]
    print('variables:')
    pprint(formulas)
    print('variables: %s' % va_list)
    ans = solve(formulas, va_list)
    if len(ans) == 0:
        print('No ans')
        return
    for i, st in enumerate(ans):
        print('# ans-%s' % i)
        for (var, val) in zip(va_list, st):
            print('%s: %s' % (str(var), val))
        # print('%s: %s, %s, %s' % (i, x, y, z))


if __name__ == '__main__':

        if len(sys.argv) != 3:
            print('usage: ./relate.py [length.csv] [inner_product.json]')
        else:
            _main(sys.argv)

#    _solve('graph501.json')
#    _solve('graph502.json')
#    _solve('graph503.json')
#    _solve('graph504.json')
#    _solve('graph505.json')
#    _solve('graph506.json')
#    _solve('graph507.json')
#    _solve('graph508.json')
#    _solve('graph510.json')
#    _solve('graph511.json')
#    _solve('graph512.json')
#    _solve('graph513.json')
#    _solve('graph515.json')
#    _solve('graph516.json')
#    _solve('graph517.json')
#    _solve('graph518.json')
#    _solve('graph519.json')
#    _solve('graph520.json')
#
