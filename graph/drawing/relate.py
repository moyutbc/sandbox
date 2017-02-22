import json
import csv
import sys
from pprint import pprint
from sympy import solve, symbols, Rational, sqrt
import numpy as np
import logging

def load_length(csvfilename):
    """ ２頂点間の長さが定義されたCSVファイルを読み込み、5*5の配列にして返す。
    """
    arr = np.empty((0,5), float)
    with open(csvfilename) as f:
        str_list = csv.reader(f)
        for row in str_list:
            tmp = [eval(n) for n in row]
            arr = np.append(arr, np.array([tmp]), axis=0)
    return arr

def get_formula_with_zero(co_list):
    """ 頂点v1(a,b,c), 頂点v2(d,e,f), 頂点v3(g,h,i)のa,b,c,e,f,iが0となる式を作る
    """
    f = []
    index = [[0,0], [0,1], [0,2], [1,1], [1,2],[2,2]]
    for i in index:
        f.append(co_list[i[0]][i[1]])
    return f

def is_valid_length(l):
    """ 辺の長さが有効な値かどうか判定する

    0.0625で割り切れる時、有効な値としている
    """
    rtn = True 
    if isinstance(l, float) and l % 0.0625 != 0:
        rtn = False
    logging.debug('%s is %s' % (l, rtn))
    return rtn


def get_formula_with_length(co_list, len_arr):
    """ 2頂点間の長さから式を立てる
    """
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

def is_valid_inner_product(ip):
    """ 内積が有効な値かどうか判定する
    """
    return True
    rtn = False
    if ip % 0.125 == 0:
        rtn = True
    return rtn

def get_formula_with_inner_product(co_list, ip_list):
    """ 2頂点間の内積から式を立てる
    """
    ax, ay, az = co_list[0] 
    bx, by, bz = co_list[1]
    cx, cy, cz = co_list[2]
    dx, dy, dz = co_list[3]
    ex, ey, ez = co_list[4]
    f = []

    if is_valid_inner_product(ip_list['ip22']) == 0:
        f.append(bx * bx + by * by + bz * bz - ip_list['ip22'])
    if is_valid_inner_product(ip_list['ip23']) == 0:
        f.append(bx * cx + by * cy + bz * cz - ip_list['ip23'])
    if is_valid_inner_product(ip_list['ip24']) == 0:
        f.append(bx * dx + by * dy + bz * dz - ip_list['ip24'])
    if is_valid_inner_product(ip_list['ip25']) == 0:
        f.append(bx * ex + by * ey + bz * ez - ip_list['ip25'])
    if is_valid_inner_product(ip_list['ip33']) == 0:
        f.append(cx * cx + cy * cy + cz * cz - ip_list['ip33'])
    if is_valid_inner_product(ip_list['ip34']) == 0:
        f.append(cx * dx + cy * dy + cz * dz - ip_list['ip34'])
    if is_valid_inner_product(ip_list['ip35']) == 0:
        f.append(cx * ex + cy * ey + cz * ez - ip_list['ip35'])
    if is_valid_inner_product(ip_list['ip44']) == 0:
        f.append(dx * dx + dy * dy + dz * dz - ip_list['ip44'])
    if is_valid_inner_product(ip_list['ip45']) == 0:
        f.append(dx * ex + dy * ey + dz * ez - ip_list['ip45'])
    if is_valid_inner_product(ip_list['ip55']) == 0:
        f.append(ex * ex + ey * ey + ez * ez - ip_list['ip55'])

    return f


def load_inner_product(filename):
    """ 内積が定義されたファイルを読み込み、リストとして返す
    """
    ip = []
    with open(filename) as f:
        ip = json.load(f)
    return ip

def assume_coordinates():
    """ 連立方程式で使用する文字を宣言する
    """
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


def show_raw_answer(answer):
    """ 連立方程式の答えを表示する
    """
    for vertex in answer:
        alt = {}
        for k, v in vertex.items():
            alt[str(k)] = v

        ax, ay, az = [alt.get('ax', '@'), alt.get('ay', '@'), alt.get('az', '@')]
        bx, by, bz = [alt.get('bx', '@'), alt.get('by', '@'), alt.get('bz', '@')]
        cx, cy, cz = [alt.get('cx', '@'), alt.get('cy', '@'), alt.get('cz', '@')]
        dx, dy, dz = [alt.get('dx', '@'), alt.get('dy', '@'), alt.get('dz', '@')]
        ex, ey, ez = [alt.get('ex', '@'), alt.get('ey', '@'), alt.get('ez', '@')]

        print('# raw')
        for li in [[ax,ay,az],[bx,by,bz,],[cx,cy,cz],[dx,dy,dz],[ex,ey,ez]]:
            x, y, z = li
            print('%s, %s, %s' % (x, y, z))

        print('# float')
        for li in [[ax,ay,az],[bx,by,bz,],[cx,cy,cz],[dx,dy,dz],[ex,ey,ez]]:
            x, y, z = li
            if not isinstance(x, str) and not isinstance(y, str) and not isinstance(z, str):
                print('%s, %s, %s' % (x.evalf(5), y.evalf(5), z.evalf(5)))
            else:
                print('%s, %s, %s' % (x, y, z))

        print('')

def _main(argv):
    """ 連立方程式を解くメイン関数

    以下の手順で連立方程式を解く
    # 01. 連立方程式で使用する変数（代数）を宣言する
    # 02. 01. で宣言した変数のうち、0に決まるものから立式する
    # 03. 2頂点間の長さが定義されたファイルを読み込む
    # 04. 2頂点間の長さから式を立てる
    # 05. 2頂点間の内積が定義されたファイルを読み込む
    # 06. 2頂点間の内積から式を立てる
    # 07. 連立方程式を解く
    # 08. 答えを表示する

    """

    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                        filename='tmp.log',
                        level=logging.DEBUG)
    print('----------')
    print('input: length=>[%s], inner_product=>[%s]' % (argv[1], argv[2]))

    formulas = []
    # 
    # 01. 連立方程式で使用する変数（代数）を宣言する
    co_list = assume_coordinates()
    # print('co_list: %s' % co_list)

    # 02. 01. で宣言した変数のうち、0に決まるものから立式する
    f0 = get_formula_with_zero(co_list)
    formulas.extend(f0)
    # print('formula_zero: %s' % f0)

    # 03. 2頂点間の長さが定義されたファイルを読み込む
    len_arr = load_length(argv[1])

    # 04. 2頂点間の長さから式を立てる
    f1 = get_formula_with_length(co_list, len_arr)
    formulas.extend(f1)
    print('formula_length: %s' % f1)

    # 05. 2頂点間の内積が定義されたファイルを読み込む
    ip_list = load_inner_product(argv[2])

    # 06. 2頂点間の内積から式を立てる
    f2 = get_formula_with_inner_product(co_list, ip_list)
    formulas.extend(f2)
    print('formula_inner_product: %s ' % f2)
    
    # 07. 連立方程式を解く
    va_list = [e2 for e1 in co_list for e2 in e1]
    # print('formulas:', end='')
    # pprint(formulas)
    print('variables: %s' % va_list)
    ans = solve(formulas, va_list, dict=True)

    # 08. 答えを表示する
    show_raw_answer(ans)


# プログラムを実行するとここから処理が始まる
if __name__ == '__main__':
  

    if len(sys.argv) != 3:
        print('usage: python3 ./relate.py [length.csv] [inner_product.json]')
    else:
        _main(sys.argv)

