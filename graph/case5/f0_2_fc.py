import sys
import csv

def main(file_in, file_out):

    # read data
    data = []
    with open(file_in, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            l = []
            for elem in line:
                l.append(int(elem))
            data.append(l)

    # process

    ## transponse
    data = list(map(list, zip(*data)))

    ## multiply by -1
    for li in data:
        for i in range(len(li)):
            li[i] = -1 * li[i]

    ## exchange
    for i in range(4, 14):
        ### shift
        for n in range(0, 10):
            data[i].insert(0,0)
        ### move
        tmp = data[i]
        data[i] = data[i + 10]
        data[i + 10] = tmp

    ## transponse
    data = list(map(list, zip(*data)))

    # write data
    with open(file_out, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

